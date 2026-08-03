#### Funciones avanzadas
'''
def saludar():
    print("Hola!")

saludar()

#Estructura basica
def nombre_funcion():
    codigo

def despedida():
    print("Adiós")

despedida()

#Funciones con parámetros
#Los parámetros permiten enviar datos a la función.

def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Ricardo")
saludar("Ana")

#Funciones con varios parámetros

def sumar(a, b):
    print(a + b)

sumar(5, 3)
sumar(10, 20)


#return
#return devuelve un valor.

def sumar(a, b):
    return a + b

resultado = sumar(5, 3)

print(resultado)

#Diferencia entre print() y return
#   Con print

def suma(a, b):
    print(a + b) #Solo muestra


#    Con return

def suma(a, b):
    return a + b #Devuelve el valor para reutilizarlo

#Función que valida datos

def es_mayor_edad(edad):

    if edad >= 18:
        return True
    
    else:
        return False
    
print(es_mayor_edad(20))
print(es_mayor_edad(15))

#Variables locales
#Las variables creadas dentro de una función existen SOLO dentro de ella.

#Ejemplo
def prueba():
    numero = 10
    print(numero)

prueba()

#Ejemplo 1  --- Calculadora BAsica
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):

    if b == 0:
        return "No se puede dividir por cero"

    return a / b


print(suma(10, 5))
print(resta(10, 5))
print(multiplicacion(10, 5))
print(division(10, 5))


###  ***** Buenas prácticas *******
#✅ Nombres claros
#  calcular_total()
# ❌ Evitar:
#  ct()

#Una función = una tarea
#✅ Reutilizar funciones

#Mini práctica
#Ejercicio 1
#Crea una función llamada
#       saludar()
#Que imprima:
#       Bienvenido al sistema

def saludar():
    print("Bienvenido al sistema")

saludar()

#Ejercicio 2
#  Crea una función:
#   multiplicar(a, b)
#  Que devuelva la multiplicación.

def multiplicar(a, b):
    return a * b

print(multiplicar(2, 5))

#Ejercicio 3
#Crear una función que reciba un nombre y una edad e imprima:
#            Hola Ricardo, tienes 30 años

def datos():
    nombre = str(input("Escribir nombre: "))
    edad = int(input("Digita edad: "))
    print("Hola", nombre, "tienes", edad, "años")

datos()

#Otra manera, aca la funcion queda reutilizable

def datos(nombre, edad):
    print("Hola", nombre, "tienes", edad, "años")

datos("Ricardo", 30)

#Ejercicio 4
#Crear una función que determine si un número es par.
#Debe devolver:    True   o   False


def prueba():
    numero = int(input("Digite un numero: "))
    residuo = numero % 2
    if residuo == 0:
        return True
    else:
        return False
   
print(prueba())

#Otra funcion del ejercicio anterior, mas profesonal
def es_par(numero):

    if numero % 2 == 0:
        return True
    
    else:
        return False

print(es_par(8))

#Mini reto del día 🚀
#Crear una función que calcule el IVA.
#Ejemplo:    calcular_iva(100000, 19)
#Resultado:   119000

def impuesto(a, b):
    return (a * b) / 100 


print(impuesto(100000, 19))
'''

#Manera mas profesional

def calcular_iva(precio, iva):

    total_iva = (precio * iva) / 100

    return precio + total_iva

print(calcular_iva(100000, 19))

#Ejemplo de funcion reutilizable

def calcular_iva(precio, iva):
    return precio + (precio * iva / 100)

precio = float(input("Precio: "))
iva = float(input("IVA: "))

print(calcular_iva(precio, iva))


#**************** “La función debe hacer UNA tarea bien.” **************