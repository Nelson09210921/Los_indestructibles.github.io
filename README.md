# :collision: Los indestructibles
| Integrantes |
|--- |
| Nelson Andres Barboza Landinez |
| Garbiel Antonio Chavarro Avellaneda | 
| Nery Karolina Aponte Barajas | 
| Carlos Alejandro Amaya Cepeda | 


## :speech_balloon: Practicas

##   **Proyecto 1:**
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


## :notes: Trabajo Final:



