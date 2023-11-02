# :collision: Los indestructibles
| Integrantes |
|--- |
| Nelson Andres Barboza Landinez |
| Garbiel Antonio Chavarro Avellaneda | 
| Nery Karolina Aponte Barajas | 
| Carlos Alejandro Amaya Cepeda | 

https://nelson09210921.github.io/Los_indestructibles.github.io/

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

##   **Practica 2**

### ** Lógica Aritmética y Lógica secuencial respectivamente**

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
### **Lenguaje de máquina y arquitectura computacional**

La practica 3 consistió en el desarrollaron los proyectos 4 y 5 de nand2tetris.

Los objetivos del proyecto 4 Lenguaje de máquina, fueron

•	Tener una experiencia práctica en programación de bajo nivel en lenguaje de máquina.

•	Familiarizarnos con el conjunto de instrucciones Hack antes de construir la computadora Hack en el proyecto 5.

•	Conocer el proceso de ensamblaje antes de construir un ensamblador en el proyecto 6. 

Se uso la plataforma Hack para la creación de un programa que desarrolle operaciones de multiplicación en el lenguaje de máquina, teniendo en cuenta que esta no es una operación primitiva de la plataforma mientras que la suma si lo es, por tanto, se debe implementar usando la suma.

La finalidad de este proyecto fue almacenar el producto de dos números, RAM 0 y RAM 1 en el espacio de memoria R2, para completar el proyecto se editaron los archivos Mult.asm y Fill.asm usando el ensamblador Hack y cargándolo posteriormente los archivos Mult.hack y Fill.hack creados por el ensamblador en el emulador CPU.

Mult.asm: este programa consta con tres memorias RAM R0, R1 y R2, donde los dos primeros es donde se almacenan los nueros a multiplicar y R2 es el resultado de la multiplicación, estos números se multiplican realizando sumas repetitivas en un ciclo.

Fill.asm: este programa es un script que ejecuta un bucle infinito para verificar la captura de datos del teclado, si fue presionada una tecla la pantalla se torna de color negro de lo contrario se ilumina.

El proyecto 5 arquitectura computacional, se desarrollo de la siguiente manera

- Leer el capítulo 5 del libro "The Elements of Computing Systems" que explica los conceptos teóricos y las especificaciones de los chips que se deben construir¹.
- Incluir las herramientas de simulación, las pruebas y los scripts necesarios para verificar el funcionamiento de los chips.
- Usa el simulador de hardware para implementar la ALU siguiendo la especificación dada en el libro y en el archivo ALU.hdl. La ALU debe ser capaz de realizar 18 operaciones diferentes sobre dos entradas de 16 bits cada una y producir una salida de 16 bits y dos bits de estado.
- Usa el simulador de hardware para implementar la memoria RAM siguiendo la especificación dada en el libro y en el archivo RAM.hdl. La RAM debe ser capaz de almacenar y recuperar datos de 16 bits en una dirección específica de 15 bits¹.
- Usa el simulador de hardware para implementar el programa contador siguiendo la especificación dada en el libro y en el archivo PC.hdl. El PC debe ser capaz de incrementar, cargar o reiniciar su valor según las señales de control que recibe¹.
- Usa el simulador de hardware para implementar el chip CPU siguiendo la especificación dada en el libro y en el archivo CPU.hdl. El CPU debe ser capaz de ejecutar instrucciones de máquina escritas en lenguaje ensamblador, usando la ALU, la RAM y el PC como componentes internos.
- Verifica que los chips funcionan correctamente usando las pruebas y los scripts proporcionados por el software del curso.

Introducción

El diseño e implementación de la Unidad Aritmético-Lógica (ALU), que es un componente fundamental de un computador moderno. La ALU es el chip que realiza las operaciones aritméticas y lógicas sobre los datos que se procesan en el sistema. El código HDL para la ALU se basa en las especificaciones dadas en el libro "The Elements of Computing Systems", que forma parte del curso Nand2Tetris.

Metodología

Para implementar la ALU, se usó el simulador de hardware provisto por el software del curso, que permite crear y probar chips usando un lenguaje de descripción de hardware (HDL). El HDL es un lenguaje que permite especificar la estructura y el comportamiento de un circuito electrónico usando puertas lógicas como elementos básicos. El simulador de hardware permite visualizar el funcionamiento de los chips y verificar que cumplen con las pruebas y los scripts proporcionados por el software del curso.

