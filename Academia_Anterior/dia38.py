#Día 38 — Enumerate y Any / All
#Estos tres elementos aparecen constantemente en proyectos reales, entrevistas y 
# código backend.

#Parte 1: enumerate()
#Permite obtener:  índice   valor  al mismo tiempo.

#Sin enumerate():
'''
frutas = ["manzana", "pera", "uva"]

for i in range(len(frutas)):
    print(i, frutas[i])

#Con enumerate():

frutas = ["manzana", "pera", "uva"]

for indice, fruta in enumerate(frutas):
    print(indice, fruta)

#Empezando desde otro número
frutas = ["manzana", "pera", "uva"]

for numero, fruta in enumerate(frutas, start=1):
    print(numero, fruta)


#Parte 2: any()
#Responde: ¿Existe AL MENOS un elemento verdadero?

valores = [False, False, True]

print(any(valores))

#Ejemplo: 
 
numeros = [1, 3, 5, 8]

print(any(n % 2 == 0 for n in numeros))

#Ejemplo:

numeros = [1, 3, 5]

print(any(n % 2 == 0 for n in numeros))

#Parte 3: all()
#Responde: ¿Todos los elementos son verdaderos?
#Ejemplo:

valores = [True, True, False]

print(all(valores))

#Ejemplo:

numeros = [2, 4, 6, 8]

print(all(n % 2 == 0 for n in numeros))

#Ejemplo:

numeros = [2, 4, 5, 8]

print(all(n % 2 == 0 for n in numeros))

#  ??????????????  Comparación mental rápida ???????????

#any(...)  Significa:   ¿Existe al menos uno?

#all(...)   Significa:   ¿Todos cumplen?

# ????????????????????????????????????????????????????????
'''
#Ejercicios de análisis (sin ejecutar)
#Ejercicio 1

nombres = ["Ana", "Luis", "Carlos"]

for i, nombre in enumerate(nombres):
    print(i, nombre)

#¿Qué imprime?  >>> Imprime
# 0 Ana
# 1 Luis
# 2 Carlos

#Ejercicio 2

numeros = [1, 3, 5, 8]

resultado = any(n > 7 for n in numeros)

print(resultado)

#¿Qué imprime?   >>> Imprime True

#Ejercicio 3

numeros = [2, 4, 6]

resultado = all(n % 2 == 0 for n in numeros)

print(resultado)

#¿Qué imprime?  >>> Imprime  True

#Ejercicio 4

numeros = [10, 20, 30]

for posicion, valor in enumerate(numeros, start=1):
    print(posicion, valor)

#¿Qué imprime?  >>> Imprime  
# 1 10
# 2 20
# 3 30

#Mini reto extra (nivel entrevista)
#Sin ejecutar código:

palabras = ["python", "java", "go"]

resultado = all(
    len(palabra) >= 2
    for palabra in palabras
)

print(resultado)

#¿Qué imprime y por qué?  >>> Imprime True. Por que pregunta si la lista cumple con la
#condicion de que la longitud de los elementos sea mayor o igual a dos, todas las 
#palabras lo cumplen por lo tanto se cumple la condicion y entonces imprime True.