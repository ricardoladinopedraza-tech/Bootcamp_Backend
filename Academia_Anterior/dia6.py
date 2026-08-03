'''
#Listas

numeros = [1, 2, 3, 4, 5]
nombres = ["Ana", "Luis", "Carlos"]

print(nombres[0])
print(nombres[1])

nombres[1] = "Pedro"
print(nombres)

#agregar elementos a una lista
nombres.append("Sofia")
print(nombres)


#Eliminar elementos de una lista
nombres.remove("Ana")
print(nombres)

for nombre in nombres:
    print(nombre)

print(len(nombres))


#Ejericios basicos
#1.
lista = [2, 3, 4, 5, 6]
print(lista[0], lista[4])

#2.
nombres = ["Ricardo", "Johana", "Jose", "Pipe", "Maria"]
print(nombres)
nombres.append("Sixto")
print(nombres)
nombres.remove("Maria")
print(nombres)


#3.
Estudiantes = []
for n in range(3):
    nombre = input(f"Digite un nombre {n+1}: ")
    Estudiantes.append(nombre)

print(Estudiantes)

for n, nombre in enumerate(Estudiantes):
    print(f"{n}: {nombre}")

#Teoria de listas

numeros = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90]

print(numeros[0])   # 10 #imprime el primero de la lista
print(numeros[-1])  # 40 (último) #imprime el ultimo de la lista

numeros = [5, 6, 7, 8, 9, 4, 3, 2, 1]

print(numeros[0:4])   # imprime el desde el item cero hasta el item (4-1)
print(numeros[:4])    # imprime los tres primeros, o los n primeros
print(numeros[::2])   # imprime los items de dos en dos desde el 0
print(numeros[::3])   # imprime de tres en tres desde item 0


lista = [5, 6, 7, 8, 9, 4, 3, 2, 1]

lista.append(4)        # añade al final
print(lista)
lista.insert(1, 99)    # inserta en posición
print(lista)
lista.remove(2)        # elimina valor
print(lista)
lista.pop()            # elimina último
print(lista)
lista.sort()           # ordena
print(lista)
lista.reverse()        # invierte
print(lista)

for i in range(len(lista)): # Recorre la lista
    print(i, lista[i])

print(len(lista)) # imprime la cantidad de items de la lista

Lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

cuadrados = [x**2 for x in range(10)] #imprime los cuadrados de los items del rango
print(cuadrados)

pares = [x for x in range(10) if x % 2 == 0] #imprime los items pares de la lista
print(pares)

impares = [x for x in range(10) if x % 2 == 1] #imprime los items impares de la lista
print(impares)


# .join()

palabras = ["Hola", "mundo"]
print(palabras)

texto = " ".join(palabras)
print(texto)  # "Hola mundo"

palabra = ["Hola", "mundo", "Python"]
print(palabra)
frase = " ".join(palabra) # Une con un espacio
print(frase)  # Resultado: "Hola mundo Python"

guion = "-".join(palabra) # Une con guiones
print(guion)  # Resultado: "Hola-mundo-Python"



a = [1,2,3, 7]
b = a 
print(a)
print(b)

b.append(4)

print(a)
print(b)

b = a.copy()
print(b)

c = max(a)
print(c)

print(max(a))


lista = ["hola", "python", "lista"]

guion = "-".join(lista) 
print(guion) 


# encontrar el numero mayor de una lista sin max()
lista = [3, 8, 2, 10, 5]

mayor = lista[0]

print(mayor)

for numero in lista:
    if numero > mayor:
        mayor = numero

print(mayor)
'''

# encontrar el numero menor sin usar min()

lista = [3, 8, 2, 10, 5]

menor = lista[0]

print(menor)

for numero in lista:
    if numero < menor:
        menor = numero

print(menor)