El código HDL para la ALU se puede dividir en las siguientes partes:

- La declaración del chip ALU, que indica las entradas y salidas que tiene. La ALU recibe dos entradas de 16 bits cada una (x e y), que son los datos sobre los que se va a operar. También recibe una entrada de 6 bits (zx, nx, zy, ny, f, no), que son las señales de control que determinan qué operación se va a realizar. La ALU produce una salida de 16 bits (out), que es el resultado de la operación. También produce dos bits de estado (zr y ng), que indican si la salida es cero o negativa.
- La definición de los componentes internos que usa la ALU, que son otros chips que se han construido previamente en el curso. Estos son: Not16, que aplica la operación NOT a una entrada de 16 bits; Mux16, que selecciona entre dos entradas de 16 bits según una señal de control; And16, que aplica la operación AND a dos entradas de 16 bits; Add16, que aplica la operación ADD a dos entradas de 16 bits; Or8Way, que aplica la operación OR a una entrada de 8 bits; Or, que aplica la operación OR a dos entradas de 1 bit; y And, que aplica la operación AND a dos entradas de 1 bit.
- La implementación de la lógica de la ALU, que consiste en conectar los componentes internos de forma adecuada para realizar la operación deseada. La lógica se puede explicar de la siguiente manera:

    - Primero, se procesan las entradas x e y según las señales de control zx, nx, zy y ny. Estas señales permiten modificar las entradas antes de operar con ellas. Por ejemplo, si zx es 1, se reemplaza x por una entrada de 16 ceros; si nx es 1, se aplica la operación NOT a x; si zy es 1, se reemplaza y por una entrada de 16 ceros; y si ny es 1, se aplica la operación NOT a y. Para lograr esto, se usan los chips Not16 y Mux16. El resultado de este procesamiento se almacena en las variables x1 e y1.
    - Segundo, se opera con las entradas procesadas x1 e y1 según la señal de control f. Esta señal permite elegir entre dos posibles operaciones: AND o ADD. Si f es 0, se aplica la operación AND a x1 e y1; si f es 1, se aplica la operación ADD a x1 e y1. Para lograr esto, se usan los chips And16, Add16 y Mux16. El resultado de esta operación se almacena en la variable fOut.
    - Tercero, se procesa la salida fOut según la señal de control no. Esta señal permite modificar la salida después de operar con ella. Si no es 1, se aplica la operación NOT a fOut; si no es 0, se deja igual a fOut. Para lograr esto, se usan los chips Not16 y Mux16. El resultado de este procesamiento se asigna a la salida out.
    - Cuarto, se verifica el valor de la salida out y se asignan los bits de estado zr y ng. Estos bits indican si la salida es cero o negativa. Para verificar si la salida es cero, se usa el chip Or8Way para aplicar la operación OR a cada mitad de la salida (8 bits cada una) y luego se usa el chip Or para aplicar la operación OR al resultado. Si el resultado final es 0, significa que todos los bits de la salida son 0; si el resultado final es 1, significa que al menos un bit de la salida es 1. Luego se usa el chip Not para invertir el resultado final y asignarlo al bit zr. Para verificar si la salida es negativa, se usa el chip And para aplicar la operación AND entre el valor true y el bit más significativo de la salida (el bit 15). Si el resultado es 1, significa que el bit más significativo es 1, lo que indica un número negativo en complemento a dos; si el resultado es 0, significa que el bit más significativo es 0, lo que indica un número positivo o cero en complemento a dos. El resultado se asigna al bit ng.

Conclusiones 

En este proyecto se logró implementar la arquitectura de un computador moderno usando solo elementos lógicos básicos. Se construyó la ALU, la RAM, el PC y el CPU que permiten ejecutar instrucciones de máquina escritas en lenguaje ensamblador. Se aprendió sobre los principios y los componentes fundamentales de un sistema computacional y se desarrollaron habilidades de diseño e implementación de hardware.

