# :collision: Los indestructibles
| Integrantes |
|--- |
| Nelson Andres Barboza Landinez |
| Garbiel Antonio Chavarro Avellaneda | 
| Nery Karolina Aponte Barajas | 
| Carlos Alejandro Amaya Cepeda | 

https://nelson09210921.github.io/Los_indestructibles.github.io/

*[#Practica 1](#Practica_1)

*[Practica 2](#Practica_2)

*[Practica 3](#Practica_3)

##   **Practica 1**

### **Familiarizándonos con la Herramienta Nand2Tetris y reforzando lógica booleana**

El objetivo inicial del proyecto número 1 era generar las funciones necesarias para así dados una serie de datos de entrada se generará el comportamiento de las compuertas lógicas dadas (And, Or, Mux, etc.…). Para empezar, es necesario realizar el código de las compuertas más básicas, como lo son (And, Mux, Not, Or). Una vez realizadas estas funciones se proceden a usarse como base para el desarrollo de compuertas más complejas las cuales necesitaron en diversas ocasiones de la mezcla de las compuertas básicas antes mencionadas. Terminada la digitación del código el programa permitía su verificación por medio de la entrada de unos datos, comparando las salidas cerciorándonos así que la compuerta lógica quedo sin errores en la lógica. Después de esto se adjuntan los archivos con extensión ".hdl" al repositorio de colaboración grupal.

 La práctica inicia con la instalación y reconocimiento de las principales características de Nand2Tetris basados en la guía del proyecto 1, este es el cual es un conjunto de herramientas software, el cual nos ayuda a entender los elementos de arquitectura de computadores basada en el libro The Elements of Computing Systems, Building a Modern Computer from First escrito por Noam Nisan y Simon Schocken los cuales también son los creadores del software mencionado.
 
El objetivo principal de la práctica es reforzar los conocimientos previos acerca de la lógica booleana con el uso de compuertas lógicas, tomando como base la compuerta primitiva NAND.

AND
Esta se desarrollo a partir de la compuerta NAND y la compuerta NOT, pasando los parámetros de la primera y negando la salida.

NOT
Para el desarrollo de esta compuerta le pasamos un único dato de entrada a la compuerta NAND obteniendo el parámetro de entrada negado.

OR
Para esta se aplica un NOT a los dos parámetros de entrada y después una NAND a la salida de estos.

XOR
Se aplica un NOT en las entradas, posterior usamos dos AND con parámetros de entrada una señal directa y la otra negada, luego se realiza un OR a la salida de las AND obteniendo el OR exclusivo.

MUX
Se trabajo en función del selector para la salida del multiplexor, una compuerta NOT a la salida del selector que va a la entrada de una compuerta AND junto con una señal b, la otra AND tiene como entradas la salida directa de selector y la entrada a, la salida de las AND son las entradas de la or y de esta manera queda el multiplexor.

DMUX
se tiene señal de entrada y de datos y dos salidas, la primera salida depende de la entrada negada del multiplexor a una AND junto a la señal directa, la otra salida depende de la entrada del multiplexor sin negar a una AND junto a la señal directa.

NOT16
Es la compuerta NOT pero extendida a 16 bits, es decir 16 entradas.

AND16
Se tomaron parejas de bits (a_i  ,b_i), obteniendo el valor de la compuerta, replicándolo 16 veces.

OR16
Se replica la compuerta OR 16 veces.

MUX16
Se comparan parejas bits (a_i  ,b_i), a través del MUX replicándolo 16 veces.

OR8WAY
Tomamos la compuerta OR usando las dos primeras entradas, y la salida de este se toma como entrada del siguiente junto con la entrada contigua, así sucesivamente se van encadenando hasta obtener la salida de esta compuerta.

MUX4WAY16
Se usan dos multiplexores de 16, cada uno esta conectado a dos entradas, la salida de estos se toma como entrada de otro MUX16 obteniendo así la salida de este.

MUX8WAY16
Se usan 2 compuertas MUX4WAY16 cada una con 4 entradas distintas, obteniendo una salida ara cada una, luego se usa una MUX16 cuyas entradas son las salidas de las anteriores y así obtenemos la salida final.

DMUX4WAY
Cuenta con dos señales multiplexadas negadas y una de datos junto con 4 salidas, las entradas negadas junto a los datos se conectan a unas compuertas AND, la salida de cada una van a 2 DMUX respectivamente, junto con la señal sin negar, a partir de estas se obtienen las cuatro salidas.

DMUX8WAY
Cuenta con tres señales multiplexadas negadas y una de datos junto con 8 salidas, las entradas negadas junto a los datos se conectan a unas compuertas AND, la salida de cada una van a 2 DMUX4WAY respectivamente, junto con la señal sin negar, a partir de estas se obtienen las cuatro salidas.

En conclusión, se pudo comprobar que basados en una sola compuerta primitiva como lo es la NAND se pueden formar las demás compuertas básicas, y la combinación de estas se pueden crear componentes más complejos.

**Bibliografía**
https://www.logicbus.com.mx/compuertas-logicas.php

https://personales.unican.es/manzanom/planantiguo/edigitali/MUXG2.pdf

Gutiérrez, J. M. R., Rudecino, M. S. B., Islas, M. N. O. B., & Gutiérrez, I. R. M. Circuitos Digitales.

##   **Practica 2: proyectos 2 y 3 demominados Lógica Aritmética y Lógica secuencial respectivamente**

El proyecto 2 de nand2tetris consistio en construir una serie de chips que permiten realizar operaciones aritméticas y lógicas con números binarios. El objetivo final es crear una Unidad Aritmética Lógica (ALU), que es el componente central de la CPU de una computadora.

Para hacer este proyecto, necesitas usar el simulador de hardware que se proporciona en el sitio web de nand2tetris1. También necesitamos leer el capítulo 2 del libro, que explica los conceptos y los diseños de los chips que hay que implementar.

Los chips a construir son los siguientes:

HalfAdder: realiza la suma de dos bits y produce un bit de suma y un bit de acarreo.
FullAdder: realiza la suma de tres bits y produce un bit de suma y un bit de acarreo.
Add16: realiza la suma de dos números binarios de 16 bits y produce un número binario de 16 bits.
Inc16: incrementa un número binario de 16 bits en una unidad y produce un número binario de 16 bits.
ALU: realiza una operación aritmética o lógica sobre dos números binarios de 16 bits, según una entrada de control, y produce un número binario de 16 bits y dos indicadores (zero y negative).
Para cada chip, se te proporciona un archivo .hdl con una parte faltante que tienes que completar. También se te proporciona un archivo .tst que indica cómo probar el chip con el simulador, y un archivo .cmp que contiene la salida correcta que debe generar el chip.

paso a paso: 

la construcción de una Unidad Aritmética Lógica (ALU) de 16 bits utilizando el lenguaje de descripción de hardware HDL (Hardware Description Language). Aquí tienes una breve descripción de cómo puedes abordar este proyecto:

La ALU debe tener dos entradas de 16 bits (A y B) y realizar operaciones aritméticas y lógicas en estos números.
Debe tener una entrada de control de 6 bits para seleccionar la operación que realizará.
Debe tener una salida de 16 bits para el resultado.
Debe manejar operaciones como suma, resta, AND, OR, NOT, etc.
Diseña la ALU:

Antes de comenzar a escribir el código en HDL, es importante diseñar la lógica de la ALU en papel o utilizando una herramienta de diseño digital.
Definimos cómo se realizarán las diferentes operaciones y cómo se conectarán las diferentes partes de la ALU.
Escribiendo el código HDL:

Utilizamos un lenguaje de descripción de hardware como VHDL o Verilog para implementar la ALU. 

Implementamos otras operaciones:

Utilizamos una herramienta de simulación de circuitos HDL (como ModelSim) para verificar que la ALU funcione correctamente. Creamos casos de prueba para cada operación y verifica los resultados.
Integramos la ALU en tu proyecto:

Una vez que completamos la implementación y que la ALU funcione correctamente, la integramos en el proyecto general de "Nand to Tetris" según las instrucciones del curso.

El Proyecto 03 de "Nand to Tetris" tuvo como objetivo principal la creación de un simulador de la Unidad Central de Procesamiento (CPU) para la computadora que hemos estado construyendo en proyectos anteriores. A lo largo de este informe, proporcionaré una descripción detallada de la CPU diseñada, el lenguaje ensamblador desarrollado, el código del simulador implementado y los desafíos enfrentados durante el proceso de construcción.

Descripción de la CPU
Arquitectura de la CPU
La CPU diseñada para este proyecto se basa en una arquitectura Von Neumann y cuenta con un conjunto de registros, una unidad de control y una ALU (Unidad Lógico-Aritmética). Los registros incluyen el Registro de Instrucciones (IR), el Registro de Datos A (A), el Registro de Datos B (B), el Registro de Resultados (R), y otros registros específicos del proyecto.

Conjunto de Instrucciones
La CPU admite un conjunto de instrucciones específico definido en el lenguaje ensamblador diseñado para esta computadora. Las instrucciones incluyen operaciones aritméticas, de transferencia de datos y de control de flujo.

Lenguaje Ensamblador
Diseño del Lenguaje Ensamblador
Se creó un lenguaje ensamblador específico para esta arquitectura de CPU. El lenguaje ensamblador consta de un conjunto de mnemónicos y una sintaxis que refleja las operaciones admitidas por la CPU. Esto permitió escribir programas en ensamblador que la CPU podía ejecutar.

Implementación del Simulador
El simulador de la CPU se implementó en el lenguaje de programación Java. El código del simulador es responsable de cargar programas escritos en lenguaje ensamblador, decodificar y ejecutar las instrucciones, y mostrar el estado de la CPU en cada paso.

## **Practica 3**

La practica 3 consistió en el desarrollaron los proyectos 4 y 5 de nand2tetris.

Los objetivos del proyecto 4 Lenguaje de máquina, fueron

•	Tener una experiencia práctica en programación de bajo nivel en lenguaje de máquina.

•	Familiarizarnos con el conjunto de instrucciones Hack antes de construir la computadora Hack en el proyecto 5.

•	Conocer el proceso de ensamblaje antes de construir un ensamblador en el proyecto 6. 

Se uso la plataforma Hack para la creación de un programa que desarrolle operaciones de multiplicación en el lenguaje de máquina, teniendo en cuenta que esta no es una operación primitiva de la plataforma mientras que la suma si lo es, por tanto, se debe implementar usando la suma.

La finalidad de este proyecto fue almacenar el producto de dos números, RAM 0 y RAM 1 en el espacio de memoria R2, para completar el proyecto se editaron los archivos Mult.asm y Fill.asm usando el ensamblador Hack y cargándolo posteriormente los archivos Mult.hack y Fill.hack creados por el ensamblador en el emulador CPU.

Mult.asm: este programa consta con tres memorias RAM R0, R1 y R2, donde los dos primeros es donde se almacenan los nueros a multiplicar y R2 es el resultado de la multiplicación, estos números se multiplican realizando sumas repetitivas en un ciclo.

Fill.asm: este programa es un script que ejecuta un bucle infinito para verificar la captura de datos del teclado, si fue presionada una tecla la pantalla se torna de color negro de lo contrario se ilumina.

Pr último, ¿Por qué el lenguaje de máquina es importante para definir la arquitectura computacional? 
El lenguaje de máquina es importante para definir la arquitectura computacional porque es el lenguaje que la CPU puede entender y ejecutar directamente. La arquitectura computacional se refiere al diseño y la organización de los componentes de hardware y software de un sistema informático, como la CPU, la memoria, los buses, los dispositivos de entrada y salida, etc. El lenguaje de máquina determina las instrucciones que la CPU puede realizar, así como el formato y el significado de los datos que puede procesar. Cada arquitectura computacional tiene su propio lenguaje de máquina, que es específico y adaptado a sus características y capacidades. El lenguaje de máquina es el nivel más bajo de abstracción en la programación, lo que significa que es el más cercano al hardware y el más difícil de entender y escribir para los humanos. Por eso, se han desarrollado otros lenguajes de programación de más alto nivel, que son más fáciles de leer y escribir, pero que requieren ser traducidos al lenguaje de máquina para que la CPU pueda ejecutarlos. Estos lenguajes de programación se pueden clasificar en distintos niveles según su grado de abstracción y su similitud con el lenguaje natural. Algunos ejemplos son el ensamblador, el C, el Java, el Python, etc.


## :notes: Trabajo Final:



