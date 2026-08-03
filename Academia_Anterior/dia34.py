#Día 34 – Dictionary Comprehensions
#Hoy veremos una extensión natural de las list comprehensions.

#1. ¿Qué es una Dictionary Comprehension?
#Permite crear diccionarios de forma compacta.
#Sintaxis:  nuevo_diccionario = {clave: valor for elemento in iterable}
'''
numeros = [1, 2, 3, 4]

cuadrados = {n: n**2 for n in numeros}

print(cuadrados)

#2. Con condición

numeros = [1, 2, 3, 4, 5, 6]

pares = {n: n**2 for n in numeros if n % 2 == 0}

print(pares)

#3. Transformando datos

palabras = ["python", "java", "go"]

longitudes = {palabra: len(palabra) for palabra in palabras}

print(longitudes)

#4. Invirtiendo claves y valores
edades = {
    "Ana": 20,
    "Luis": 25,
    "Pedro": 30
}

invertido = {edad: nombre for nombre, edad in edades.items()}

print(invertido)

#Ejercicio 1
#Analiza la salida:

numeros = [1, 2, 3]

resultado = {n: n + 10 for n in numeros}

print(resultado)
#¿Qué imprime?  >> Imprime {1: 11, 2: 12, 3: 13}

#Ejercicio 2
#Analiza la salida:

numeros = [2, 3, 4, 5]

resultado = {n: n * 2 for n in numeros if n % 2 == 0}

print(resultado)

#¿Qué imprime?  >> Imprime {2: 4, 4: 8}

#Ejercicio 3
#Completa el resultado mentalmente:

palabras = ["sol", "luna", "estrella"]

resultado = {p: len(p) for p in palabras}

print(resultado)

# ¿Qué imprime?   >> Imprime  {'sol': 3, 'luna': 4, 'estrella': 8}

#Ejercicio 4
#Analiza la salida:

datos = {
    "a": 1,
    "b": 2,
    "c": 3
}

resultado = {valor: clave for clave, valor in datos.items()}

print(resultado)

#¿Qué imprime?  >> Imprime  {1: 'a', 2: 'b', 3: 'c'}

#Ejercicio 5 (Nivel entrevista junior)
#Sin ejecutar código, determina la salida:

numeros = [1, 2, 3, 4, 5]

resultado = {
    n: "par" if n % 2 == 0 else "impar"
    for n in numeros
}

print(resultado)

#¿Qué imprime?  >> Imprime {1: 'impar', 2: 'par', 3: 'impar', 4: 'par', 5: 'impar'}

#Desafío de razonamiento
#Sin escribir código todavía:
#Si tienes:

["python", "java", "c", "javascript"]

#¿Cómo sería el diccionario final si quisieras obtener:

{
    "python": 6,
    "java": 4,
    "c": 1,
    "javascript": 10
}

#Explica la lógica con palabras antes de pensar en la sintaxis.
#Para obtner el resultado tendriamos que hacer un diccionario donde la clave
#es la palabra "palabra" y el valor a traves de len(palabra) la cantidad de 
#caracteres que tiene la palabra, y recorremos con for.
'''
#Mini reto extra (nivel entrevista)
#Sin ejecutar código:

numeros = [1, 2, 3, 4]

resultado = {
    n: n**2
    for n in numeros
    if n > 2
}

print(resultado)

#¿Qué imprime?  >> Imprime {3: 9, 4: 16}

#Y una pregunta de razonamiento:

palabras = ["python", "java", "go"]

#Si quisieras obtener:

{
    6: "python",
    4: "java",
    2: "go"
}

#¿Qué tendrías que intercambiar respecto al ejercicio anterior?
#Para este caso hay que intercambia la clave por el valor y recoorer con for