El código HDL para la ALU, que es un chip que realiza las operaciones aritméticas y lógicas sobre los datos que se procesan en un computador moderno. Se explicó el diseño e implementación de la ALU usando elementos lógicos básicos como puertas NAND. Se mostró cómo la ALU recibe dos entradas de 16 bits cada una (x e y) y una entrada de 6 bits (zx, nx, zy, ny, f, no) que determinan la operación a realizar. Se mostró cómo la ALU produce una salida de 16 bits (out) y dos bits de estado (zr y ng) que indican si la salida es cero o negativa.

Pr último, ¿Por qué el lenguaje de máquina es importante para definir la arquitectura computacional? 
El lenguaje de máquina es importante para definir la arquitectura computacional porque es el lenguaje que la CPU puede entender y ejecutar directamente. La arquitectura computacional se refiere al diseño y la organización de los componentes de hardware y software de un sistema informático, como la CPU, la memoria, los buses, los dispositivos de entrada y salida, etc. El lenguaje de máquina determina las instrucciones que la CPU puede realizar, así como el formato y el significado de los datos que puede procesar. Cada arquitectura computacional tiene su propio lenguaje de máquina, que es específico y adaptado a sus características y capacidades. El lenguaje de máquina es el nivel más bajo de abstracción en la programación, lo que significa que es el más cercano al hardware y el más difícil de entender y escribir para los humanos. Por eso, se han desarrollado otros lenguajes de programación de más alto nivel, que son más fáciles de leer y escribir, pero que requieren ser traducidos al lenguaje de máquina para que la CPU pueda ejecutarlos. Estos lenguajes de programación se pueden clasificar en distintos niveles según su grado de abstracción y su similitud con el lenguaje natural. Algunos ejemplos son el ensamblador, el C, el Java, el Python, etc.

Referencias

"Nisan, N., & Schocken, S. (2005). The elements of computing systems: building a modern computer from first principles. MIT press."

## Práctica 4
### **Asambler**

Para el desarrollo de la practica 4 nos basamos en el proyecto 6 de nan2tetris, donde el objetivo principal es construir un ensamblador que traduzca programas escritos en lenguaje ensamblador Hack (un lenguaje de bajo nivel diseñado para el curso) en código binario que pueda ser ejecutado en la arquitectura Hack.

ASS.asm es la suma de dos constantes poniendo el resultado en R0.

Max.asm Calcula el máximo de dos números los cuales van a ser ingresados en R0 y R1 poniendo el resultado en R2.

Rect.asm dibuja un rectángulo en la parte superior izquierda de la pantalla con dimensiones de 16px de ancho y R0px de alto.

Pong.asm juego simbólico sin etiquetas diseñado por un ensamblador usando lenguaje Hack y el compilador se encarga de traducirlo al ensamblador correspondiente, este juego consiste el rebote de una pelota de lado a lado donde el usuario debe tocarla con una barra y no dejarla caer , cada que la pelota golpea la barra esta se encoge haciendo mas emocionante el juego, el juego termina dejando caer la pelota u oprimiendo esc, este tiende a ser lento al ser ejecutado por un emulador de CPU.

¿Cuál es la principal limitante que observan?

El ensamblador es una herramienta esencial en el desarrollo de software a bajo nivel dado que este se ubica en una posición extremadamente baja en la jerarquía de lenguajes de programación, es crucial considerar las restricciones asociadas con su empleo. Estas incluyen la necesidad de comprender y aplicar con precisión las reglas gramaticales del lenguaje Hack, así como la conversión de estructuras de alto nivel a instrucciones de bajo nivel en la máquina virtual de UBM, lo que requiere una comprensión profunda de la semántica del lenguaje y las operaciones de la máquina subyacente. Aunque el ensamblador posee un gran poder para la programación a nivel de sistema y puede optimizar el rendimiento en plataformas específicas, su carencia de portabilidad y falta de abstracción hacen que sea menos adecuado para aplicaciones de software que necesitan ejecutarse en diversos entornos o que demandan un desarrollo rápido y un mantenimiento sencillo.


## Práctica 5
### **Maquina virtual, Aritmética de pila y Control de programa**

Para el desarrollo de la practica 5 nos basamos en loa proyectos 7 y 8 de nan2tetris, los cuales consisten en la construcción de una máquina virtual (VM) y su traductor, Aritmética de pila y Control de programa respectivamente.

