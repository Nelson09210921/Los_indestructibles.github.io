// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// Un programa simple que llena la pantalla
//@counter
//M=-1
//(LOOP)
//@counter
//M=M+1
//D=M
//@SCREEN
//A=A+D
//M=-1
//@8192
//D=D-A
//@LOOP
//D;JNE
//... Se llena la pnatalla con negro pero para con un mensaje de error

(BEGIN)      // Inicia el ciclo

@KBD
D=M
@BLACK
D;JNE
@WHITE
D;JEQ

(BLACK)
@counter     // Pinta la pantalla
M=-1
(LOOP)
@counter
M=M+1
D=M
@SCREEN
A=A+D
M=-1
@8191
D=D-A
@LOOP
D;JNE       // Acaba el proceso de llenar la pantalla
@BEGIN
0;JMP

(WHITE)
@counterwhite     // Pinta nuevamente la pantalla pero ahora de blanco
M=-1
(LOOPWHITE)
@counterwhite
M=M+1
D=M
@SCREEN
A=A+D
M=0
@8191
D=D-A
@LOOPWHITE
D;JNE       // Finaliza 

@BEGIN      // Se hace un salto al inicio
0;JMP