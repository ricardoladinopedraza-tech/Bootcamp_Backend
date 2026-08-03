#Día 25 — Clases Abstractas (ABC)
#Las clases abstractas permiten definir una "plantilla" que obliga a las clases hijas a implementar 
# ciertos métodos.
#¿Por qué son útiles?
#Imagina que todas las figuras geométricas deben calcular su área.
#No tiene sentido que una figura genérica calcule un área, pero sí que obligue a sus hijas a hacerlo.
'''
from abc import ABC, abstractmethod

class Figura(ABC):

    @abstractmethod
    def area(self):
        pass


class Cuadrado(Figura):

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado


class Rectangulo(Figura):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


cuadrado = Cuadrado(5)
rectangulo = Rectangulo(4, 6)

print(cuadrado.area())
print(rectangulo.area())

#Ejercicio 1
#Crea:   Animal   Perro  Gato

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau! Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau! Miau!")

miperro = Perro()

miperro.hacer_sonido()

migato = Gato()

migato.hacer_sonido()


#Ejercicio 2
#Crea: Empleado  Programador  Diseñador  
# Requisitos
#Clase abstracta:  trabajar()
#Implementaciones:  El programador escribe código.  El diseñador crea interfaces.


from abc import ABC, abstractmethod

class Empleado(ABC):

    @abstractmethod
    def trabajador(self):
        pass

class Programador(Empleado):

    def trabajador(self):
        print(f"El programador escribe codigo")

class Diseñador(Empleado):

    def trabajador(self):
        print(f"El diseñador crea interfaces")

empleado = Programador()

empleado.trabajador()

empleado1 = Diseñador()

empleado1.trabajador()

#Ejercicio 3 (Nivel Junior Backend)

#Crea una clase abstracta:  BaseDeDatos
#Método abstracto:  conectar()
#Clases hijas:   MySQL   PostgreSQL
#Mensajes:   Conectando a MySQL...    Conectando a PostgreSQL...

from abc import ABC, abstractmethod

class BaseDeDatos(ABC):
    @abstractmethod
    def conectar(self):
        pass

class MySQL(BaseDeDatos):

    def conectar(self):
        print(f"Conectando a MySQL...")

class PostgreSQL(BaseDeDatos):

    def conectar(self):
        print(f"Conectando a PostgreSQL...")

bases = [MySQL(), PostgreSQL()]

for base in bases:
    base.conectar()

#Mini Test 🧠
#Responde sin ejecutar código:

#1. ¿Para qué sirve @abstractmethod?
    #para obligar a las clases hijas a implementar un método específico
#2. ¿Se puede crear un objeto directamente de una clase abstracta?
    #no
#3. ¿Qué módulo debemos importar para trabajar con clases abstractas?
    #el módulo abc
#4. ¿Qué significa ABC?
    #Abstrac Base Classes 
#5. ¿Qué ventaja tienen las clases abstractas?
    #garantizan una estructura uniforme, evitan la duplicación de código y facilitan el mantenimiento 
    #de sistemas grandes.

    '''