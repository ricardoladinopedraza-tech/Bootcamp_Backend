###### TUPLAS

#¿Qué es una tupla?
#Una tupla es una colección de datos, parecida a una lista.
#La diferencia principal:
#Lista	                Tupla
#Se puede modificar	    NO se puede modificar
#Usa []	                Usa ()
'''
#Crear una tupla
numeros = (1, 2, 3, 4)

print(numeros)

#Acceder a elementos

frutas = ("manzana", "pera", "uva")

print(frutas[0])
print(frutas[1])

#Las tuplas NO se pueden modificar, lo siguiente sera error

frutas = ("manzana", "pera", "uva")

frutas[0] = "kiwi"

#Recorrer una tupla con for
colores = ("rojo", "verde", "azul")

for color in colores:
    print(color)

#Saber cuántos elementos tiene
numeros = (10, 20, 30, 40)

print(len(numeros))

#Buscar elementos

paises = ("Colombia", "Perú", "México")

print("Colombia" in paises) #imprime True si elemento esta en tupla
print("Chile" in paises) #imprime False si elemento NO esta en tupla

#Contar elementos repetidos
numeros = (1, 2, 2, 3, 2)

print(numeros.count(2))

#Encontrar posición

frutas = ("manzana", "pera", "uva")

print(frutas.index("uva"))

#Diferencia entre lista y tupla

#lista = [1, 2, 3]
#tupla = (1, 2, 3)

#Cuándo usar tuplas?
#Cuando los datos:
#    no deben cambiar
#    son fijos
#    quieres proteger la información
#Ejemplos:
#    coordenadas
#    meses del año
#    días de la semana

dias = (
    "lunes",
    "martes",
    "miércoles",
    "jueves",
    "viernes"
)

#Tupla de un solo elemento

#tupla = (5,) # sin la coma solo sera un numero
tupla = (5)
print(tupla)

#Mini practica

#Ejercicio 1
#Muestra:

#el primer número
#el último número

numeros = (5, 10, 15, 20)

print(numeros[0])
print(numeros[3])
#print(numeros[-1])  #TAmbien busca el ultimo elemento de la tupla

#Ejercicio 2
#Recorre esta tupla con for
animales = ("perro", "gato", "conejo")

for animal in animales:
    print(animal)

#Ejercicio 3

#Verifica si "Python" está en:
lenguajes = ("Java", "Python", "C++")
print("Python" in lenguajes)

#Mini reto 🚀
#Crea una tupla con 5 ciudades.

#Luego:

#Mostrar todas las ciudades
#Mostrar cuántas ciudades hay
#Preguntar una ciudad al usuario
#Indicar si existe o no en la tupla

ciudades = ("Sogamoso", "Paipa", "Duitama", "Tunja", "Bogota")

print(ciudades)

print(len(ciudades))

ciudad = str(input("Digite una ciudad para buscar: "))

print(ciudad in ciudades)

#Mejora de ultima parte
#if ciudad in ciudades:
#    print("La ciudad existe")
#else:
#    print("La ciudad no existe")
'''
