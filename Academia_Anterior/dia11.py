###### Diccionarios
'''
#CRear un diccionario
persona = {
    "nombre": "Ana",
    "edad": 25,
    "pais": "Colombia"
}

print(persona)

#Acceder a un valor
persona = {
    "nombre": "Ana",
    "edad": 25
}

print(persona["nombre"])
print(persona["edad"])

#Modificar valores
persona = {
    "nombre": "Ana",
    "edad": 25
}

persona["edad"] = 26

print(persona)

#Agregar nuevos datos
persona = {
    "nombre": "Ana"
}

persona["ciudad"] = "Bogotá"

print(persona)

#eliminar datos
persona = {
    "nombre": "Ana",
    "edad": 25
}
print(persona)

del persona["edad"]

print(persona)

#Recorrer un diccionario  ++++ solo claves
persona = {
    "nombre": "Ana",
    "edad": 25
}
print(persona)

for dato in persona:
    print(dato)

#Recorrer un diccionario +++++++ Clave y datos
persona = {
    "nombre": "Ana",
    "edad": 25
}

for clave, valor in persona.items():
    print(clave, valor)

#Ejemplo
producto = {
    "nombre": "Mouse",
    "precio": 50000,
    "cantidad": 3
}

print("Producto:", producto["nombre"])
print("Precio:", producto["precio"])
print("Cantidad:", producto["cantidad"])


#Ejercicio 1
#Crea un diccionario llamado carro con:
#marca
#modelo
#año
#y luego imprime la marca.

carro = {
    "marca": "Kia",
    "modelo": "Sportage",
    "año": 1994
}

print("Marca: ", carro["marca"])

#Ejercicio 2 
#Agrega una nueva clave llamada "curso".
estudiante = {
    "nombre": "Carlos",
    "nota": 4.5
}
print(estudiante)

estudiante["curso"] = "cuarto"

print(estudiante)

#Ejercicio 3
#Recorre este diccionario e imprime clave y valor:

animal = {
    "tipo": "Perro",
    "nombre": "Max",
    "edad": 5
}

for clave, valor in animal.items():
    print(clave, valor)

#Mini reto del Día 11 🚀
#Crea un programa que:
#Cree un diccionario de un producto
#Pida: nombre   precio   cantidad
#Guarde todo en el diccionario

producto = {
    "nombre": str(input("Digite producto: ")),
    "precio": float(input("Digite precio: ")),
    "cantidad": int(input("Digite cantidad: "))
}

print(producto)

for clave, valor in producto.items():
    print(clave, ":", valor)


#version mejorada de mini reto

producto = {
    "nombre": str(input("Digite producto: ")),
    "precio": float(input("Digite precio: ")),
    "cantidad": int(input("Digite cantidad: "))
}

print("\n--- PRODUCTO ---")

for clave, valor in producto.items():
    print(clave.capitalize(), ":", valor) #coloca en mayusculas la primera letra de la clave
'''
#Ejercicio Extra — Diccionarios 🐍
#Vamos a mezclar varias cosas que ya sabes 😄
#Objetivo
#Crear un sistema pequeño de inventario.
#Instrucciones
#Crear un diccionario vacío llamado producto
#Pedir:
#nombre
#precio
#cantidad
#Guardar los datos
#Calcular el valor total:
#total = precio * cantidad
#Guardar también el total dentro del diccionario
#Imprimir todo el diccionario
#Recorrerlo con for
#Resultado esperado (ejemplo)
#Nombre : Arroz
#Precio : 3000
#Cantidad : 4
#Total : 12000
#Pista 🔍
#Puedes hacerlo paso a paso:
#producto = {}
#Luego:
#producto["nombre"] = ...

#Y al final:
#producto["total"] = producto["precio"] * producto["cantidad"]
#Inténtalo tú solo primero 💪

producto = {}

nombre = str(input("Digite producto: "))
precio = float(input("Digite precio: "))
cantidad = int(input("Digite cantidad: "))
impuesto = float(input("Digite valor de IVA: "))
impuesto = impuesto / 100

producto["nombre"] = nombre
producto["precio"] = precio
producto["cantidad"] = cantidad

total = precio * cantidad
#producto["total"] = producto["precio"] * producto["cantidad"] #tambien se puede asi
producto["total"] = total

iva = total * impuesto
#producto["iva"] = iva
producto["iva"] = round(iva, 2) #Evita numeros largos 3,69999999999999

total_con_iva = total + iva
#producto["total con IVA"] = total_con_iva  
producto["total con IVA"] = round(total_con_iva, 2)

print("\n--- PRODUCTO ---")

for clave, valor in producto.items():
    print(clave.capitalize(), ":", valor)

