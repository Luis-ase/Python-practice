#################################################
"""
Ejercicio 061
Escribir un programa que permita ingresar un número entero positivo y mostrar su factorial. El factorial de un número es el producto de todos los números enteros desde 1 hasta el número ingresado. Por ejemplo, el factorial de 5 es 1 * 2 * 3 * 4 * 5 = 120.
"""
#################################################
"""
Ejercicio 062
Un entrenador le ha propuesto a un atleta recorrer una ruta de cinco kilómetros durante 10 días para determinar si es apto para la prueba de 5 kilómetros que se desarrollará en el Parque. No se sabe si está apto y para eso nos piden que hagamos el siguiente programa.
Nos ingresan por cada día de entrenamiento tiempo de la prueba en minutos (entero mayor que 0 y menor a 100)
Para considerarlo apto debe cumplir las siguientes condiciones:
Que en ninguna de las pruebas haga un tiempo mayor a 20 minutos.
Que al menos en una de las pruebas realice un tiempo menor de 15 minutos.
Que su promedio sea menor o igual a 18 minutos.
Se pide:
Diseñar un algoritmo para registrar los datos y decidir si es apto para la competencia.
Sólo en caso de estar apto, informar el promedio y el número de día en el que realizó el menor tiempo
"""
#################################################
"""
Ejercicio 063
Escribir un programa para registrar y obtener información sobre los viajes diarios de un conductor de Uber.
Cada vez que comienza un viaje se debe ingresar la distancia recorrida, indicando si el viaje fue corto (‘C’), mediano (‘M’), largo (‘L’) o si es el fin de los datos (‘Z’).
El día finaliza cuando se llega a los 30 viajes o cuando se ingresa distancia ‘Z’ (fin de los datos).
Por cada viaje se debe ingresar la siguiente información:
Cantidad de pasajeros (mayor a 0 y menor a 4).
Importe a cobrar, incluyendo la el costo básico ($180).
Por cada pasajero de ese viaje se debe ingresar:
Nombre.
Edad (mayor a 18 y menor a 120 años).
Se desea saber, para cada viaje, cuál es la persona más grande y su nombre.
Al finalizar el día de trabajo, el programa debe informar:
Cantidad de viajes por cada categoría (‘C’, ‘M’, ‘L’).
Recaudación total.
Valor promedio del viaje.
Porcentaje de viajes cortos.
Todos los datos ingresados deben ser validados.
"""
#################################################
"""
Ejercicio 064
Un animal en rehabilitación después de una cirugía requiere ser alimentado y monitoreado en un zoológico. Se alimenta al animal 3 veces al día y se le da de comer hasta que ya no tenga ganas de comer.
Por cada tanda de comida, se debe ingresar la cantidad de alimento en kg (número entero) que se le dio y se le debe preguntar al animal si quiere seguir comiendo ('S', 'N').
Se desea conocer:
Cuál de las 3 comidas fue la que el animal comió más cantidad de alimento y cuánto fue esa cantidad.
El total en kg de alimento recibido.
Promedio de alimento por tanda.

"""
#################################################
"""
Ejercicio 065
Una cadena de comida rápida solicita el desarrollo de una aplicación para sus terminales de autoservicio que permita a los clientes armar su propio menú. Los clientes pueden elegir entre diferentes opciones de combos o pedir por separado la comida, bebida y postre.
Al iniciar la aplicación, se debe mostrar el siguiente menú de opciones:
1) Combo 1: Hamburguesa, papas fritas y gaseosa - 1550
2) Combo 2: Hamburguesa con queso, papas fritas y gaseosa - 1650
3) Hamburguesa sola - 1300
4) Hamburguesa con queso - 1400
5) Gaseosa - 700
6) Postre - 600
7) Agregar aderezo - 100
8) Terminar
Luego de seleccionar cada ítem, se debe mostrar el subtotal para que el cliente pueda decidir si desea agregar más productos a su pedido antes de terminar.
El valor mínimo del pedido debe ser de $1550. Si el cliente elige un combo, se debe sumar el importe total al subtotal. Si el cliente selecciona opciones 3 a 7, se le debe preguntar la cantidad deseada y calcular el valor total antes de sumarlo al subtotal.
Al finalizar el pedido, se debe mostrar el monto total a pagar, el ítem más caro y, si no se han seleccionado productos, mostrar un mensaje que diga "Pedido cancelado".
"""
#################################################
"""
Ejercicio 066a
La biblioteca de la ciudad necesita organizar y hacer un recuento de los libros que tiene en sus 5 estantes. Para cada uno de los 5 estantes, se deben ingresar los libros, y para cada libro, se debe ingresar su nombre (usando 'FIN' si no hay más libros para ese estante), género (usando 'I' para Infantil, 'N' para Novela, o 'H' para Historia), y cantidad de páginas (mayor a 0). Una vez que se han ingresado los datos de 1 estante, se debe mostrar por pantalla el nombre del libro con la mayor cantidad de páginas y su cantidad correspondiente. Al finalizar el ingreso de datos de todos los estantes, se deben mostrar la cantidad de libros por género y el promedio de libros por estante.
"""
#################################################
"""
Ejercicio 066b
La biblioteca de la ciudad necesita organizar y hacer un recuento de los libros que tiene en sus estantes. Para cada uno de los estantes (usando 'F' para indicar el fin de los estantes), se deben ingresar 15 libros, y para cada libro, se debe ingresar su nombre, género (usando 'I' para Infantil, 'N' para Novela, o 'H' para Historia), y cantidad de páginas (mayor a 0). Una vez que se han ingresado los datos de 1 estante, se debe mostrar por pantalla el nombre del libro con la mayor cantidad de páginas y su cantidad correspondiente. Al finalizar el ingreso de datos de todos los estantes, se deben mostrar la cantidad de libros por género.
"""
#################################################
"""
Ejercicio 066c
La biblioteca de la ciudad necesita organizar y hacer un recuento de los libros que tiene en sus estantes. Para cada uno de los estantes (usando 'F' para indicar el fin del estante), se deben ingresar los libros, y para cada libro, se debe ingresar su nombre (usando 'FIN' si no hay más libros para ese estante), género (usando 'I' para Infantil, 'N' para Novela, o 'H' para Historia), y cantidad de páginas (mayor a 0). Una vez que se han ingresado los datos de 1 estante, se debe mostrar por pantalla el nombre del libro con la mayor cantidad de páginas y su cantidad correspondiente. Al finalizar el ingreso de datos de todos los estantes, se deben mostrar la cantidad de libros por género y el promedio de libros por estante.
"""
#################################################
"""
Ejercicio 066d
La biblioteca de la ciudad necesita organizar y hacer un recuento de los libros que tiene en sus estantes. Para cada uno de los 5 estantes, se le pide al usuario que ingrese la cantidad de libros que tendrá ese estante. Para cada libro, se debe ingresar su nombre, género (usando 'I' para Infantil, 'N' para Novela, o 'H' para Historia), y cantidad de páginas (mayor a 0). Una vez que se han ingresado los datos de 1 estante, se debe mostrar por pantalla el nombre del libro con la mayor cantidad de páginas y su cantidad correspondiente. Al finalizar el ingreso de datos de todos los estantes, se deben mostrar la cantidad de libros por género.
"""
#################################################
"""

"""