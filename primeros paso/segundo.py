#Ejercicio 011
"""
Escribir un programa que permita resolver el siguiente problema:
Tres personas aportan diferente capital a una sociedad y 
desean saber el valor total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje).
Solicitar la carga por teclado del nombre de cada socio y 
su capital aportado, a partir de esto calcular e informar lo requerido previamente.
"""
# nombre_de_la_persona_1= input("Tu nombre persona 1:")
# nombre_de_la_persona_2= input("Tu nombre persona 2:")
# nombre_de_la_persona_3= input("Tu nombre persona 3:")

# inversion_de_la_persona_1=float(input("Cuanto inverstiste en la sociedad persona 1:"))
# inversion_de_la_persona_2=float(input("Cuanto inverstiste en la sociedad persona 2:"))
# inversion_de_la_persona_3=float(input("Cuanto inverstiste en la sociedad persona 3:"))

# suma_total_de_las_inversiones = inversion_de_la_persona_1 + inversion_de_la_persona_2 + inversion_de_la_persona_3

# porcentaje_de_la_persona_1 =round((inversion_de_la_persona_1 / suma_total_de_las_inversiones)* 100 , 2)
# porcentaje_de_la_persona_2 =round((inversion_de_la_persona_2 / suma_total_de_las_inversiones)* 100 , 2)
# porcentaje_de_la_persona_3 =round((inversion_de_la_persona_3 / suma_total_de_las_inversiones)* 100 , 2)

# print(f"El valor aportado por la persona {nombre_de_la_persona_1} es del {porcentaje_de_la_persona_1}%",
#       f"El valor aportado por la persona {nombre_de_la_persona_2} es del {porcentaje_de_la_persona_2}%",
#       f"El valor aportado por la persona {nombre_de_la_persona_3} es del {porcentaje_de_la_persona_3}%",
#       sep="\n")

#################################################
#Ejercicio 012
"""
Escribir un programa en Python que solicite al usuario ingresar dos valores que representen 
las medidas en grados de dos ángulos interiores de un triángulo. 

Luego, calcular y mostrar por pantalla el valor en grados del ángulo restante.
Es importante recordar que la suma de los ángulos interiores de todo triángulo es de 180 grados. 
Es decir, la suma de los ángulos internos de un triángulo siempre es igual a 180 grados. 
Por lo tanto, para calcular el ángulo restante es necesario restar la suma de los dos ángulos interiores 
ingresados al valor 180."
Para pensar:
¿Qué pasaría si se ingresan valores negativos como medidas de ángulos?

¿Qué sucedería si la suma de los dos ángulos ingresados es mayor o igual a 180 grados?

"""
# TOTAL= 180
# angulo_1 = int(input("ingrese un angulo 1: "))
# angulo_2 = int(input("ingrese un angulo 2: "))

# if angulo_1 > 0 and angulo_2 >0:
#       if angulo_2 < TOTAL or angulo_1 < TOTAL:
#             restante = 0
#             restante= TOTAL - angulo_1 - angulo_2
#             triangulo = restante + angulo_1 +angulo_2
#             if triangulo == 180:
#                   print(f"exito el angulo restante para formar 180° es {restante}")
#             if triangulo < 180:
#                   print(f"no es un triangulo") 
#       else:
#             print(f"tiene que ingresar angulos que sea menores a 180")
# else:
#       print("tiene que ingresar angulo positivos no exite angulos negativos ")

