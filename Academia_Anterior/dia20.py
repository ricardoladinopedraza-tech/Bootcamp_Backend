######    POO (Parte 2): Métodos y objetos

#Ayer creaste una clase Perro.
#Hoy vamos a reforzar uno de los conceptos más importantes de la Programación Orientada a Objetos:
'''
class Perro:

    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print("Guau!")

#Crear objeto:

mi_perro = Perro("Max", "Labrador")

#Usar atributos:

print(mi_perro.nombre)
print(mi_perro.raza)
mi_perro.ladrar()

# AGREGAR MAS METODOS

class Perro:

    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print("Guau!")

    def presentarse(self):
        print(f"Soy {self.nombre} y soy un {self.raza}")

mi_perro = Perro("Max", "Labrador")

mi_perro.ladrar()
mi_perro.presentarse()


#Mini práctica 🧠
#Ejercicio 1     Crea una clase:    Gato

class Gato:

#Ejercicio 2
#Agrega un constructor que reciba:   nombre     color

class Gato:

    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        

#Ejercicio 3
#Crea un método:  maullar()
#Que imprima:   Miau!

class Gato:

    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def maullar(self):
        print("Miau!")



#Ejercicio 4
#Crea un método:   presentarse()
#Que imprima algo similar a:    Soy Luna y soy de color blanco

class Gato:

    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def maullar(self):
        print("Miau!")

    def presentarse(self):
        print(f"Soy {self.nombre} y soy color {self.color}")


#Ejercicio 5
#Crea un objeto:    Luna        blanco

class Gato:

    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def maullar(self):
        print("Miau!")

    def presentarse(self):
        print(f"Soy {self.nombre} y soy color {self.color}")


mi_gato = Gato("Luna", "blanco")

mi_gato.maullar()
mi_gato.presentarse()
'''

#Mini práctica extra 🚀

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre}")

    def cumplir_anios(self):
        self.edad = self.edad + 1
        print(f"Edad: {self.edad}")
        
    #def cumplir_anios(self):  Abreviado pero mas prof
        #self.edad += 1

        

persona1 = Persona("Ricardo", 30)

persona1.saludar()
persona1.cumplir_anios()