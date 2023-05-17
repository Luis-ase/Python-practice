#Ejercicio 011
"""
Escribir un programa que permita resolver el siguiente problema:
Tres personas aportan diferente capital a una sociedad y 
desean saber el valor total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje).
Solicitar la carga por teclado del nombre de cada socio y 
su capital aportado, a partir de esto calcular e informar lo requerido previamente.
"""
nombre_de_la_persona_1= input("Tu nombre persona 1:")
nombre_de_la_persona_2= input("Tu nombre persona 2:")
nombre_de_la_persona_3= input("Tu nombre persona 3:")

inversion_de_la_persona_1=float(input("Cuanto inverstiste en la sociedad persona 1:"))
inversion_de_la_persona_2=float(input("Cuanto inverstiste en la sociedad persona 2:"))
inversion_de_la_persona_3=float(input("Cuanto inverstiste en la sociedad persona 3:"))

suma_total_de_las_inversiones = inversion_de_la_persona_1 + inversion_de_la_persona_2 + inversion_de_la_persona_3

porcentaje_de_la_persona_1 =round((inversion_de_la_persona_1 / suma_total_de_las_inversiones)* 100 , 2)
porcentaje_de_la_persona_2 =round((inversion_de_la_persona_2 / suma_total_de_las_inversiones)* 100 , 2)
porcentaje_de_la_persona_3 =round((inversion_de_la_persona_3 / suma_total_de_las_inversiones)* 100 , 2)

print(f"El valor aportado por la persona {nombre_de_la_persona_1} es del {porcentaje_de_la_persona_1}%",
      f"El valor aportado por la persona {nombre_de_la_persona_2} es del {porcentaje_de_la_persona_2}%",
      f"El valor aportado por la persona {nombre_de_la_persona_3} es del {porcentaje_de_la_persona_3}%",
      sep="\n")