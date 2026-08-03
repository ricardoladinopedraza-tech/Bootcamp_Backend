#Día 36 – Nested Comprehensions (Comprensiones Anidadas)

#Este tema aparece mucho en entrevistas porque evalúa tu capacidad para leer y 
# construir estructuras de datos de forma compacta.

#1. ¿Qué es una Nested Comprehension?
#Es una comprensión dentro de otra comprensión.
#Ejemplo clásico:
'''
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = [
    numero
    for fila in matriz
    for numero in fila
]

print(resultado)

#2. Entendiendo el orden
#La comprensión:

[
    numero
    for fila in matriz
    for numero in fila
]

#equivale a:

resultado = []

for fila in matriz:
    for numero in fila:
        resultado.append(numero)

# >>>>>> Regla importante:  👉 Se leen los for de izquierda a derecha.  <<<<<<<<

#3. Crear una matriz
#Podemos generar estructuras bidimensionales.

matriz = [
    [0 for _ in range(3)]
    for _ in range(4)
]

print(matriz)

#4. Tabla de multiplicar
tabla = [
    [fila * columna for columna in range(1, 6)]
    for fila in range(1, 6)
]

print(tabla)

#5. Filtros en Nested Comprehensions
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

pares = [
    numero
    for fila in matriz
    for numero in fila
    if numero % 2 == 0
]

print(pares)
'''
#Ejercicio 1
#Sin ejecutar código:

matriz = [
    [1, 2],
    [3, 4]
]

resultado = [
    n
    for fila in matriz
    for n in fila
]

print(resultado)

#¿Qué imprime?  >> Imprime [1, 2, 3, 4]

#Ejercicio 2
#Sin ejecutar código:

resultado = [
    x * y
    for x in range(1, 4)
    for y in range(1, 3)
]

print(resultado)

#¿Qué imprime?  >>> imprime [1, 2, 2, 4, 3, 6]

#Ejercicio 3
#Sin ejecutar código:

matriz = [
    [2, 3, 4],
    [5, 6, 7]
]

resultado = [
    n
    for fila in matriz
    for n in fila
    if n % 2 == 0
]

print(resultado)

#¿Qué imprime?  >>> [2, 4, 6]

#Mini reto extra (nivel entrevista)
#Sin ejecutar código:

matriz = [
    [1, 2],
    [3, 4]
]

resultado = [
    n ** 2
    for fila in matriz
    for n in fila
    if n > 2
]

print(resultado)

#¿Qué imprime?  >>> imprime [9, 16]
#Explica paso a paso qué elementos:
#recorren el primer for  >> Se elije la primera fila
#recorren el segundo for  >> Se elijen los elementos de la primera fila
#pasan el filtro if n > 2  >> Se aplica filtro a elemetos de primera fila

#se aplica filtro a cada elemento al encontrar los validos se aplica la modificacion