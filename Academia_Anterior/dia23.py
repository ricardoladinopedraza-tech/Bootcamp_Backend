#Día 23 – Herencia en Programación Orientada a Objetos (POO)
# La herencia permite que una clase reutilice atributos y métodos de otra clase.
'''
class Animal:
    def comer(self):
        print("El animal está comiendo")


class Perro(Animal):
    def ladrar(self):
        print("¡Guau!")

mi_perro = Perro()

mi_perro.comer()
mi_perro.ladrar()

## Constructor en la clase padre

class Animal:

    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo")

#Clase hija:

class Perro(Animal):

    def ladrar(self):
        print(f"{self.nombre} dice ¡Guau!")

#Uso:

perro1 = Perro("Firulais")

perro1.comer()
perro1.ladrar()

#super()

#       super() permite usar métodos de la clase padre.

class Animal:

    def __init__(self, nombre):
        self.nombre = nombre


class Perro(Animal):

    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")

#Uso:

perro1 = Perro("Firulais", "Labrador")

perro1.mostrar()

#Mini práctica
#Crea una clase padre llamada:   Vehiculo  
# #Con:   atributo marca   método mostrar_marca()
#Luego crea una clase hija: Carro
#Con:   atributo modelo     método mostrar_datos()
#Debes usar:   super()   para heredar la marca.
#   Resultado esperado   Marca: Toyota   Modelo: Corolla

class Vehiculo:

    def __init__(self, marca):
        self.marca = marca
        
    def mostrar_marca(self):
        print(f"Marca: {self.marca}")
            
class Carro(Vehiculo):

    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

    def mostrar_datos(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        

vehiculo1 = Carro("Toyota", "Corolla")

vehiculo1.mostrar_datos()
'''
#Ejercicio Final
#Ahora realiza este ejercicio por tu cuenta:

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años")
        
class Estudiante(Persona):

    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def mostrar_info(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años")
        print(f"Curso: {self.curso}")

persona1 = Estudiante("Ricardo", 30, "Python Backend")

persona1.mostrar_info()