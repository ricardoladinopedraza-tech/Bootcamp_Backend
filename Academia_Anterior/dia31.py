#Día 31 – Expresiones Lambda
#Las funciones lambda son funciones pequeñas y anónimas que se utilizan mucho
#  con herramientas como map(), filter() y sorted().

# ***lambda sirve para crear funciones anónimas y de una sola línea, conocidas también
#  como funciones lambda. A diferencia de las funciones normales creadas con def, 
# no necesitan un nombre formal y su sintaxis es mucho más rápida y concisa

#Sintaxis
'''
lambda argumentos: expresión

#Equivale a:

def sumar(a, b):
    return a + b

#Versión lambda:

sumar = lambda a, b: a + b

print(sumar(3, 5))

#Ejercicio 1
#Analiza la salida:

duplicar = lambda x: x * 2

print(duplicar(4))

#¿Qué se imprime? Se imprime 8

#Ejercicio 2
#Convierte esta función a lambda:

def cuadrado(x):
    return x ** 2  

cuadrado = lambda x: x ** 2

print(cuadrado(4)) #imprime 16

#Ejercicio 3
#Completa el código:

sumar = lambda a, b: a + b

print(sumar(10, 5))

#La salida debe ser:  15

#Uso con sorted() **** puede ordenar cualquier iterable ******
#sorted([3, 1, 2])          # lista
#sorted((3, 1, 2))          # tupla
#sorted({3, 1, 2})          # conjunto
#sorted("python")           # cadena

personas = [
    ("Ana", 30),
    ("Luis", 25),
    ("Carlos", 35)
]

ordenadas = sorted(personas, key=lambda persona: persona[1])

print(ordenadas)

#Aquí la lambda indica que se ordene por la edad (persona[1]).

#Mini reto
#Crea una lambda llamada es_par que reciba un número y devuelva True si es par y False
#  si es impar.
#Ejemplo:   print(es_par(8))

es_par = lambda x: x % 2 == 0

print(es_par(8))
print(es_par(9))
'''
#Ejemplo 3: Filtrar datosCon la función filter(), lambda actúa como una condición para
#  evaluar cada elemento de una lista.

numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares) 
# Resultado: [2, 4, 6]

#Sin ejecutar el código, ¿qué imprime?

numeros = [1, 2, 3, 4]

resultado = list(map(lambda x: x * 3, numeros))

print(resultado)  # [3, 6, 9, 12]

#Regla mental útil
#filter()
#Conserva o descarta elementos existentes. Nunca inventa elementos nuevos.
#map()
#Transforma cada elemento. El número de elementos normalmente se mantiene.

#Regla mental útil para entrevistas
#Función
#Pregunta mental
#filter(f, xs)	
#“¿Qué elementos sobreviven?”

#map(f, xs)	
#“¿En qué se convierte cada elemento?”

#sorted(xs, key=...)	
#“¿Cuál es el criterio de orden?”

La realidad es que map() puede transformar un elemento en cualquier tipo de dato.

Por ejemplo:

Número → Número

list(map(lambda x: x * 2, [1, 2, 3]))

Resultado:

[2, 4, 6]

Número → Booleano

list(map(lambda x: x > 2, [1, 2, 3]))

Resultado:

[False, False, True]

Texto → Número

list(map(len, ["Ana", "Luis", "Carlos"]))

Resultado:

[3, 4, 6]

Número → Texto

list(map(str, [1, 2, 3]))

Resultado:

["1", "2", "3"]

Por eso una forma más precisa de definir map() sería:

Aplica una función a cada elemento de un iterable y devuelve los resultados.

No importa si esos resultados son:

números,
textos,
booleanos,
fechas,
objetos,
diccionarios.

Lo que devuelva la función será lo que aparezca en la nueva lista.
