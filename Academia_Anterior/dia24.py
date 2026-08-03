#Día 24 – Polimorfismo
#¿Qué es el polimorfismo?

#El polimorfismo permite que diferentes clases utilicen el mismo método, pero cada una lo implemente
#  de forma distinta.

class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        print("Guau")

class Gato(Animal):
    def hablar(self):
        print("Miau")

class Vaca(Animal):
    def hablar(self):
        print("Muuu")

#Aunque tienen el método hablar(), cada uno responde de manera diferente.

animales = [Perro(), Gato(), Vaca()]

for animal in animales:
    animal.hablar()

#Ejercicio 1
#Crea las siguientes clases:  Vehiculo   Moto   Carro   Bicicleta
#Cada una debe tener el método:    moverse()
# Y mostrar mensajes diferentes:  La moto acelera.   El carro avanza.   La bicicleta pedalea.
#Después guarda los objetos en una lista y recórrela con un for.

class Vehiculo:
    def moverse(self):
        pass

class Moto(Vehiculo):
    def moverse(self):
        print(f"La moto acelera")

class Carro(Vehiculo):
    def moverse(self):
        print(f"El carro avanza")

class Bicicleta(Vehiculo):
    def moverse(self):
        print(f"La bicicleta pedalea")

vehiculos = [Moto(), Carro(), Bicicleta()]

for vehiculo in vehiculos:
    vehiculo.moverse()

#Ejercicio 2
#Crea una clase base:   Empleado
#Y dos clases hijas:    Programador    Diseñador

class Empleado:
    def trabajar(self):
        pass

class Programador(Empleado):
    def trabajar(self):
        print(f"El progrmador escribe codigo")

class Diseñador(Empleado):
    def trabajar(self):
        print("El diseñador crea interfaces")

empleados = [Programador(), Diseñador()]

for empleado in empleados:
    empleado.trabajar()