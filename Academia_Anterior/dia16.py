### return y fuciones

#Función SIN return
'''
def sumar():
    resultado = 5 + 3
    print(resultado)

sumar()

#Función CON return

def sumar():
    resultado = 5 + 3
    return resultado

dato = sumar()

print(dato)

#Ejemplo

def multiplicar(a, b):
    return a * b

resultado = multiplicar(4, 5)

print(resultado)

#print() NO es igual a return
#Con print
def prueba():
    print(10)

dato = prueba()

print(dato) #imprime none, print solo muestra

#Con return
def prueba():
    return 10

dato = prueba()

print(dato) #imprime 10, por que return devuelve valor, en este caso 10

#Varias operaciones

def calcular(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b 

    return suma, resta, multiplicacion, division

resultado = calcular(10, 5)

print(resultado)

#Guardar múltiples valores

def calcular(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b

    return suma, resta, multiplicacion, division

s, r, m, d = calcular(10, 5)

print("Suma:", s)
print("Resta:", r)
print("Multiplicaion:", m)
print("Division:", d)

#Funciones que validan datos

def es_mayor(edad):
    if edad >= 18:
        return True
    else:
        return False

print(es_mayor(20))
print(es_mayor(15))

#Forma simplificada

def es_mayor(edad):
    return edad >= 18

print(es_mayor(20))

#Scope (variables locales)

def prueba():
    mensaje = "Hola"

print(mensaje)
##  NameError    Porque mensaje solo existe dentro de la función.


# Correccion, usar return
def prueba():
    return "Hola"

print(prueba())


#Mini práctica 🧠
#Ejercicio 1
#  Crea una función:   cuadrado(numero)    Debe retornar el cuadrado del número.
#Ejemplo:      print(cuadrado(4))    Resultado:   16

def cuadrado(numero):
    return numero * numero

print("Resultado:", cuadrado(4))

#Ejercicio 2
#Crea una función:   saludo(nombre)     Debe retornar:  Hola Ricardo

def saludo(nombre):
    print("Hola", nombre)


saludo("Ricardo")

************ Correccio, debe retornar, usar return *****************
def saludo(nombre):
    return "Hola " + nombre

print(saludo("Ricardo"))


#Ejercicio 3
#Crea una función que:   reciba 2 números   retorne:   suma    multiplicación

def operacion(a, b):
    suma = a + b
    multiplicacion = a * b
    return suma, multiplicacion

s, m = operacion(5, 10)
print("suma:", s)
print("multiplicacion:", m)

#Mini reto 🔥
#Haz un programa que:  Cree una función llamada calcular_descuento
#Reciba:   precio    descuento   Retorne el precio final

def calcular_descuento(precio, descuento):
    return precio - ((precio * descuento) / 100)
    
precio_final = calcular_descuento(1000, 20) 
print(precio_final)
'''

def calcular()
    suma = 3 = 4