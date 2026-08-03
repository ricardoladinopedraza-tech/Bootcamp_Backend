### ema: List Comprehension (Comprensión de listas)
#Esta es una herramienta MUY usada en Python profesional porque permite crear listas de forma más rápida
#  y elegante.

'''
#Forma tradicional

numeros = []

for i in range(5):
    numeros.append(i)

print(numeros)

#Con List Comprehension

numeros = [i for i in range(5)]

print(numeros)

#Multiplicar valores

dobles = [i * 2 for i in range(5)]

print(dobles)

#Trabajar con listas existentes
numeros = [1, 2, 3, 4]

cuadrados = [n ** 2 for n in numeros]

print(cuadrados)

#Agregar condiciones
pares = [i for i in range(10) if i % 2 == 0]

print(pares)

#Ejemplo con texto
nombres = ["ana", "juan", "carlos"]

mayusculas = [nombre.upper() for nombre in nombres]

print(mayusculas)

#  ************Comparación importante*************
#Forma normal
cuadrados = []

for i in range(5):
    cuadrados.append(i ** 2)
#List comprehension
cuadrados = [i ** 2 for i in range(5)]

# ***************Mismo resultado, menos código.*********************
'''
#Mini práctica 🧠
#Ejercicio 1    Crea una lista con los números del 1 al 10 usando list comprehension.

prueba_ricardo = []

for i in range(1, 11):
    prueba_ricardo.append(i)

print(prueba_ricardo)

prueba_ricardo_1 = []

prueba_ricardo_1 = [i for i in range(1,11)]

print(prueba_ricardo_1)

#Ejercicio 2
#Crea una lista con:  los cuadrados de los números del 1 al 5
#Resultado esperado:    [1, 4, 9, 16, 25]

prueba_cuadrados = []

for i in range (1, 6):
    prueba_cuadrados.append(i ** 2)

print(prueba_cuadrados)

prueba_cuadrados_1 = []

prueba_cuadrados_1 = [i ** 2 for i in range(1, 6)]

print(prueba_cuadrados_1)

#Ejercicio 3
#Crea una lista con solo números impares:   0 al 10

impares = []

for i in range(10):
    if i % 2 ==1:
        impares.append(i)

print(impares)

impares_1 = []

impares_1 = [i for i in range(10) if i % 2 == 1]

print(impares_1)

#Ejercicio 4
#Convierte esta lista a mayúsculas:

frutas = ["manzana", "pera", "uva"]

mayusculas = [nombre.upper() for nombre in frutas]

print(mayusculas)

#Mini reto 🚀
#Usa list comprehension para crear una lista con: números del 1 al 20, pero solo múltiplos de 3

multiplos = []

multiplos = [i for i in range (1, 21) if i % 3 == 0]

print(multiplos)

