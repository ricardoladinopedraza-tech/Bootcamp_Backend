#Bucles while + acumuladores
'''
n = 1

while n <= 5:
    print(n)
    n += 1

#####################
total = 0

for numero in [3, 5, 2]:
    total += numero

print(total)

#####################
suma = 0

while True:
    dato = input("Escribe un numero o 'salir': ")

    if dato == "salir":
        break

    suma += int(dato)

print("Total:", suma)

##################################
contador = 0

while True:
    dato = input("Numero o 'salir': ")

    if dato == "salir":
        break

    contador += 1

print("Ingresaste", contador, "numeros")

#######################################
suma = 0
cantidad = 0

while True:
    dato = input("Numero o 'salir': ")

    if dato == "salir":
        break

    numero = int(dato)

    suma += numero
    cantidad += 1

promedio = suma / cantidad

print("Promedio:", promedio)

######### Mini reto
#Haz un programa que:

#Pida nombres de productos
#Pida precios
#Se detenga cuando escriban "fin"
#Muestre:
#cuántos productos ingresaron
#suma total de precios

total = 0
cantidad = 0

while True:
    producto = input("Escriba producto (o 'fin' para salir): ")

    # salir del ciclo
    if producto == "fin":
        break

    # pedir precio
    precio = float(input("Escriba precio: "))

    # acumular total
    total += precio

    # contar productos
    cantidad += 1

print("Productos ingresados:", cantidad)
print("Suma total de precios:", total)

############## Mini reto extra
total = 0
cantidad = 0
productos = [] #crear lista


while True:
    producto = input("Escriba producto (o 'fin' para salir): ")
    
    # salir del ciclo
    if producto == "fin":
        break
    
    # pedir precio
    precio = float(input("Escriba precio: "))

    #Agregar producto a la lista
    productos.append(producto)

    # acumular total
    total += precio

    # contar productos
    cantidad += 1

#print("Los productos almacenados son: ", productos) #imprime la lista
for p in productos: #imprime producto por producto
    print(p)
print("Productos ingresados:", cantidad)
print("Suma total de precios:", total)

###### Otra version anterior
total = 0
cantidad = 0
productos = [] #crear lista


while True:
    producto = input("Escriba producto (o 'fin' para salir): ")
    
    # salir del ciclo
    if producto == "fin":
        break
    
    # pedir precio
    precio = float(input("Escriba precio: "))

    #Agregar producto a la lista
    productos.append([producto, precio]) #se agregan dos items a la lista

    # acumular total
    total += precio

    # contar productos
    cantidad += 1

#print("Los productos almacenados son: ", productos) #imprime la lista
for item in productos: #imprime producto por producto de la lista
    print(item[0], "-", "$",item[1])
    #print(f"{item[0]} - ${item[1]}") #mejora en la impresion
    
print("Productos ingresados:", cantidad)
print("Suma total de precios:", total)
'''
####### Version antterior mostrando el numero de item
total = 0
cantidad = 0
n = 1
productos = [] #crear lista


while True:
    producto = input("Escriba producto (o 'fin' para salir): ")
    
    # salir del ciclo
    if producto == "fin":
        break
    
    # pedir precio
    precio = float(input("Escriba precio: "))

    #Agregar producto a la lista
    productos.append([producto, precio]) #se agregan dos items a la lista

    # acumular total
    total += precio

    # contar productos
    cantidad += 1

for item in productos: #para imprimir producto por producto con numero de item
    print(n, "-", item[0], "-", "$", item[1])
    n += 1
   
print("Productos ingresados:", cantidad)
print("Suma total de precios:", total)

