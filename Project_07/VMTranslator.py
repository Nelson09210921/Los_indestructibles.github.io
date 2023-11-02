import os
import sys


class Parser:
    """Carga el archivo VM dado y proporciona funciones auxiliares para analizar los comandos."""

    def __init__(self, file_name: str):
        """Abre el archivo y se prepara para el análisis."""
        # Comando actual que se esta procesando.
        self.current_command = ""
        # Indice del comando actual.
        self.current = -1
        # Todos los comandos del archivo de entrada.
        self.commands = []
        # Abre el archivo y prepara para el análisis.
        # Eliminar todos los comentarios, líneas vacías y caracteres de espacio en blanco.
        file = open(file_name)
        for line in file:
            line = line.partition("//")[0]
            line = line.strip()
            if line:
                self.commands.append(line)
        file.close()

    def hasMoreCommands(self) -> bool:
        """Verifica si hay más comandos."""
        return (self.current + 1) < len(self.commands)

    def advance(self) -> None:
        """Lee el siguiente comando y lo convierte en el comando actual."""
        self.current += 1
        self.current_command = self.commands[self.current]

    def commandType(self) -> str:
        """Devuelve el tipo del comando actual."""
        # Define la lista de comandos aritméticos conocidos.
        arithmetic_commands = ["add", "sub", "neg",
                               "eq", "gt", "lt", "and", "or", "not"]
        # Extrae el comando actual de la línea de entrada.
        cmd = self.current_command.split(" ")[0]
        # Determina el tipo del comando actual.
        if cmd in arithmetic_commands:
            return "C_ARITHMETIC"
        elif cmd == "push":
            return "C_PUSH"
        elif cmd == "pop":
            return "C_POP"
        else:
            # C_LABEL
            # C_GOTO
            # C_IF
            # C_FUNCTION
            # C_RETURN
            # C_CALL
            raise NameError("Tipo de comando inesperado")

    def arg1(self) -> str:
        """Devuelve el primer argumento del comando actual. Para C_ARITHMETIC devuelve el comando en sí. No debería ser llamado para C_RETURN."""
        if self.commandType() == "C_ARITHMETIC":
            return self.current_command.split(" ")[0]
        else:
            return self.current_command.split(" ")[1]

    def arg2(self) -> int:
        """Devuelve el segundo argumento del comando actual. Válido solo para C_PUSH, C_POP, C_FUNCTION y C_RETURN."""
        return int(self.current_command.split(" ")[2])


