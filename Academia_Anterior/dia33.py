#Día 33 – List Comprehensions Avanzadas

#1. Comprensión con condición
'''
numeros = [1, 2, 3, 4, 5, 6]

pares = [n for n in numeros if n % 2 == 0]

print(pares)

#2. Comprensión con transformación

palabras = ["python", "java", "go"]

mayusculas = [palabra.upper() for palabra in palabras]

print(mayusculas)

#3. Comprensión con if-else

numeros = [1, 2, 3, 4, 5]

resultado = [
    "par" if n % 2 == 0 else "impar"
    for n in numeros
]

print(resultado)

#4. Comprensión anidada
matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
]

numeros = [n for fila in matriz for n in fila]

print(numeros)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4
# List compresion basica
#as list comprehension nos permiten crear listas de elementos en una sola línea 
# de código. Por ejemplo, podemos crear una lista con los cuadrados de los primeros 
# 5 números de la siguiente forma

cuadrados = [i**2 for i in range(5)]

print(cuadrados)

#Antes de continuar, veamos la sintaxis general de las comprensiones de listas.

# lista = [expresión for elemento in iterable]

#La expresión puede ser una operación como hemos visto anteriormente i**2, 
# pero también puede ser un valor constante. El siguiente ejemplo genera una 
# lista de cinco unos.

unos = [1 for i in range(5)]

print(unos)  #[1, 1, 1, 1, 1]

#La expresión también puede ser una llamada a una función. Se podría escribir el 
# ejemplo anterior del cálculo de cuadrados de la siguiente manera.

def eleva_al_2(i):
    return i**2

cuadrados = [eleva_al_2(i) for i in range(5)]

print(cuadrados)  #[0, 1, 4, 9, 16]

lista = [10, 20, 30, 40 , 50]
nueva_lista = [i/10 for i in lista]
print(nueva_lista) #[1.0, 2.0, 3.0, 4.0, 5.0]

#Pero, ¿y si quisiéramos realizar la operación sobre el elemento sólo si una 
# determinada condición se cumple? Pues tenemos buenas noticias, porque es 
# posible añadir un condicional if. La expresión genérica sería la siguiente.

# lista = [expresión for elemento in iterable if condición]

#Por lo tanto la expresión sólo se aplicará al elemento si se cumple la condición. 
# Veamos un ejemplo con una frase, de la que queremos saber el número de erres que 
# tiene.

frase = "El perro de san roque no tiene rabo"
erres = [i for i in frase if i == 'r']
print(erres)  #['r', 'r', 'r', 'r']
print(len(erres))

#Ejercicio 1
#Analiza la salida:

numeros = [1, 2, 3, 4, 5]

resultado = [n * 2 for n in numeros]

print(resultado) 

#¿Qué imprime?   #imprime [1, 4, 6, 8, 10]

#Ejercicio 2
#Completa:   Debe producir:  [10, 20, 30]
#Código:

numeros = [1, 2, 3]

resultado = [i * 10 for i in numeros]

print(resultado)

#Ejercicio 3
#Analiza la salida:

numeros = [1, 2, 3, 4, 5, 6]

pares = [n for n in numeros if n % 2 == 0]

print(pares)

#¿Qué imprime?   imprime [2, 4, 6]

#Ejercicio 4
#Sin ejecutar:

palabras = ["python", "backend", "api"]

resultado = [p.upper() for p in palabras]

print(resultado)

#¿Qué imprime? imprime ["PYTHON", "BACKEND", "API"]
'''

