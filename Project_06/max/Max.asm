   @R0
   D=M              // D = primer numero
   @R1
   D=D-M            // D = primer numero - segundo numero
   @OUTPUT_FIRST
   D;JGT            // if D>0 (el primero es mayor) va a la primera salida
   @R1
   D=M              // D = segundo nombre
   @OUTPUT_D
   0;JMP            // va a las salida d
(OUTPUT_FIRST)
   @R0             
   D=M              // D = Primer numero
(OUTPUT_D)
   @R2
   M=D              // M[2] = D (numero mayor)
(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP            // Ciclo infinito