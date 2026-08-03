#Día 27 – Métodos Especiales (Dunder Methods)
#Los métodos especiales permiten personalizar cómo se comportan los objetos.

# Los más utilizados son:   __init__()   __str__()   __len__()

#Caso 1: str()
#El método especial __str__ en Python se utiliza para definir una representación en cadena de texto
# (string) que sea legible y amigable para los humanos al trabajar con objetos de una clase personalizada.
# Si no defines este método, al intentar imprimir un objeto con print(), Python mostrará un mensaje 
# genérico poco útil como <__main__.Auto object at 0x7f81b0>.


# ********** Sin __str__:  *************
'''
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

p = Persona("Ricardo")
print(p)   # Salida:   <__main__.Persona object at 0x...>

# *********** Con __str__: ***************

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Persona: {self.nombre}"

p = Persona("Ricardo")
print(p)  #  Salida:  Persona: Ricardo

#Ejemplo ******

class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Definición del método especial __str__
    def __str__(self):
        return f"Auto: {self.marca} {self.modelo}"

# Crear una instancia (objeto) de la clase
mi_auto = Auto("Toyota", "Corolla")

# Al imprimir el objeto, se invoca automáticamente __str__
print(mi_auto)  
# Salida: Auto: Toyota Corolla

# También se invoca al usar la función integrada str()
texto = str(mi_auto)
print(texto)
# Salida: Auto: Toyota Corolla

#Caso 2 len()
#El método especial __len__ es el mecanismo interno que utiliza Python para ejecutar la función integrada
#  len(). Cuando pasas un objeto a len(objeto), Python busca y ejecuta el método objeto.__len__() 
# tras bambalinas


class Equipo:
    def __init__(self, jugadores):
        self.jugadores = jugadores

    def __len__(self):
        return len(self.jugadores)

equipo = Equipo(["Ana", "Luis", "Carlos"])

print(len(equipo))   #Salida:   3

#Ejemplo

class CarritoDeCompras:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)

    # Definición del método dunder __len__
    def __len__(self):
        return len(self.productos)

# Prueba de uso
mi_carrito = CarritoDeCompras()
mi_carrito.agregar("Laptop")
mi_carrito.agregar("Ratón")

print(len(mi_carrito))  # Devuelve 2

#Ejercicio 1.

#Crea una clase Libro.
#Atributos:   titulo    autor
#Implementa __str__() para mostrar:
#Libro: Python Básico - Juan Pérez

class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    # Definición del método especial __str__
    def __str__(self):
        return f"Libro: {self.titulo} - {self.autor}"

# Crear una instancia (objeto) de la clase
mi_libro = Libro("Pythom Basico", "Juan Perez")

# Al imprimir el objeto, se invoca automáticamente __str__
print(mi_libro)  

#Ejercicio 2
#Crea una clase Curso.
#Recibe una lista de estudiantes.
#Implementa __len__() para que:   print(len(curso))    muestre la cantidad de estudiantes.

class Curso:

    def __init__(self, estudiantes):
        self.estudiantes = estudiantes

    # Definición del método dunder __len__
    def __len__(self):
        return len(self.estudiantes)
    
curso = Curso(["Ricardo", "Johana", "Jose", "Felipe"])

print(len(curso))  

#Ejercicio 3
#Crea una clase Biblioteca.
#Guarda una lista de libros.
#Implementa:  __len__() para contar libros y   __str__()  para mostrar algo como:  Biblioteca con 5 libros

class Biblioteca:

    def __init__(self):
        self.libros = ["Matematica", "Lenguaje", "Ingles", "Etica", "Ciencia"]

    # Definición del método dunder __len__
    def __len__(self):
        return len(self.libros)

    # Definición del método especial __str__
    def __str__(self):
        return f"Biblioteca con {len(self.libros)} libros"
    
biblioteca = Biblioteca()
print(biblioteca)


#Mini Reto ⭐
#Crea la clase Playlist.   Debe almacenar una lista de canciones.
#Al ejecutar:   print(playlist)   mostrar:   Playlist con 4 canciones
#Y al ejecutar:  len(playlist)  devolver la cantidad de canciones.

class Playlist:

    def __init__(self):
        self.canciones = ["Madrigal", "Precidio", "Loco", "Tu poeta"]

    # Definición del método dunder __len__
    def __len__(self):
        return len(self.canciones)

    # Definición del método especial __str__
    def __str__(self):
        return f"Playlist con {len(self.canciones)} canciones"
    
playlist = Playlist()
print(playlist)
print(len(playlist))
'''

#Caso 3 eq()

#El método mágico __eq__ en Python te permite personalizar el comportamiento del operador de 
# igualdad (==). Por defecto, comparar dos instancias de una clase con == compara sus posiciones 
# en la memoria (su identidad), pero al definir __eq__, puedes hacer que dos objetos se consideren 
# iguales si coinciden sus atributos

#Ejemplo práctico de cómo comparar objetos por sus valores en lugar de su identidad en memoria
'''
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __eq__(self, other):
        # Verifica que 'other' sea de la misma clase para evitar errores
        if not isinstance(other, Persona):
            return False
        # Compara los atributos y devuelve True o False
        return self.nombre == other.nombre and self.edad == other.edad

# Creación de objetos con los mismos datos
persona1 = Persona("Ana", 28)
persona2 = Persona("Ana", 28)
persona3 = Persona("Juan", 30)

print(persona1 == persona2)  # Devuelve True
print(persona1 == persona3)  # Devuelve False
'''

class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __eq__(self, other):
        # Si el otro objeto no es un Producto, no son iguales
        if not isinstance(other, Producto):
            return False
        # La igualdad se define estrictamente por el código único
        return self.codigo == other.codigo

# Creamos dos instancias del mismo producto, pero con precios distintos (ej. una oferta)
producto_antiguo = Producto("PROD123", "Laptop Asus", 800)
producto_oferta  = Producto("PROD123", "Laptop Asus", 750)

# Creamos un producto totalmente diferente
producto_distinto = Producto("PROD999", "Mouse Logitech", 25)

# Pruebas de comparación
print(producto_antiguo == producto_oferta)   # Devuelve True (mismo código)
print(producto_antiguo == producto_distinto) # Devuelve False (distinto código)
print(producto_antiguo == "PROD123")         # Devuelve False (son tipos diferentes)