El objetivo principal  es construir un traductor de Máquina Virtual (VM) a Hack. Este traductor debe ajustarse a la Especificación VM, Parte I (sección 7.2 del libro) y al Mapeo Estándar VM-on-Hack, Parte I (sección 7.3.1 del libro).

Funcionamiento

El traductor toma como entrada un archivo con código en lenguaje VM y genera un archivo de salida con el código equivalente en lenguaje Hack. El archivo de salida se denomina fileName.asm y se almacena en el mismo directorio que el archivo de entrada.
Se divide en dos etapas principales:

Etapa I: Manejo de comandos aritméticos de pila
La Etapa I del Proyecto 07 de Nand2Tetris se centra en el manejo de comandos aritméticos de pila. En esta etapa, el traductor VM debe implementar los nueve comandos aritméticos/lógicos del lenguaje VM, así como el comando VM push constant x.
Comandos Aritméticos/Lógicos
Los nueve comandos aritméticos/lógicos que debes implementar son: add, sub, neg, eq, gt, lt, and, or y not. Cada uno de estos comandos opera en los valores en la parte superior de la pila.
Por ejemplo, el comando add toma los dos valores superiores de la pila, los suma y empuja el resultado a la pila. El comando neg toma el valor superior de la pila, lo niega (es decir, lo multiplica por -1) y empuja el resultado a la pila.
Comando VM push constant x
El comando VM push constant x empuja una constante x a la pila. El código VM contiene la línea push constant 7, tu traductor VM debe generar código Hack que empuje el número 7 a la pila.

Implementación

Para implementar estos comandos, el traductor VM debe generar código Hack que realice las operaciones correspondientes en la pila. Esto implica manipular los registros y la memoria del lenguaje ensamblador Hack para replicar el comportamiento de una máquina virtual basada en una pila.

Etapa II: Implementación de comandos de operación de segmento de memoria

Segmentos de Memoria

Los segmentos de memoria en la Máquina Virtual (VM) incluyen local, argument, this, that, constant, static, pointer, y temp. Cada uno de estos segmentos tiene un propósito específico y una ubicación específica en la memoria.
Por ejemplo, el segmento local se utiliza para almacenar variables locales en una función, mientras que el segmento argument se utiliza para pasar argumentos a una función. El segmento constant se utiliza para empujar constantes a la pila, y el segmento static se utiliza para almacenar variables estáticas que persisten entre las llamadas a las funciones.
Comandos push y pop
Los comandos push y pop se utilizan para manipular los datos en los segmentos de memoria. El comando push segment index empuja el valor del segmento especificado en el índice especificado a la parte superior de la pila. Por otro lado, el comando pop segment index saca el valor superior de la pila y lo almacena en el segmento especificado en el índice especificado.
Por ejemplo, el comando VM push local 0 empuja el valor del primer índice del segmento local a la pila. El comando VM pop argument 1 saca el valor superior de la pila y lo almacena en el segundo índice del segmento argument.

Implementación

Para implementar estos comandos, el traductor VM debe generar código Hack que realice las operaciones correspondientes en los segmentos de memoria. Esto implica manipular los registros y la memoria del lenguaje ensamblador Hack para replicar el comportamiento de una máquina virtual basada en una pila.
Resultados 

Al finalizar el proyecto, el traductor es capaz de convertir correctamente el código en lenguaje VM a código en lenguaje Hack. Esto permite ejecutar programas escritos en lenguaje VM en la plataforma Hack.

Teniendo en cuenta el marco de estas dos prácticas que son las máquinas virtuales. ¿Cuál cree que es el futuro de las máquinas virtuales?
El futuro de las máquinas virtuales es prometedor y continuará evolucionando en varias direcciones. Las prácticas 7 y 8 del curso de nand2tetris brindan una comprensión fundamental de cómo funcionan las máquinas virtuales a un nivel más básico. Sin embargo, el panorama actual de las máquinas virtuales va mucho más allá, este apunta hacia apunta hacia la continua mejora de la eficiencia, el rendimiento, la seguridad y la integración con tecnologías emergentes, como contenedores y la nube. Es probable que veamos una evolución constante en la forma en que se utilizan y se integran en los sistemas informáticos, con un enfoque en la optimización y la flexibilidad.




## :notes: Trabajo Final:



