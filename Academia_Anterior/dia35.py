#Día 35 – Set Comprehensions y repaso de Comprehensions
#Hoy veremos el tercer tipo de comprehension:

#1. Set Comprehension
#Así como existe:

# Lista
#[n for n in numeros]

# Diccionario
#{n: n**2 for n in numeros}

#También existe:

# Conjunto (set)
#{n for n in numeros}

#>>>>>>>>>>>>>>> Los sets eliminan automáticamente duplicados. <<<<<<<<<<<<<<
'''
#Ejemplo:

numeros = [1, 2, 2, 3, 3, 3, 4]

resultado = {n for n in numeros}

print(resultado)

#2. Transformando valores

numeros = [1, 2, 3, 4]

cuadrados = {n**2 for n in numeros}

print(cuadrados)

#3. Con condición

numeros = [1, 2, 3, 4, 5, 6]

pares = {n for n in numeros if n % 2 == 0}

print(pares)

# >>>>>>>>>>>>> Comparación rápida  <<<<<<<<<<<<<
#Lista:  [n for n in numeros]
#Resultado:    [1, 2, 3]

#Set:   {n for n in numeros}
#Resultado:   {1, 2, 3}

#Diccionario:   {n: n**2 for n in numeros}
#Resultado:  {1:1, 2:4, 3:9}

#Ejercicio 1
#Sin ejecutar código:

numeros = [1, 2, 2, 3, 3, 4]

resultado = {n for n in numeros}

print(resultado)

#¿Qué imprime?  >>> Imprime {1, 2, 3, 4}

#Ejercicio 2
#Sin ejecutar código:

numeros = [1, 2, 3, 4, 5]

resultado = {n * 10 for n in numeros if n > 3}

print(resultado)

#¿Qué imprime?  >>> Imprime  {40, 50}

#Ejercicio 3
#Analiza cuidadosamente:

palabras = ["python", "java", "python", "go"]

resultado = {palabra.upper() for palabra in palabras}

print(resultado)

#¿Qué imprime?  >>> Imprime  {'PYTHON', 'JAVA', 'GO'}

#Mini reto entrevista
#Sin ejecutar:

numeros = [1, 2, 3, 4, 5]

resultado = {
    n**2
    for n in numeros
    if n % 2 != 0
}

print(resultado)

#¿Qué elementos pasan el filtro?  >>> Pasan {1, 3, 5}, por ser impares
#¿Qué transformación se aplica?  >>> Se elevan al cuadrado
#¿Qué imprime finalmente?  >>> Imprime {1, 9, 25}

#Pregunta conceptual
#Responde con tus palabras:
#¿Cuándo usarías un set comprehension en lugar de una list comprehension?
#Ok, Usaria un set comprehesion para eliminar los elementos repetidos de una lista
#que por definicion es lo aporta los conjuntos, de momento no identifico otra ventaja
'''
#Mini reto extra (nivel entrevista)
#Sin ejecutar código:

numeros = [1, 2, 2, 3, 4, 4]

resultado = {
    n * 2
    for n in numeros
    if n >= 2
}

print(resultado)
#¿Qué elementos pasan el filtro?  >> Pasan [2, 2, 3, 4, 4]
#¿Qué transformación se aplica?  >> se multiplica por 2 [4, 4, 6, 8, 8]
#¿Qué imprime finalmente? >> Finalmente se imprime {4, 6, 8}

#Y una de razonamiento:

valores = [1, 1, 1, 1]

resultado = {n + 10 for n in valores}

print(resultado)

#¿Por qué el resultado tiene menos elementos que la lista original?
#La transformacion aplica la suma de 10 a los 4 elementos de la lista
#pero la aplicacion de set() elimina los elementos repetidos, por lo tanto, solo
#imprime {11}