#################################################
#Ejercicio 013
"""
Escribir un programa para calcular el importe a cobrar por un vendedor, 
considerando su sueldo fijo de $200000 pesos más el 16% del monto total 
de ventas realizadas durante un mes.
Pensando los pasos para resolver el problema:
1 Solicitar al usuario que ingrese el monto total de ventas realizadas 
por el vendedor durante el mes en una variable correspondiente.

2 Calcular el 16% del monto total de ventas realizadas y almacenar el resultado en una variable.

3 Sumar el resultado del cálculo anterior al sueldo fijo del vendedor.

4 Mostrar el importe a cobrar por el vendedor.

Para pensar:
¿Qué pasaría si se modificara el sueldo fijo del vendedor?

Si se modifica el sueldo fijo del vendedor, entonces 
la fórmula utilizada para calcular el salario total debería ser actualizada para reflejar 
el nuevo sueldo fijo. En este caso, si el sueldo fijo aumenta, 
entonces el salario total también aumentaría. De igual manera, 
si el sueldo fijo disminuye, entonces el salario total también disminuiría. 
Es importante actualizar la fórmula en el programa para asegurarse de que el 
cálculo del salario total sea preciso y refleje el cambio en el importe a cobrar por del vendedor.

¿Hay que modificar el programa cada vez? ¿Cómo lo soluciono?
"""
# SUELDO=200000
# monto_total_de_ventas_realizadas= float(input("Monto total de ventas: "))
# porcentaje_de_las_ventas = (monto_total_de_ventas_realizadas/100) * 16

# sueldo_total= SUELDO + porcentaje_de_las_ventas
# print(f"El sueldo que obtendras por las ventas realizadas es de: {sueldo_total} ")

#################################################
#Ejercicio 014
"""
Escribir un programa que permita al usuario ingresar el ancho y largo de un terreno en metros,
junto con el valor del metro cuadrado de tierra. El programa debe calcular 
y mostrar el valor total del terreno. 
Además, debe calcular la cantidad de metros de alambre necesarios para cercar 
completamente el terreno a tres alturas distintas.
Pensando los pasos para resolver el problema:
Solicitar al usuario que ingrese el ancho del terreno en metros 
y almacenarlo en una variable. Solicitar al usuario que ingrese el largo del terreno en metros 
y almacenarlo en otra variable. Solicitar al usuario que ingrese el valor del metro cuadrado de tierra 
y almacenarlo en otra variable. Calcular el valor total del terreno multiplicando el ancho por el largo 
y luego multiplicando el resultado por el valor del metro cuadrado de tierra.
Mostrar el valor total del terreno al usuario. 
Calcular la cantidad de metros de alambre necesarios para cercar el terreno a tres alturas distintas. 
Por ejemplo, se puede calcular la cantidad de alambre necesaria para cercar a 1 metro de altura,
 a 2 metros de altura y a 3 metros de altura. 
 Para hacerlo, se debe sumar el perímetro del terreno (2 veces el ancho más 2 veces el largo) 
 y luego multiplicarlo por la cantidad de alturas. 
 Mostrar la cantidad de metros de alambre necesarios para cercar el terreno a las tres alturas 
 distintas al usuario.

"""
# ancho = int(input("Ancho del terreno en metros: "))
# largo = int(input("Largo del terreno en metros: "))
# metros_cuadrados_del_terreno = int(input("Metros cuadrados del terreno : "))
# terreno_total= (ancho * largo) * metros_cuadrados_del_terreno
# print(f"Valor total del terreno : {(terreno_total)}")

#################################################
#Ejercicio 015
"""
Definición del problema: Una inmobiliaria paga a sus vendedores un salario base, 
más una comisión fija por cada venta realizada, más el 5% del valor de esas ventas. 
Realizar un programa que imprima el nombre del vendedor 
y el salario que le corresponde en un determinado mes.

Se leen por teclado el nombre del vendedor, la cantidad de ventas que realizó 
y el valor total de las mismas.
¿Sobran datos? ¿Qué datos sobran?

"""
# SALARIO_BASE= 100000
# COMISION_FIJA_POR_VENTA= 200
# nombre_del_vendedor = input("Ingrese su nombre vendedor:")
# ventas_realizadas_por_mes = int(input("Ingrese el numero de ventas realizadas en el mes: "))
# cantidad_de_monto_realizado_en_el_mes = int(input("Ingrese el monto obtenido en el mes: "))
# salario_total= SALARIO_BASE + (COMISION_FIJA_POR_VENTA *ventas_realizadas_por_mes) + ((cantidad_de_monto_realizado_en_el_mes/100)* 5)
# print(f"Nombre del vendedor: {nombre_del_vendedor}.\n Cantidad de ventas realizada: {ventas_realizadas_por_mes}.\n Monto total por las ventas realizadas en el men {cantidad_de_monto_realizado_en_el_mes}.\n Salario total del vendedor en este mes:{salario_total}")

