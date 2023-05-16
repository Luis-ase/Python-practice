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

# number1 = int(input("Ingrese un numero:"))
# number2 = int(input("Ingrese un numero:"))


# print("Notas: ",number1 ,",", number2 ,"==> promedio:",(number1 +number2 )/2 ,"." )
########################################################
#Ejercicio 006
"""
Escribir un programa que solicite al usuario ingresar tres notas de un alumno.
El programa debe mostrar por pantalla las notas separadas por comas en un renglón y el promedio de las notas en el siguiente renglon.
ejemplo
Ingrese la nota 1: 7
Ingrese la nota 2: 8
Ingrese la nota 3: 9
Notas: 7, 8, 9
Promedio: 8.0
"""

# nota1 = int(input("Ingrese un nota 1:"))
# nota2 = int(input("Ingrese un nota 2:"))
# nota3 = int(input("Ingrese un nota 3:"))
# print("Notas: ", nota1,nota2,nota3,)
# print("Promedio",(nota1 + nota2 +nota3)/3)
########################################################
#Ejercicio 007
"""
Escribir un programa que permita ingresar un número entero. Debe mostrarse el número ingresado:
a. Multiplicado por 10. (utilizar el operador *)
b. Dividido por 10. (utilizar el operador /)
c. Elevado al cuadrado. (utilizar el operador **)
Cada resultado debe mostrarse en una línea distinta.
Ejemplo de ejecución:

Ingrese un número entero: 5
5 * 10 = 50
5 / 10 = 0.5
5 ** 2 = 25
"""
# numero_a_operar = int(input("Ingrese un numero entero: "))

# print(numero_a_operar,"*",10,"=",(numero_a_operar * 10))
# print(numero_a_operar,"*",10,"=",(numero_a_operar / 10))
# print(numero_a_operar,"*",2,"=",(numero_a_operar ** 2))

########################################################

#Ejercicio 008
"""
Escribir un programa que permita ingresar el valor monetario de una hora de trabajo y la cantidad de horas trabajadas por día, 
para calcular el salario semanal de un trabajador que trabaja todos los días hábiles y la mitad de las horas del día hábil los 
sábados, suponiendo que todas las horas tienen el mismo valor."
Como pensarlo:
1- Pedir al usuario que ingrese el valor monetario de una hora de trabajo y almacenarlo en una variable valor_hora.

2- Pedir al usuario que ingrese la cantidad de horas trabajadas por día por el trabajador y almacenarla en una variable horas_trabajadas_por_dia.

3- Calcular el salario diario del trabajador multiplicando valor_hora por horas_trabajadas_por_dia.

4- Calcular el salario semanal del trabajador multiplicando el salario diario por la cantidad de días hábiles de la semana.
 Para esto, puedes utilizar la constante dias_habiles definida como 5.

5- Calcular la cantidad de horas trabajadas por el trabajador el sábado, que es la mitad de la cantidad de horas trabajadas por día hábil.
 Para esto, se puede utilizar la vaiable horas_sabado definida como horas_trabajadas_por_dia / 2.

6- Calcular el salario del trabajador por las horas trabajadas el sábado multiplicando valor_hora por horas_sabado.

7- Sumar el salario semanal con el salario del sábado para obtener el salario total semanal del trabajador.

8- Mostrar el resultado del salario semanal en la pantalla.
"""

# DIAS_HABILES = 5

# valor_de_la_hora= float(input("Valor de la hora:"))
# horas_por_dia = float(input("Cuantas horas trabajas por dia capo:"))
# salario_diaro= valor_de_la_hora * horas_por_dia
# salario_semanal= salario_diaro * DIAS_HABILES
# horas_sabado =horas_por_dia /2
# salario_sabado = horas_sabado * valor_de_la_hora
# salario_total= salario_sabado + salario_semanal
# print(salario_total)
########################################################

#Ejercicio 009
"""
Escribir un programa que permita ingresar valores del mismo tipo para las variables num1 y num2. Una vez cargadas, mostrar ambas variables por pantalla, intercambiá sus valores (que lo cargado en num1 quede en num2, y viceversa) y volvé a mostrarlas actualizadas.
Como pensarlo:
1- Pedir al usuario que ingrese un valor para la variable num1.

2- Pedir al usuario que ingrese un valor para la variable num2.

3- Mostrar por pantalla el valor de las variables num1 y num2.

4- Intercambiar los valores de las variables num1 y num2.

5- Mostrar por pantalla el valor de las variables num1 y num2.

Otra forma de resolverlo:
a=10
b=20
print(a,b)
a = a + b;
b = a - b;
a = a - b;
print(a,b)
"""

