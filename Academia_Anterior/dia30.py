#Día 30 – Iterables e Iteradores

#1 ¿Qué es un iterable?
#Un iterable es cualquier objeto que puede recorrerse elemento por elemento.
#Ejemplos:
'''
lista = [10, 20, 30]
tupla = (1, 2, 3)
texto = "Python"

#Todos son iterables.
#Puedes recorrerlos con for:

for letra in "Python":
    print(letra)

for n in lista:
    print(n)

for i in tupla:
    print(i)

#2. ¿Qué es un iterador?
#Un iterador es el objeto que realmente entrega los elementos uno a uno.
#Se obtiene con:   iter()
#Ejemplo:

numeros = [10, 20, 30]

iterador = iter(numeros)

print(next(iterador))
print(next(iterador))
print(next(iterador))

#3. ¿Qué ocurre si se acaba?
#Si pedimos otro elemento:    print(next(iterador))
#Python genera:  StopIteration
#porque ya no quedan elementos.

#4. El for usa iteradores internamente
#Cuando escribes:

for numero in [1, 2, 3]:
    print(numero)

#Python hace algo parecido a:

iterador = iter([1, 2, 3])

while True:
    try:
        numero = next(iterador)
        print(numero)
    except StopIteration:
        break

#Ejercicio 1
#Analiza la salida:

frutas = ["manzana", "pera", "uva"]

it = iter(frutas)

print(next(it))
print(next(it))

# se imprimen los dos primeros elementos de la lista "manzana" y "pera"

#Ejercicio 2
#Completa el código para obtener cada número usando next():

numeros = [5, 10, 15]

it = iter(numeros)

print(next(it))
print(next(it))
print(next(it))

# Completa aquí

#Salida esperada: 5 10 15

#Mini reto
#Crea un iterable:

nombres = ["Ana", "Luis", "Pedro", "Marta"]

#Obtén manualmente los cuatro nombres usando:   iter()   next()  sin utilizar for.

iterable = iter(nombres)

print(next(iterable))
print(next(iterable))
print(next(iterable))
print(next(iterable))
#print(next(iterable)) probando StopIteration!!!
'''