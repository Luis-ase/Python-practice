#################################################
"""
Ejercicio 051
Escribir un programa que permita al usuario ingresar números hasta que se introduzca un 0.
La computadora debe mostrar el número máximo y el número mínimo.
"""
#################################################
"""
Ejercicio 052
Escribir un programa que permita un programa que permita ingresar la estatura (en metros con decimales) de cada jugador de un equipo de baloncesto. La carga finalizará al ingresar cero. Calcular y mostrar la estatura promedio del equipo.
"""
#################################################
"""
Ejercicio 053
Escribir un programa que permita ingresar nombre y edad de un grupo de personas (para cada una, nombre y edad). La carga termina cuando en el nombre de la persona se ingresa un asterisco ('*'). Mostrar al final cómo se llama la persona más joven.
"""
#################################################
"""
Ejercicio 054
Escribir un programa que permita controlar con validación el ingreso a un sitio web. Teniendo dos constantes con un nombre de usuario ("admin") y una contraseña ("123456"), el programa debe permitir al usuario ingresar sus credenciales. Si las mismas son erróneas, se volverán a pedir hasta un máximo de 3 intentos. Finalmente, la computadora debe mostrar alguno de los siguientes mensajes según sea el caso: "Acceso concedido" o "Se ha bloqueado la cuenta"
"""
#################################################
"""
Ejercicio 055
Escribir un programa que permita para cada cliente que va al banco "Express".
Cada cliente indica su número de documento y aguarda a ser atendido, cuando finaliza la atención del día se ingresa -1 para indicar que no hay más clientes para ser atendidos. El banco desea saber quién fue el primer cliente atendido y quién fue el último.

"""
#################################################
"""
Ejercicio 056
Escribir un programa que permita Leer números que representan edades de un grupo de personas, finalizando la lectura cuando se ingrese el número 999. Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos. Descartar valores que no representan una edad válida. (Se considera válido una edad entre 0 y 100)

"""
#################################################
"""
Ejercicio 057
Escribir un programa que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final. El fin de la carga se determina ingresando un -1 en el legajo.
Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4. Se debe validar que la nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar:
Cantidad de alumnos que aprobaron (nota >= 4).
Cantidad de alumnos que desaprobaron el examen (nota < 4).
Porcentaje de alumnos que están aplazados (nota == 1).
"""
#################################################
"""
Ejercicio 058
Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
Aplica el precio base a la primera docena de unidades.
Aplica un 10% de descuento a todas las unidades entre 13 y 100.
Aplica un 25% de descuento a todas las unidades por encima de las 100.
Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. El cálculo resultante sería:
100 * 12 + 90 * 88 + 75 * 130 = 18870, y el precio promedio será 18870 / 230 = 82,04
Escribir un programa que lea la cantidad solicitada de un producto y su precio base, y muestre el valor total de la venta y el precio promedio por unidad. El fin de carga se determina ingresando -1 como cantidad solicitada.
Al finalizar informar:
a) Cantidad de ventas realizadas total.
b) Cantidad de ventas que se aplicaron un 10% de descuento.
c) Cantidad de ventas que SOLO se aplicó el precio base, no se le realizaron descuentos
"""
#################################################
"""
Ejercicio 059
Escribir un programa para un negocio de venta de granos que desea controlar las ventas realizadas. De cada venta ingresa el importe total y un código que indica la forma de pago. Los códigos puede ser:
C: cheque, 20% de recargo.
E: efectivo, 10% de descuento.
T: con tarjeta, 12% de recargo.
Se debe ingresar una F para finalizar el día de venta y arrojar los siguientes totales.
| Forma de Pago | Total |
| ---------------- | --------- | | Efectivo en Caja |  xxxx.xx||Tarjeta/Crédito|  xxxx.xx |
| Cheques |  xxxx.xx||TotaldeVenta|  xxxx.xx |
| Importe del IVA | $ xxxx.xx |
"""
#################################################
"""
Ejercicio 060
Escribir un programa para calcular el sueldo final a pagar a cada empleado de una empresa. De cada uno se tiene, sueldo básico, antigüedad, cantidad de hijos y estudios superiores (‘S’ o ‘N’). Además, se conocen los porcentajes de aumento del sueldo que dependen de los siguientes factores:
Si el empleado tiene más de 10 años de antigüedad: aumento del 10%
Si el empleado tiene más de 2 hijos: aumento del 10%, si solo tiene uno 5%
Si el empleado posee estudios superiores: aumento del 5%
Luego de ingresar los datos de un empleado se debe preguntar si se desea ingresar otro empleado o no. Se termina la carga cuando no se deseen ingresar más empleados.
Determinar:
a. Por cada empleado: número de empleado, el sueldo básico y el nuevo sueldo.
b. Sueldo nuevo promedio de la empresa.
"""