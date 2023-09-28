// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.
@k      // k inicia como 0
M=0
@c      // c inicia como 0
M=0
(LOOP)
    @c      // si (c-R1)=0 va a END
    D=M
    @1
    D=D-M
    @END
    D;JEQ
    @0      // k += R0
    D=M
    @k
    M=M+D
    @c
    M=M+1   // c++
    @LOOP   // va al ciclo
    0;JMP
(END)
    @k      // Ajusta R2 = k
    D=M
    @2
    M=D