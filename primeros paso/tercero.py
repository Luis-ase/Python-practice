#################################################
#Ejercicio 021
"""
Escribir un programa que permita ingresar dos números enteros e indicar si el primero es mayor,
menor o igual al segundo.
"""

#################################################
#Ejercicio 022
"""
Escribir un programa que permita ingresar tres números enteros e indicar cual es el mayor.
"""
#################################################
#Ejercicio 023
"""
Escribir un programa que permita ingresar tres números enteros y mostrar el mayor el menor y
 el valor que esta en medio.
Ejemplo: Si se ingresan los números 5, 3 y 7, el programa debe mostrar el número 5 como el menor,
 el número 7 como el mayor y el número 3 como el que esta en medio.
Otra vez se mezclaron las instrucciones, ¿podrías arreglarlas?
numero_uno = int(input("Ingrese el primer número: "))
numero_dos = int(input("Ingrese el segundo número: "))
numero_tres = int(input("Ingrese el tercer número: "))

if medio < menor:
auxiliar = medio
medio = menor
menor = auxiliar

if numero_tres > mayor:
mayor = numero_tres
medio = numero_uno
menor = numero_dos

if numero_dos > mayor:
mayor = numero_dos
medio = numero_uno
menor = numero_tres

mayor = numero_uno
medio = numero_dos
menor = numero_tres

print("El mayor es: ", mayor)
print("El medio es: ", medio)
print("El menor es: ", menor)

"""
#################################################
#Ejercicio 024
"""
Para acceder a cierta atracción, es necesario cumplir con dos requisitos: tener al menos 10 años de edad y medir más de 1,60 metros.
(Ojo, tener en cuenta las palabras: más,al menos y sobre todo la letra y)
Escribir un programa en Python que solicite al usuario su edad y estatura, y que determine si cumple con los requisitos para subir a la atracción. Si cumple con ambos requisitos, el programa debe imprimir "¡Puede acceder!" en la pantalla. Si no cumple con alguno de los requisitos, el programa debe imprimir un mensaje que indique el motivo por el cual no puede subir. Por ejemplo, si no cumple con el requisito de la edad, el programa debe imprimir "Lo siento, eres demasiado joven para acceder." Si no cumple con el requisito de la estatura, el programa debe imprimir "Lo siento, eres demasiado bajo para acceder"
Los conectores lógicos "and" y "or" son operadores booleanos utilizados en programación y en lógica matemática para combinar o unir dos o más expresiones lógicas.

El conector "and" se utiliza para combinar dos o más expresiones lógicas y evaluarlas en conjunto. La expresión completa es verdadera sólo si todas las expresiones individuales son verdaderas. Por ejemplo, la expresión lógica "A and B" será verdadera sólo si tanto A como B son verdaderos. Si alguna de las expresiones es falsa, la expresión completa será falsa.

La tabla de verdad del operador "and" se utiliza en lógica proposicional para determinar el valor de verdad de una proposición compuesta formada por dos proposiciones simples unidas por "and". La tabla de verdad del "and" se construye evaluando todas las posibles combinaciones de valores de verdad de las proposiciones simples, y determinando el valor de verdad de la proposición compuesta para cada combinación.

La tabla de verdad del "and" es la siguiente:

"""
#################################################
#Ejercicio 025
"""
Para acceder a cierta atracción, alcanza con que se cumpla solamente una de las siguientes condiciones: ser mayor de 6 años o medir más de 1,50 metros.
Escribir un programa en Python que solicite al usuario su edad y estatura, y que determine si cumple con los requisitos para subir a la atracción. Si cumple con al menos una de las condiciones, el programa debe imprimir "¡Puede acceder!" en la pantalla. Si no cumple con ninguna de las condiciones, el programa debe imprimir un mensaje que lo indique.
(Ojo, tener en cuenta las palabras: más, mayor y sobre todo la letra o)
El conector "or" se utiliza para combinar dos o más expresiones lógicas y evaluarlas en conjunto. La expresión completa es verdadera si al menos una de las expresiones individuales es verdadera. Por ejemplo, la expresión lógica "A or B" será verdadera si al menos una de las variables A o B es verdadera. Solo si ambas variables son falsas, entonces la expresión completa será falsa.

La tabla de verdad del "or" es la siguiente:
"""
#################################################
#Ejercicio 026
"""
Escribir un programa que permita ingresar la cantidad de invitados a una fiesta y
la cantidad de asientos disponibles en el salon. Debes indicar si alcanzan los asientos, 
Si los asientos no alcanzaran indicar cuántos faltan para que todos los invitados puedan sentarse.
"""
#################################################
#Ejercicio 027
"""
Escribir un programa que permita ingresar una edad 
(entre 1 y 120 años), un género ('F'para mujeres, 'M' para hombres) 
y un nombre. En caso de haber ingresado valores erróneos 
(edad fuera de rango o género inválido), 
informar tal situación indicando el nombre de la persona. 
Si los datos están bien ingresados el programa debe indicar, 
sabiendo que las mujeres se jubilan con 60 años o más y 
los hombres con 65 años o más, si la persona está en edad de jubilarse.
"""
#################################################
#Ejercicio 028
"""
Crear un programa que pida un número de mes (ejemplo 4) y
 escriba el nombre del mes en letras ("abril").
   Verificar que el mes sea válido e informar en caso que no lo sea.
"""

numero = int(input("Elige el mes en base al numero:"))
obj = {
    1:"enero",
    2:"febrero",
    3:"marzo",
    4:"abril",
    5:"mayo",
    6:"junio",
    7:"julio",
    8:"agosto",
    9:"septiembre",
    10:"octubre",
    11:"noviembre",
    12:"diciembre"
}

if obj[numero]:
    print(f"El mes con ese numero es {obj[numero].title()}")
else: 
    print("No existe ese mes")

#################################################
#Ejercicio 029
"""
Escribir un programa que permita Ingresar las notas de los dos parciales
 de un alumno e indicar si promocionó, aprobó o debe recuperar. 
 Si el valor de la nota no esta entre 0 y 10, debe informar un error.
Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
Se debe recuperar cuando al menos una de las dos notas es menor a 4.
"""
#################################################
#Ejercicio 030
"""
Escribir un programa que permita al usuario ingresar dos números enteros. 
La computadora debe indicar si el mayor es divisible por el menor.
(Un número entero a es divisible por un número entero b cuando el resto de la división entre a y b es 0)
"""


