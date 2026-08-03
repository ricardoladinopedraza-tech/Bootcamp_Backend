#Día 28 — Decoradores (Decorators)

#Los decoradores permiten modificar o ampliar el comportamiento de una función sin cambiar su código original.
'''
def decorador(funcion):

    def envoltura():
        print("Antes de ejecutar la función")

        funcion()

        print("Después de ejecutar la función")

    return envoltura

#Uso:

def saludar():
    print("Hola")

saludar = decorador(saludar)

saludar()

#Sintaxis con @

def decorador(funcion):

    def envoltura():
        print("Antes")

        funcion()

        print("Después")

    return envoltura


@decorador
def saludar():
    print("Hola")


saludar()

#Ejercicio 1
#Crea un decorador que muestre:  Iniciando función...  antes de ejecutar cualquier función.
#Después crea una función:  mensaje()   que imprima:  Aprendiendo decoradores
#y aplícale el decorador.

def decorador(funcion):

    def envoltura():
        print("Iniciando función... ")

        funcion()

    return envoltura

def mensaje():
    print("Aprendiendo decoradores!")

mensaje = decorador(mensaje)   #usando @ esto cambia por @decorador

mensaje()

#mismo ejercicio usando @

def decorador(funcion):

    def envoltura():
        print("Iniciando función...")

        funcion()

    return envoltura


@decorador   #sin @ esto cambia por mensaje = decorador(mensaje)
def mensaje():
    print("Aprendiendo decoradores!")


mensaje()

#Ejercicio 2
#Crea un decorador que muestre: Función finalizada.   después de ejecutar la función.
#Aplica el decorador a una función:  despedida()   que imprima:   Hasta luego

def decorador(funcion):

    def envoltura():

        funcion()

        print("Funcion finalizada")

    return envoltura

@decorador
def despedida():
    print("Hasta luego")        

despedida()

#Ejercicio 3
#Crea un decorador que muestre:   === Inicio ===  antes de la función y: === Fin === después de la función.
#Aplícalo a una función: estudiar()  que imprima:   Estudiando Python

def decorador(funcion):

    def envoltura():
        print(" ===Inicio=== ")

        funcion()

        print(" ===Fin=== ")

    return envoltura

@decorador
def estudiar():
    print("Estudiando Python")

estudiar()

#Mini Reto ⭐
#Crea un decorador que cuente cuántas veces se ejecuta una función.
#Ejemplo esperado:   saludar()  saludar()   saludar()
#Salida: 
#Esta función se ha ejecutado 1 veces    Hola
#Esta función se ha ejecutado 2 veces    Hola
#Esta función se ha ejecutado 3 veces    Hola
'''
def decorador(funcion):

    i = 0
    
    def envoltura(*args, **kwargs):
        nonlocal i
        
        i += 1
        
        print(f"Esta funcion se ha ejecutado {i} veces")

        return funcion(*args, **kwargs)
        
    return envoltura

@decorador
def saludar():
    print("Hola") 

saludar()
saludar()
saludar()
saludar()




'''
def decorador(funcion):

    contador = 0

    def envoltura(*args, **kwargs):
        nonlocal contador

        contador += 1

        print(f"Esta función se ha ejecutado {contador} veces")

        return funcion(*args, **kwargs)

    return envoltura


@decorador
def saludar(nombre):
    print(f"Hola {nombre}")


saludar("Ricardo")
saludar("Ana")
saludar("Carlos")
'''