class CodeWriter:
    """Conversor de código VM.
    Convierte los comandos VM a código ensamblador y los escribe en el archivo de salida."""

    def __init__(self, file_name: str):
        """Configura el convertidor de código para el archivo de salida dado."""
        # Almacena el nombre del archivo para referencias de etiquetas estáticas.
        self.file_name = file_name[:-4]
        # Abre el archivo de salida para escribir en él.
        self.file = open(file_name, "w")
        # Crea un contador de etiquetas para la creación de etiquetas únicas.
        self.label_counter = 0
        # Tabla de símbolos para operaciones aritméticas y símbolos de ensamblador.
        self.symbols = {
            # Operadores aritméticos
            "add": "M=D+M",
            "sub": "M=M-D",
            "and": "M=D&M",
            "or": "M=D|M",
            "neg": "M=-M",
            "not": "M=!M",
            "eq": "D;JEQ",
            "gt": "D;JGT",
            "lt": "D;JLT",
            # Símbolos de ensamblador
            "local": "@LCL",
            "argument": "@ARG",
            "this": "@THIS",
            "that": "@THAT",
            "constant": "",
            "static": "",
            "pointer": "@3",
            "temp": "@5"
        }

    def comment(self, command: str):
        """Escribe en el archivo de salida el comando actual como un comentario."""
        print("// " + command, file=self.file)

    def write_arithmetic(self, command: str):
        """Escribe en el archivo de salida el código de ensamblador aritmético para el comando dado."""
        output = []
        if command in ["add", "sub", "and", "or"]:
            # Pop Stack into D.
            output.append("@SP")
            output.append("AM=M-1")
            output.append("D=M")
            # Access to Stack[-1]
            output.append("@SP")
            output.append("A=M-1")
            # Use the Arithmetic Operator
            output.append(self.symbols[command])
        elif command in ["neg", "not"]:
            # Access to Stack[-1]
            output.append("@SP")
            output.append("A=M-1")
            output.append(self.symbols[command])
        elif command in ["eq", "gt", "lt"]:
            jump_label = "CompLabel" + str(self.label_counter)
            self.label_counter += 1
            # Pop Stack into D.
            output.append("@SP")
            output.append("AM=M-1")
            output.append("D=M")
            # Access to Stack[-1]
            output.append("@SP")
            output.append("A=M-1")
            # Calculate the difference
            output.append("D=M-D")
            # Set the Stack to True in anticipation.
            output.append("M=-1")
            # Load the jump label into A.
            output.append("@" + jump_label)
            # Jump if the statement is True.
            # Else update the Stack to False.
            output.append(self.symbols[command])
            # Set the Stack[-1] to False
            output.append("@SP")
            output.append("A=M-1")
            output.append("M=0")
            # Jump label for the True state.
            output.append("(" + jump_label + ")")
        else:
            raise NameError("Unexpected Arithmetic Command")

        # Add an empty line for debug purposes.
        output.append("")

        # Print assembly commands to the screen.
        for line in output:
            print(line, file=self.file)

    def write_push_pop(self, command: str, segment: str, index: int):
        """Writes to the output file the given push or pop command."""
        # print("write_push_pop:", command, segment, index)
        # segments = constant, local, argument, this, and that.
        output = []
        if command == "C_PUSH":
            if segment == "constant":
                output.append("@" + str(index))
                output.append("D=A")
                output.append("@SP")
                output.append("AM=M+1")
                output.append("A=A-1")
                output.append("M=D")
            elif segment in ["local", "argument", "this", "that", "temp", "pointer"]:
                # Put the index value into D.
                output.append("@" + str(index))
                output.append("D=A")
                # Put the base value into A.
                if segment == "temp" or segment == "pointer":
                    output.append(self.symbols[segment])
                else:
                    # Resolve where the segment refers to.
                    output.append(self.symbols[segment])
                    output.append("A=M")
                # Calculate the source address into A.
                output.append("A=D+A")
                # Put the source value into D.
                output.append("D=M")
                # Put D value into where SP points to.
                output.append("@SP")
                output.append("A=M")
                output.append("M=D")
                # Increment the stack pointer.
                output.append("@SP")
                output.append("M=M+1")
            elif segment == "static":
                # Calculate the source address into A.
                output.append("@" + self.file_name + "." + str(index))
                # Put the source value into D.
                output.append("D=M")
                # Put D value into where SP points to.
                output.append("@SP")
                output.append("A=M")
                output.append("M=D")
                # Increment the stack pointer.
                output.append("@SP")
                output.append("M=M+1")
            else:
                raise NameError("Unexpected Push Segment")
        elif command == "C_POP":
            if segment == "constant":
                # Not a valid command.
                raise NameError("Cannot Pop Constant Segment")
            elif segment in ["local", "argument", "this", "that", "temp", "pointer"]:
                # Put the index value into D.
                output.append("@" + str(index))
                output.append("D=A")
                # Put the base value into A.
                if segment == "temp" or segment == "pointer":
                    output.append(self.symbols[segment])
                else:
                    # Resolve where the segment refers to.
                    output.append(self.symbols[segment])
                    output.append("A=M")
                # Calculate the source address into D.
                output.append("D=D+A")
                # Put D value into R13 for future use.
                output.append("@R13")
                output.append("M=D")
                # Pop stack value into D.
                output.append("@SP")
                output.append("AM=M-1")
                output.append("D=M")
                # Put D value into where R13 points to.
                output.append("@R13")
                output.append("A=M")
                output.append("M=D")
            elif segment == "static":
                # Pop stack value into D.
                output.append("@SP")
                output.append("AM=M-1")
                output.append("D=M")
                # Put the source address into A.
                output.append("@" + self.file_name + "." + str(index))
                # Put D value into static address.
                output.append("M=D")
            else:
                raise NameError("Unexpected Pop Segment")
        else:
            raise NameError("Unexpected Command Type")

        # Añadir una línea vacía con propósitos de depuración.
        output.append("")

        # Imprime comandos de ensamblador en la pantalla.
        for line in output:
            print(line, file=self.file)

    def close(self):
        """Cierra el archivo de salida."""
        self.file.close()


def main():
    """Organiza el análisis y la conversión de código de un archivo de Máquina Virtual."""

    # Comprueba si se proporciona un nombre de archivo.
    if len(sys.argv) != 2 or sys.argv[1][-3:] != ".vm":
        print("Error: Por favor, proporciona un archivo de Máquina Virtual.")
        print("Uso: python " + os.path.basename(__file__) + " [file.vm]")
        return

    # Define los nombres de archivo de entrada y salida.
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[1][:-3] + ".asm"

    # Crea un analizador con el archivo de entrada.
    parser = Parser(input_file_name)

    # Crea un escritor de código con el archivo de salida.
    
    code_writer = CodeWriter(output_file_name)

    # Escanea el archivo de entrada en busca de comandos VM y escribe traducciones en el archivo de salida.
    while parser.hasMoreCommands():
        parser.advance()
        # Escribe el comando actual como un comentario en el archivo de salida con propósitos de depuración.
        code_writer.comment(parser.current_command)
        # Determinar el tipo de comando actual.
        # C_ARITHMETIC, C_PUSH, or C_POP.
        command_type = parser.commandType()
        if command_type == "C_ARITHMETIC":
            # Pasar el comando aritmético al escritor de código.
            code_writer.write_arithmetic(parser.arg1())
        elif command_type in ["C_PUSH", "C_POP"]:
            # Pasa el comando push/pop al escritor de código con sus argumentos.
            argument1 = parser.arg1()
            argument2 = parser.arg2()
            code_writer.write_push_pop(command_type, argument1, argument2)
        else:
            raise NameError("Unsupported Command Type")

    # Cerrar el archivo de salida antes de salir.
    code_writer.close()


if __name__ == "__main__":
    main()
