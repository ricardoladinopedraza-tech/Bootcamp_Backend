########## sets / Conjuntos

#Crear un set
'''
numeros = {1, 2, 3, 4}

print(numeros)

#diferencia entre set y lista
#lista
lista = [1, 1, 2, 2, 3]
print(lista)
#Set
conjunto = {1, 1, 2, 2, 3}
print(conjunto) #elimina los elementos repetidos

#Crear set desde una lista    **** se usa para eliminar duplicados*******

numeros = [1, 1, 2, 3, 3, 4]
print(numeros)
set_numeros = set(numeros)
print(set_numeros)

# agregar elementos 
frutas = {"manzana", "pera"}
print(frutas)
frutas.add("uva")
print(frutas)

#Eliminar elementos 
# Eliminar con *** remove() ******
frutas = {"manzana", "pera", "uva"}
frutas.remove("pera") #***** Si no existe el elemento produce error ********
print(frutas)

#Eliminar con discard()
frutas = {"manzana", "pera"}
frutas.discard("banana") #***** no genera error ******
print(frutas)

#recorrer un set
numeros = {1, 2, 3, 4, 5, 6, 7, 5, 3, 1}

for numero in numeros:
    print(numero)

#Verificar si existe un elemento en el set

frutas = {"manzana", "pera", "uva"}

if "pera" in frutas:
    print("Sí existe")

#Union de sets
a = {1, 2, 3}
b = {3, 4, 5}

resultado = a.union(b)

print(resultado)

#interseccion

a = {1, 2, 3}
b = {2, 3, 4}

print(a.intersection(b))

#diferencia, elementos  que estan en uno pero no en el otro

a = {1, 2, 3}
b = {2, 3, 4}

print(a.difference(b))

# Mini práctica

#Ejercicio 1
#Crear un set con nombres de frutas.
#Agregar una fruta nueva.
#Mostrar el resultado.

frutas = {"manzana", "banano", "fresa", "pera"}
print(frutas)
frutas.add("uva")
print(frutas)

#Ejercicio 2
#Pedir 5 números al usuario y guardarlos en un set.
#Mostrar el set final.

numeros = set() #se debe usar esta sintaxis para crear un set vacio con {} se crea un diccionario
for i in range(5):
    numero = int(input(f"Digite un numero {i+1}: " ))
    numeros.add(numero)

print(numeros)

#Ejercicio 3
#Crear dos sets y mostrar:
#unión
#intersección
#diferencia

a = {1, 2, 3, 4, 5, 6, 7}
b = {4, 5, 6, 1, 8, 9, 10}
resultado = a.union(b)
print(resultado)

resultado_1 = a.intersection(b)
print(resultado_1)

resultado_2 = a.difference(b)
print(resultado_2)
'''
#Mini reto del Día 13 🧠
#Haz un programa que:
#✅ Pida nombres de estudiantes
#✅ El usuario escribe "fin" para terminar
#✅ Guardar nombres en un set
#✅ Mostrar:
#cantidad total de estudiantes únicos
#lista final sin repetidos

estudiantes = set()

while True:
    nombre = input("Digita un nombre (o 'fin' para salir): ").lower() 
    #nombre = input("Nombre: ").lower() #Evita que Ana y ana se tomen como diferentes*******

    if nombre == "fin":
        break

    estudiantes.add(nombre)

print("Total unicos:", len(estudiantes))
print(estudiantes)
