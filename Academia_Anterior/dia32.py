#Día 32 – Funciones map(), filter() y reduce()
#Estas tres herramientas aparecen con frecuencia en código
#profesional y suelen combinarse con lambda.

#1. map()
#Permite aplicar una función a cada elemento de un iterable.
#Ejemplo
'''
numeros = [1, 2, 3, 4]

resultado = list(map(lambda x: x * 2, numeros))

print(resultado)

#Salida: [2, 4, 6, 8]   Cada número fue multiplicado por 2

#2. filter()
#Permite conservar únicamente los elementos que cumplan una condición.
#Ejemplo

numeros = [1, 2, 3, 4, 5, 6]

pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)

#Salida:   [2, 4, 6]  Solo quedaron los números pares.

#3. reduce()
#Reduce una colección a un único valor.
#Se importa desde:  from functools import reduce
#Para utilizarla, debes importarla desde el módulo oficial functools
#Sintaxis:reduce(función, iterable, [valor_inicial])
#Ejemplo

from functools import reduce

numeros = [1, 2, 3, 4]

resultado = reduce(lambda a, b: a + b, numeros)

print(resultado)

# Salida:  10
#Proceso: 1 + 2 = 3   3 + 3 = 6   6 + 4 = 10

#Comparación rápida
#  Función      	Devuelve
#  map()	        Todos los elementos transformados
#  filter()	        Solo los que cumplen una condición
#  reduce()	        Un único resultado

#Ejercicio 1
#¿Qué imprime?

numeros = [1, 2, 3]

resultado = list(map(lambda x: x + 5, numeros))

print(resultado) #imprime lista con [6, 7, 8]

#Ejercicio 2
#¿Qué imprime?

numeros = [10, 15, 20, 25]

resultado = list(filter(lambda x: x > 18, numeros))

print(resultado) #imprime lista con [20, 25]

#Ejercicio 3
#Completa el código para obtener:  [1, 4, 9, 16]

numeros = [1, 2, 3, 4]

resultado = list(map(lambda x: x ** 2, numeros))

print(resultado)
'''
#Ejercicio 4
#Completa el código para obtener:  [3, 6, 9]

numeros = [1, 2, 3, 4, 5, 6]

resultado = list(filter(lambda x: x % 3 == 0, map(lambda x: x + 5, numeros)))

print(resultado)
'''
#Ejercicio 5
#¿Qué imprime?

from functools import reduce

numeros = [2, 3, 4]

resultado = reduce(lambda a, b: a * b, numeros)

print(resultado) #Imprime [24]

#Ejercicio 6 (Nivel entrevista junior)
#Sin ejecutar el código, indica la salida:

numeros = [1, 2, 3, 4, 5]

resultado = list(filter(lambda x: x % 2 == 1, map(lambda x: x * 2, numeros)))

print(resultado) # imprime lista vacia, no hay elementos impares despues del map()
'''