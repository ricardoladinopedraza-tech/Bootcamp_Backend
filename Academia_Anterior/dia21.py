#Día 21 — Atributos y métodos de objetos
'''
class Perro:

    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print("¡Guau!")

    def presentarse(self):
        print(f"Soy {self.nombre} y soy un {self.raza}")

#Creamos objetos:

perro1 = Perro("Max", "Labrador")
perro2 = Perro("Rocky", "Pastor Alemán")

#Usamos métodos:

perro1.presentarse()
perro2.presentarse()

perro1.ladrar()

#¿Qué es self?
#self representa al objeto que está ejecutando el método.

#Mini práctica 🧠
#Ejercicio 1    Crea una clase llamada:    Persona

class Persona:

#Ejercicio 2
#Agrega un constructor que reciba:  nombre    edad

def __init__(self, nombre, edad)
    
#Ejercicio 3
#Crea un método:    presentarse()  que imprima algo como:   Hola, me llamo Ricardo y tengo 30 años.

self.nombre = nombre
self.edad = edad

def presentarse(self):
    print("Hola, me llamo {self.nombre} y tengo {self.edad} años")

#Ejercicio 4
#Crea dos objetos diferentes y llama al método presentarse() para ambos.

persona1 = Persona("Ricardo", 30)
persona2 = Persona("Johana", 27)
'''
#Completo

class Persona:

    def __init__(self, nombre, edad):
    
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

persona1 = Persona("Ricardo", 30)
persona2 = Persona("Johana", 27)

persona1.presentarse()
persona2.presentarse()

#Ejemplo con ajustes

class Persona:

    def __init__(self, nombre, edad):
    
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

    def cumplir_anios(self):
        self.edad += 1
        print(f"Ahora tengo {self.edad} años")

persona1 = Persona("Ricardo", 30)
persona2 = Persona("Johana", 27)

persona1.presentarse()
persona2.presentarse()
persona1.cumplir_anios()

#Mini desafío final 🧠
#Sin crear una nueva clase, agrega un método:   cambiar_nombre(nuevo_nombre)

class Persona:

    def __init__(self, nombre, edad):
    
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

    def cumplir_anios(self):
        self.edad += 1
        print(f"Ahora tengo {self.edad} años")

    def cambiar_nombre(self, nuevo_nombre):
        self.nuevo_nombre = nuevo_nombre
        print(f"Hola, me llamo {self.nuevo_nombre} y tengo {self.edad} años")

persona1 = Persona("Ricardo", 30)
persona2 = Persona("Johana", 27)


persona1.presentarse()
persona1.cambiar_nombre("Carlos")

