#Ejercicios del 1 al 10 


# Escribir un programa que permita que el usuario ingrese su nombre. 
#El programa debe emitir una salida con un mensaje de bienvenida que incluya el nombre ingresado.


# nombre= input("ingrese su nombre:")

# print("Bienvenido "+ nombre)


########################################################
#Ejercicio 002

# nombre = input("Ingrese su nombre:")
# edad = input("Ingrese su edad:")

# print("Hola "+nombre+".Tu edad es "+ edad+" años.")

########################################################
#Ejercicio 003
"""
nombre = input("Ingrese su nombre:")
edad = int(input("Ingrese su edad:"))
edad2 = int(input("Ingrese cuantos años pasaran para que llegues a tu prime:"))
suma= edad + edad2
print("Hola ",nombre,".Dentro de ", edad2 ," años tendras", suma," años.")
"""


########################################################
#Ejercicio 004
"""
number1 = int(input("Ingrese un numero:"))
number2 = int(input("Ingrese un numero:"))
number3 = int(input("Ingrese un numero:"))
suma = number1 + number2 + number3
print(number1, " + ", number2, " + ", number3," =",suma )
"""
########################################################
#Ejercicio 005
"""
Escribir un programa que solicite al usuario ingresar dos notas de un alumno. 
El programa debe mostrar por pantalla el promedio de las notas de la siguiente manera: "Notas: [nota1] , [nota2] ==> promedio: [(nota1+nota2)/2]".
Ejemplo: Si el usuario ingresa 7 y 8, el programa debe mostrar por pantalla: "Notas: 7 , 8 ==> promedio: 7.5".
"""

number1 = int(input("Ingrese un numero:"))
number2 = int(input("Ingrese un numero:"))


print("Notas: ",number1 ,",", number2 ,"==> promedio:",(number1 +number2 )/2 ,"." )
