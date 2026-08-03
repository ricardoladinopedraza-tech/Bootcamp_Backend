#### Diccionarios ###
'''
persona = {"nombre":"Ricardo", "edad": 30, "ciudad": "Bogota"}

print(persona)

print(persona["nombre"])
print(persona["edad"])

#modificar valores

persona["edad"] = 48
print(persona)

# aregar valores
persona["carrera"] = "ingenieria"
print(persona)

#Eliminar datos
del persona["ciudad"]
print(persona)

#recorrer diccioinarios con for
for clave, valor in persona.items():
    print(clave, ":", valor) #imprime valores por separado

#ejercicios
#1.
carro = {"marca":"Kia", "modelo":"Sportage", "a;o":1994}
print(carro)

for clave, valor in carro.items():
    print(clave, "=", valor)

#2. 
usuario = {"nombre":"Ricardo Ladino", "edad":47, "correo":"richila@gmail.com"}
print(usuario)

usuario["edad"] = 48
usuario["telefono"] = 3133122124

for clave, valor in usuario.items():
    print(clave, "=", valor)

#minireto
producto = {"Nombre":"Laptop", "Precio":100, "Cantidad":30}

total = producto["Precio"] * producto["Cantidad"]
print("Producto :", producto["Nombre"])
print("Total inventario :", total)


#Reto extra
personas = [{"nombre":"Ana", "edad":20}, {"nombre":"Luis", "edad": 25}]

for i in personas:
    print(i)
'''
#mini reto acicional
productos = [{"nombre":"Laptop", "precio":100, "cantidad":30},
             {"nombre":"Mouse", "precio":50, "cantidad":10}, 
             {"nombre":"Teclado", "precio": 90, "cantidad": 10}]

inventario_total = 0

for i in productos:
    total = i["precio"] * i["cantidad"]
    inventario_total += total
    print(f"Producto: {i["nombre"]}")
    print("Total:", total)

print("Inventario total:", inventario_total)
