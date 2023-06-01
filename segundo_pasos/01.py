"""
Vimos anteriormente el programacion estructurado 

"""
def convertir_a_año(f):
    return f //10000

def convertir_a_mes(f:int):
    return (f//100) %100

def convertir_a_dia(f:int):
    return f%100


def main():
    numero = 19851217
    año = convertir_a_año(numero)
    dia = convertir_a_dia(numero)
    mes = convertir_a_mes(numero)
    print(f"fecha : {numero}  {año}-{mes}-{dia}")



main()