#################################################
#Ejercicio 016
"""
Escribir un programa que permita al usuario ingresar un período de tiempo en segundos. 
Luego, el programa debe convertir ese período de tiempo a una forma más legible 
y comprensible para el usuario, expresando el resultado en días, horas, minutos y segundos. 
El resultado se mostrará en pantalla en un mensaje que indique la cantidad de segundos ingresados 
y su equivalente en días, horas, minutos y segundos.
Ejemplo: 200000 segundos equivalen a 2 días, 7 horas, 33 minutos y 20 segundos.

Usar en el programa las siguientes instrucciones:
dias = segundos // 86400 # 86400 segundos = 1 día

horas = (segundos % 86400) // 3600 # 3600 segundos = 1 hora

minutos = (segundos % 3600) // 60 # 60 segundos = 1 minuto

segundos_restantes = segundos % 60 # segundos restantes

"""
# segundos_convertir = int(input("Ingrese los segundo a convertir: "))
# dias= round(segundos_convertir / 86400) 
# horas = round((segundos_convertir % 86400) / 3600)
# minutos = round((segundos_convertir % 3600) / 60)
# segundos_restantes = round((segundos_convertir % 60))

# print(
#     f""" 
#     {dias} dias
#     {horas} horas
#     {minutos} minutos
#     {segundos_restantes} segundos restantes
#     """)

#################################################
#Ejercicio 017
"""
¡Ayuda! Se me rompió el programa que convierte una cantidad de dinero en la cantidad mínima de billetes 
y monedas necesarios. Tengo todas las instrucciones necesarias, pero están todas mezcladas. 
¿Podrías ayudarme a ordenarlas de manera correcta para que funcione el programa como debería? 
A lo mejor se me perdieron algunas instrucciones, ¿podrías agregarlas?
"""
cantidad_total = int(input("Ingrese la cantidad de dinero a convertir: "))
resto = cantidad_total
billetes_cien = resto // 100
billetes_uno = resto // 1
resto = resto % 100
billetes_cinco = resto // 5
billetes_mil = resto // 1000
billetes_cincuenta = resto // 50
billetes_doscientos = resto // 200
billetes_diez = resto // 10
billetes_docientos = resto // 200
resto = resto % 10
print(f"Para la cantidad de  ",cantidad_total,"senecesitan:",billetes_mil,"billetesde 1000")
print(billetes_doscientos, "billetes de  200",billetes_cien,"billetesde 100")
print(billetes_cincuenta, "billetes de  50",billetes_cien,"billetesde 10")
print(billetes_cinco, "billetes de  5",billetes_cien,"billetesde 1")


#################################################
#Ejercicio 018
"""
Escribir un programa que permita al usuario ingresar un número entero y 
luego muestre un mensaje indicando si el número es par o impar.
Pensando los pasos para resolver el problema:
-1 Pedir al usuario que ingrese un número entero.
-2 Almacenar ese número en una variable.

-3 Verificar si el número es par o impar.

Si el número es par, mostrar un mensaje indicando que es par.
Si el número es impar, mostrar un mensaje indicando que es impar.
(Para verificar si un número es par o impar, se puede utilizar el operador módulo (%). 
Si el resto de la división del número por 2 es 0, entonces el número es par. 
Si el resto de la división del número por 2 es 1, entonces el número es impar.)

"""
#################################################
#Ejercicio 019
"""
Escribir un programa que permita ingresar dos números enteros e indicar si son iguales o distintos.

"""
#################################################
#Ejercicio 020
"""
Escribir un programa que permita ingresar dos cadenas de caracteres e indicar si son iguales o distintas.

"""


