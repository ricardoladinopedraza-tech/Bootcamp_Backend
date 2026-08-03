#Funciones
'''
nombre = "Ricardo"
print(nombre)

def saludo():
    return "hola"
    #print("Hola")

print(saludo())
saludo()


def saludar():
    print("Hola Ricardo")

saludar()


#Ejemplo 1
def saludo():
    print("Bienvenido al sistema")

saludo()

def saludo1():
    return "Bienvenido al sistema Ricardo"

saludo1()
print(saludo1())


#Ejemplo2
numero = int(input("Digita un numero: "))

def doble(numero):
    return numero * 2

print(doble(numero))



#Ejemplo3
edad = int(input("Digita edad: "))

def es_mayor(edad):
    if edad >= 18:
        print("Mayor de edad")
    else:
        print("Menor de edad")

es_mayor(edad)


#Ejemplo4

print("Vamos a calcular el area de un triangulo")

base = int(input("Digita base del triangulo: "))
altura = int(input("Digita altura del triangulo: "))

def calcular_area(base, altura):
    return base * altura / 2

print("El area del triangulo es: ", calcular_area(base, altura))
'''

#mini reto

productos = [{"nombre": "Mouse", "precio": 50, "cantidad": 5}, 
             {"nombre": "Teclado", "precio": 80, "cantidad": 3}
            ]

def calcular_total(precio, cantidad):
    return precio * cantidad

for producto in productos:

    precio = producto["precio"]
    cantidad = producto["cantidad"]

    total = calcular_total(precio, cantidad)

    print("Producto:", producto["nombre"])
    print("Total:", total)