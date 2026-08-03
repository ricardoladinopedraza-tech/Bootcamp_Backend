#Día 39 — Funciones sorted() y key
#Este es un tema muy usado en entrevistas y en proyectos reales.

#1. ¿Qué hace sorted()?
#Permite ordenar elementos sin modificar la colección original.
'''
numeros = [5, 2, 8, 1]

resultado = sorted(numeros)

print(resultado)
print(numeros)

#2. Orden descendente
numeros = [5, 2, 8, 1]

resultado = sorted(numeros, reverse=True)

print(resultado)

#3. Ordenando palabras

palabras = ["python", "java", "go", "javascript"]

resultado = sorted(palabras) #>>> Las ordena en orden alfabetico <<<

print(resultado)

#4. El parámetro key
#Permite indicar por qué criterio ordenar.
#Ejemplo: ordenar por longitud.

palabras = ["python", "go", "java", "javascript"]

resultado = sorted(
    palabras,
    key=len
)

print(resultado)

#5. key con lambda
#Muy común.

nombres = ["Ana", "Carlos", "Luis"]

resultado = sorted(
    nombres,
    key=lambda nombre: len(nombre)
)

print(resultado)

#6. Ordenando tuplas
personas = [
    ("Ana", 25),
    ("Luis", 20),
    ("Carlos", 30)
]

resultado = sorted(
    personas,
    key=lambda persona: persona[1]
)

print(resultado)
'''

#Ejercicios de análisis (sin ejecutar)
#Ejercicio 1
numeros = [7, 2, 9, 1]

resultado = sorted(numeros)

print(resultado)

#¿Qué imprime?  >>> Imprime [1, 2, 7, 9]

#Ejercicio 2
palabras = ["python", "go", "java"]

resultado = sorted(
    palabras,
    key=len
)

print(resultado)

#¿Qué imprime?  >>> Imprime ['go', 'java', 'python]

#Ejercicio 3
datos = [
    ("Pedro", 32),
    ("Ana", 25),
    ("Luis", 28)
]

resultado = sorted(
    datos,
    key=lambda x: x[1]
)

print(resultado)

#¿Qué imprime?  >>> Imprime [('Ana', 25), ('Luis', 28), ('Pedro', 32)]

#Ejercicio 4
palabras = ["sol", "montaña", "mar"]

resultado = sorted(
    palabras,
    key=lambda p: len(p),
    reverse=True
)

print(resultado)

#¿Qué imprime?  >>> Imorime ['montaña', 'sol', 'mar']

#Mini reto extra (nivel entrevista)
#Sin ejecutar código:

productos = [
    ("Teclado", 80),
    ("Mouse", 30),
    ("Monitor", 250),
    ("USB", 20)
]

resultado = sorted(
    productos,
    key=lambda p: p[1],
    reverse=True
)

print(resultado)

#¿Cuál es la salida exacta? >>> 
# [('Monitor', 250), ('Teclado', 80), ('Mouse', 30), ('USB', 20)]

#¿Por qué sorted() devuelve una nueva lista mientras que 
# .sort() modifica la lista original?

#Creo que por diseno y con el objetivo de mantener recursos como la memoria. sorted()
#crea una nueva lista, en lista pequenas no afecta pero el listas de muchos elementos
#puede ocupar mucha memoria, pero a su ves modifica la lista original. .sort() trabaja
#sobre la lista original ahorra memoria, pero tambien modifica la lista.