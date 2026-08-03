#Qué es un generador?
#Un generador es una función especial que devuelve valores uno a uno en lugar de 
# devolverlos todos al mismo tiempo.
#En vez de usar return, utiliza yield.
'''
def contar():
    yield 1
    yield 2
    yield 3

numeros = contar()

print(next(numeros))
print(next(numeros))
print(next(numeros))

#Diferencia entre return y yield
#Con return

def numeros():
    return [1, 2, 3]

#Devuelve toda la lista de una vez.

#Con yield
def numeros():
    yield 1
    yield 2
    yield 3

#Devuelve cada elemento cuando se necesita.
#Esto ahorra memoria cuando se manejan muchos datos.

#Generador con bucle
def contar_hasta(n):
    for i in range(1, n + 1):
        yield i

for numero in contar_hasta(5):
    print(numero)


#Ejercicio 1
#Crea un generador que produzca los números:  10  20  30  40  50 usando yield.

def contar():
    yield 10
    yield 20
    yield 30
    yield 40
    yield 50

numeros = contar()

print(next(numeros))
print(next(numeros))
print(next(numeros))
print(next(numeros))
print(next(numeros))

# Se puede usar cuando los numeros usan un patron
def contar():
    for numero in range(10, 51, 10):
        yield numero

for numero in contar():
    print(numero)

#Ejercicio 2
#Crea una función generadora llamada: cuadrados(n)  
# que produzca los cuadrados desde 1 hasta n.
#Ejemplo:
#for numero in cuadrados(5):
#    print(numero)
#Salida:  1  4  9  16  25

def cuadrados():
    for numero in range(1, 6, 1):
        yield numero * numero

for numero in cuadrados():
    print(numero)

#mismo ejercicio pero mas flexible

def cuadrados(n):
    for numero in range(1, n + 1):
        yield numero * numero

for numero in cuadrados(5):
    print(numero)
'''
#Mini reto
#Ahora intenta resolver:
# Crea un generador que produzca únicamente
# los números pares entre 2 y 20.
#Salida esperada:2 4 6 8 10 12 14 16 18 20

def numeros(n):
    for numero in range(1, n + 1):
        yield numero * 2

for numero in numeros(10):
    print(numero)

#Una alternativa más directa
#También podrías generar los pares usando range() con salto de 2:

def numeros_pares():
    for numero in range(2, 21, 2):
        yield numero

#o incluso:

def numeros_pares(n):
    for numero in range(2, n + 1, 2):
        yield numero