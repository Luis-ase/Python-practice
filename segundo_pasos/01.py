"""
Vimos anteriormente el programacion estructurado 

"""
def main():
    numero = 19851217
    año = numero//10000
    dia = numero%100
    mes = (numero//100) %100
    print(f"fecha : {numero}  {año}-{mes}-{dia}") 


main()