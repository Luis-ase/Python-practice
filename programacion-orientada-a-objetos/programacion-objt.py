
class Persona :
    edad = 0
    nombre = ""

    def __init__(self, nombre, edad) :
        self.nombre = nombre
        self.edad =edad
    def leer_edad(self) :
        return self.nombre + " tiene " + str(self.edad) +" años"

jesus= Persona("Jesus",20)
print(jesus.leer_edad())

mari= Persona("mari",22)
print(mari.leer_edad())