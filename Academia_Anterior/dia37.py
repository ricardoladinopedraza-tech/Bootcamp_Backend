#Día 37 — Funciones zip(), enumerate() y patrones comunes de entrevistas

#1. zip()
#Permite unir varias secuencias elemento por elemento.
#La función zip() en Python agrupa elementos de dos o más iterables (como listas o 
# tuplas) en una secuencia de tuplas. Une el elemento en la posición 0 del primer 
# iterable con el elemento en la posición 0 del segundo, y así sucesivamente.




'''
nombres = ["Ana", "Luis", "Carlos"]
edades = [20, 25, 30]

resultado = zip(nombres, edades)

print(list(resultado))

#Recorrer con zip

nombres = ["Ana", "Luis", "Carlos"]
edades = [20, 25, 30]

for nombre, edad in zip(nombres, edades):
    print(nombre, edad)

#2. enumerate()
#Permite obtener índice y valor al mismo tiempo.

frutas = ["manzana", "pera", "uva"]

for indice, fruta in enumerate(frutas):
    print(indice, fruta)

#Empezar desde otro número

frutas = ["manzana", "pera", "uva"]

for indice, fruta in enumerate(frutas, start=1):
    print(indice, fruta)

#3. Combinar zip + enumerate
#Muy común en entrevistas.

nombres = ["Ana", "Luis", "Carlos"]
edades = [20, 25, 30]

for i, (nombre, edad) in enumerate(zip(nombres, edades), start=1):
    print(i, nombre, edad)

#Ejercicios de análisis (sin ejecutar)
#Ejercicio 1
nombres = ["Juan", "Pedro"]
edades = [18, 22]

for nombre, edad in zip(nombres, edades):
    print(nombre, edad)

#¿Qué imprime?  >>> Imprime 
# Juan 18
# Pedro 22

#Ejercicio 2

frutas = ["pera", "uva", "mango"]

for i, fruta in enumerate(frutas):
    print(i, fruta)

#¿Qué imprime?  >>> 
#  0 pera
#  1 uva
#  2 mango

#Ejercicio 3

a = [1, 2, 3]
b = ["A", "B", "C"]

print(list(zip(a, b)))

#¿Qué imprime? >>> Imprime  [(1, 'A'), (2, 'B'), (3, 'C')]

#Ejercicio 4

numeros = [10, 20, 30]

for i, n in enumerate(numeros, start=1):
    print(i, n)

#¿Qué imprime? >>> Imprime  
# 1 10
# 2 20
# 3 30

#Mini reto extra (nivel entrevista)
#Sin ejecutar código:

nombres = ["Ana", "Luis", "Carlos"]
notas = [4.5, 3.8, 4.9]

resultado = [
    f"{nombre}: {nota}"
    for nombre, nota in zip(nombres, notas)
]

print(resultado)

#¿Qué imprime?  >>> Imprime ['Ana: 4.5', 'Luis: 3.8', 'Carlos: 4.9']

#Pregunta de razonamiento
#Supón:

nombres = ["Ana", "Luis", "Carlos"]
edades = [20, 25]

#¿Qué ocurre al ejecutar? >>> Al ejecutar no imprime nada

list(zip(nombres, edades))

#¿Por qué sucede eso? >>> al ser los iterables desiguales, la funcion se detiene 
# tan pronto se terminan los elementos del iterable mas corto (edades)
'''