#Programación Orientada a Objetos (POO) Parte 1 🧱

#¿Qué es una clase?
#Una clase es como un “molde”.
#Ejemplo:
#Molde → Persona
#Objetos creados → Ricardo, Juan, María

#Crear clase
'''
class Persona:
    pass        #pass significa:  “la clase está vacía por ahora”.

#Crear objetos

class Persona:
    pass

persona1 = Persona()

print(persona1)

#El método __init__
#Es el constructor.
#Se ejecuta automáticamente al crear el objeto.

class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

#¿Qué significa self?
#self representa el objeto actual.
#Es como decir:

persona1.nombre

#Ejemplo completo

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Persona("Ricardo", 30)

print(persona1.nombre)
print(persona1.edad)

#Métodos
#Las clases también pueden tener funciones.

class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

persona1 = Persona("Ricardo")

persona1.saludar()

#Mini práctica 🧠
#Ejercicio 1    Crea una clase llamada:      Perro

class perro:

#Ejercicio 2
#Agrega un constructor que reciba:   nombre     raza

class perro:

    def__init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

#Ejercicio 3
#Crea un método llamado:  ladrar()   Que imprima:    Guau!

class perro:
    # Método constructor
    def __init__(self, nombre, raza):
        self.nombre = nombre  # Atributo
        self.raza = raza      # Atributo

    def ladrar(self):
        print("Guau!")

my_perro = perro("Tomy", "Picher")
my_perro.ladrar()

#Mini reto 🚀
#Crea una clase:   CuentaBancaria
#Debe tener:   titular    saldo
#Y un método:    mostrar_saldo()

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def mostrar_saldo(self):
        print("Titular: ", self.titular)
        print("Saldo: ", self.saldo)

    #def mostrar_saldo(self):   #### Mas profesonal
    #print(f"Titular: {self.titular}")
    #print(f"Saldo: {self.saldo}")    

my_cuenta = CuentaBancaria("Ricardo", 500)
my_cuenta.mostrar_saldo()

'''
#
'''
#$$$$$$$$$$$$$$ OTRA VERSION DE CLASE $$$$$$$$$$$$$$$$$$$$

# 1. Definimos el molde
class Gato:
    # El constructor inicializa el nombre
    def __init__(self, mi_nombre):
        self.nombre = mi_nombre # El gato sabe su nombre

    # El método define la acción
    def maullar(self):
        print(self.nombre + " dice: ¡Miau, miau!")

# 2. Usamos el molde para crear gatos reales
mi_gato = Gato("Michi")
tu_gato = Gato("Tom")

# 3. Los gatos hacen su acción
mi_gato.maullar() # Michi dice: ¡Miau, miau!
tu_gato.maullar() # Tom dice: ¡Miau, miau!

####### $$$$$$$$$$$$ OTRO EJEMPLO $$$$$$$$$$$$$$$

# Definimos el molde
class Perro:
    def __init__(self, mi_nombre):
        # 1. Guarda el nombre aquí
        self.nombre = mi_nombre
    def ladrar(self):
        # 2. Usa la palabra mágica para llamar al nombre del perro
        print(self.nombre + " dice: ¡Guau, guau!")

# Creamos al perro de verdad
mi_perro = Perro("Fido")
mi_perro.ladrar() # Debe decir: Fido dice: ¡Guau, guau!

###### $$$$$$$$$$$$$ mas ejemolos $$$$$$$$$$$$$$$$$$$

class Auto:
    def __init__(self, mi_color):
        self.color = mi_color

    def pitar(self):
        print("¡Bip, bip!")

# 3. Usa el molde para crear un auto de verdad de color "Rojo"
mi_auto = Auto("Rojo" )

# 4. Haz que el auto use su método para pitar
mi_auto.pitar()

# $$$$$$$$$$$$$$$$$$$$$$ OTRO EJEMPLO $$$$$$$$$$$$$$$$

class Vaca:
    def __init__(self, mi_nombre, mis_litros):
        self.nombre = mi_nombre
        self.litros = mis_litros
        print(self.nombre)
        print(self.litros)

    def producir(self):
        # 5. Llama al atributo que guarda los litros de leche
        print(self.nombre + " da " + str(self.litros) + " litros de leche.")

# Creamos la vaca Lola con 5 litros
vaca_lola = Vaca("Lola", 5)
vaca_lola.producir() # Debe decir: Lola da 5 litros de leche.
'''