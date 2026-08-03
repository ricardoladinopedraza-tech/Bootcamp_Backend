#Encapsulación en POO
#La encapsulación consiste en proteger los datos de una clase para que no se modifiquen de forma
#  incorrecta desde fuera.
'''
class CuentaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

    def mostrar_saldo(self):
        print(f"Saldo actual: {self._saldo}")

    def depositar(self, cantidad):
        self._saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self._saldo:
            self._saldo -= cantidad
        else:
            print("Fondos insuficientes")

cuenta = CuentaBancaria("Ricardo", 1000)

cuenta.mostrar_saldo()

cuenta.depositar(500)

cuenta.mostrar_saldo()

cuenta.retirar(200)

cuenta.mostrar_saldo()


#Mini práctica 🧠
#Crea una clase llamada: Vehiculo     Requisitos  Constructor:
#marca
#combustible

#Método: #mostrar_combustible()

#Debe mostrar el combustible actual.

#Método:
#repostar(cantidad)

#Debe sumar combustible.

#Crea un objeto:
#Toyota

#con:
#50 litros
#Reposta:
#20 litros
#Muestra el combustible antes y después.

class Vehiculo:

    def __init__(self, marca, combustible):
        self.marca = marca
        self._combustible = combustible

    def mostrar_combustible(self):
        print(f"El combustible actual es: {self._combustible}")

    def repostar(self, cantidad):
        self.combustible += cantidad
        print(f"El combustible actual es: {self._combustible}")

toyota = Vehiculo("Toyota", 50)

toyota.mostrar_combustible()
toyota.repostar(20)

# ******************* OJO *****************
#Cuando veas:

#self._saldo
#self._combustible
#self._edad

#piensa:       "Este atributo es interno. Lo ideal es manipularlo mediante métodos de la clase."

#Cuando veas:

#self.nombre
#self.marca
#self.correo

# piensa:   "Es un atributo público."

# ********************************************************************************
'''
#Mini práctica extra 🚀

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self._salario = salario

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}  \nSalario: {self._salario}")

    def aumentar_salario(self, cantidad):
        self._salario += cantidad
        
empleado1 = Empleado('Ricardo', 2000)

empleado1.mostrar_datos()
empleado1.aumentar_salario(500)
empleado1.mostrar_datos()