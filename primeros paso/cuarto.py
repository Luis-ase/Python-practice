#################################################
#
"""
Ejercicio 031
Una editorial determina el precio de un libro según la cantidad de páginas que contiene. El costo básico del libro es de  1000,más 35,10 por página con encuadernación rústica. Si el número de páginas supera las 300 la encuadernación debe ser especial, lo que incrementa el costo en  1200.Además,sielnúmerodepáginassobrepasalas600sehacenecesariootroprocedimientodeencuadernaciónqueincrementaelcostoen 880. Desarrollar un programa que calcule el costo de un libro dado el número de páginas.
En Python no existen constantes como tal, pero se utiliza una convención de nomenclatura en mayúsculas para indicar que una variable no debe ser modificada. Esto se conoce como "constante simbólica" o "constante convencional". Para definir una constante convencional, simplemente se define una variable con un nombre en mayúsculas.

Por ejemplo, para el problema anterior, se pueden definir las constantes:

COSTO_BASICO con valor 1000

COSTO_POR_PAGINA con valor 35.10

COSTO_ENC_RUSTICA con valor 1200

COSTO_ENC_ESPECIAL con valor 880.

Es una buena práctica utilizar constantes para almacenar valores fijos en un programa, ya que facilita la lectura del código y su mantenimiento, evita errores por la modificación accidental de valores y permite un fácil ajuste de los valores fijos en caso de ser necesario.
"""
#################################################
#
"""Ejercicio 032
Una remisería requiere un sistema que calcule el precio de un viaje a partir de la cantidad de km que desea recorrer el usuario.
Tiene la siguiente tarifa:
Viaje mínimo $50

Si recorre entre 0 y 10km: $20/km

Si recorre 10km o más: $15/km

Escribir un programa que permita ingresar la cantidad de km que desea recorrer el usuario y muestre el precio del viaje.
"""
#################################################
#
"""
Ejercicio 033
La farmacia Sindical efectúa descuentos a sus afiliados según el importe de la compra con la siguiente escala:
Menor de  5500.0 el descuento es del 4.5%  
- ### Entre 5500.0 y  10000.0 el descuento es del 8%  
- ### Más de 10000.0 el descuento es del 10.5%
Escribir un programa que reciba un importe e informe: el descuento y el precio neto a cobrar, con mensajes aclaratorios.
"""
#################################################
#
"""
Ejercicio 034
Escribir un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo básico y su antigüedad en años. Si es soltero se le incrementa el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si es casado se le incrementa el sueldo en 7% del salario bruto por cada año de antigüedad. También se le realizan los siguientes descuentos:
Jubilación: 11%

Obra Social: 3%

Sindicato: 3%

Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y estado civil (S: Soltero / C: Casado). Se debe informar: (reemplazando los 9 por los valores que correspondan)
Estado Civil: Soltero/Casado Sueldo básico: $ 999.99 Antigüedad: 99 años

Descuentos:

Jubilación - 999,99

Obra Social - 999,99

Sindicato - 999,99

Sueldo Neto 999,99
"""
#################################################
#
"""
Ejercicio 035
Existen dos reglas que identifican dos conjuntos de valores:
a) El número es de un solo dígito.
b) El número es impar.
A partir de estas reglas, escribir un programa que permita ingresar un número entero.
Debe asignar el valor que corresponda a las variables booleanas:
esDeUnSoloDigito
esImpar
estaEnAmbos
noEstaEnNinguno
el valor Verdadero o Falso, según corresponda, para indicar si el valor número ingresado pertenece o no a cada conjunto. Definir un lote de prueba de varios números y probr el algoritmo, escribiendo los resultados.
"""
#################################################
#
"""
Ejercicio 036
Escribir un programa que permita ingresar dos números enteros y la operación a realizar('+', '-', '*', '/'). Debe mostrarse el resultado para la operación ingresada. Considerar que no se puede dividir por cero (en ese caso mostrar el texto 'ERROR').
"""
#################################################
#
"""
Ejercicio 037
Escribir un programa que muestre todos los números enteros del 1 al 5, y luego los mismos números pero en orden inverso.
"""
#################################################
#
"""
Ejercicio 038
Escribir un programa que permita ingresar un número entero n. Debe mostrar los primeros 10 múltiplos de n.
Ejemplo
n = 5

n x 1 = 5
n x 2 = 10
n x 3 = 15
n x 4 = 20
n x 5 = 25
n x 6 = 30
n x 7 = 35
n x 8 = 40
n x 9 = 45
n x 10 = 50
"""
#################################################
#
"""
Ejercicio 039
Escribir un programa para calcular e imprimir la suma de los números comprendidos entre 42 y 176
"""
#################################################
#
"""
Ejercicio 040
Escribir un programa que permita ingresar dos numeros enteros a y b. El programa debe mostrar:
La suma de los numeros pares entre a y b.
El producto de los numeros impares entre a y b.
"""