# Comienzo del programa 2 clase 2

# number = input("ingrese un numero flaco:")
# number2 = input("ingrese otro numero flaco:")
# number = int(number)
# number2 = int(number2)
# mostrar = number + number2

# print(mostrar)
# a = 0
# b = 1
# c = "pepe"

# print("a:",a,b,c,sep="\n")
# num1 = int(input("Numero 1:"))
# num2 = int(input("Numero 2:"))
# print(num1,num2, sep=" <==> ")

# `${} algo ` en python es f"{} algo {}"

#ejercicio 16

# segundos = input("ingrese los segundos")
# dias = segundos // 86400
# horas = (segundos % 86400) // 3600
# minutos =(segundos % 3600) // 60

# segundos_restantes = segundos % 60

#Ejercicio 21

# n1 = int(input("Numero 1:"))
# n2 = int(input("Numero 2:"))
# if n1 > n2 :
#     print("Mayor 1:" ,n1)
# else:
#     if n2 > n1:
#         print("Mayor 2:" ,n2)
#     else: 
#         print("Son iguales")

#Ejercicio 22

n1 = int(input("Numero 1:"))
n2 = int(input("Numero 2:"))
n3 = int(input("Numero 3:"))
# if n1 > n2  :
#     if n1 > n3:
#         print("Mayor 1:" ,n1)
#     else: 
#         print("Mayor 3:", n3)
# else:
#     if n2 > n1:
#         if n2 > n3:
#             print("Mayor 2:" ,n2)
#     else: 
#        print("Mayor 3:",n3)
 
mayor = n1 
if n2 > mayor :
    mayor = n2
if n3 > mayor:
    mayor = n3

print("Mayor :", mayor)    
