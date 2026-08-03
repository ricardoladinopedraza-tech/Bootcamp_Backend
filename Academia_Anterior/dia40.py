#Día 40 — *args y **kwargs
#Estos conceptos aparecen con frecuencia en librerías reales, frameworks como FastAPI 
# y código profesional.

#1. ¿Qué es *args?
#Permite recibir una cantidad variable de argumentos posicionales.
#Python guarda los valores en una tupla.
'''
def sumar(*args):
    print(args)

sumar(1, 2, 3)

#Ejemplo práctico
def sumar(*args):
    total = sum(args)
    return total

print(sumar(10, 20))
print(sumar(10, 20, 30))

#2. ¿Qué es **kwargs?
#Permite recibir una cantidad variable de argumentos con nombre.
#Python los guarda en un diccionario.

def mostrar(**kwargs):
    print(kwargs)

mostrar(nombre="Ricardo", edad=30)

#Ejemplo práctico
def mostrar_usuario(**kwargs):
    for clave, valor in kwargs.items():
        print(clave, valor)

mostrar_usuario(
    nombre="Ana",
    ciudad="Bogotá"
)

#3. Combinando parámetros normales y *args
#¡Cerramos con un ejercicio excelente para consolidar cómo se reparten los datos! 
# Aquí estás mezclando un parámetro fijo (nombre) con un parámetro dinámico (*args).
def saludar(nombre, *args):
    print(nombre)
    print(args)

saludar(
    "Juan",
    "Python",
    "SQL",
    "Git"
)

def saludo(caca, *args):
    print(caca)
    print(args)

saludar(
    "Python",
    "SQL",
    "Git", 
    "Juan"
)

#4. Combinando parámetros normales y **kwargs
def usuario(nombre, **kwargs):
    print(nombre)
    print(kwargs)

usuario(
    "Carlos",
    edad=25,
    ciudad="Medellín"
)
'''
#5. Orden correcto
#Cuando aparecen juntos:

def ejemplo(
    a,
    *args,
    **kwargs
):
    pass

# Siempre:  Parámetros normales  *args  **kwargs

#Ejercicios de análisis (sin ejecutar)
#Ejercicio 1
def mostrar(*args):
    print(args)

mostrar(1, 2, 3)

#¿Qué imprime?  >>> Imprime tupla (1, 2, 3)

#Ejercicio 2
def datos(**kwargs):
    print(kwargs)

datos(nombre="Ana", edad=20)

#¿Qué imprime?  >>> {'nombre': 'Ana', 'edad': 20}

#Ejercicio 3
def ejemplo(a, *args):
    print(a)
    print(args)

ejemplo(10, 20, 30)

#¿Qué imprime?  >>> Imrime 
#  10
# (20, 30)

#Ejercicio 4
def usuario(nombre, **kwargs):
    print(nombre)
    print(kwargs)

usuario(
    "Pedro",
    ciudad="Cali"
)

#¿Qué imprime?  >>> Imprime  
# Pedro
# {'ciudad': 'Cali'}

#Mini reto extra (nivel entrevista)
#Sin ejecutar:

def suma(*args):
    return sum(args)

resultado = suma(1, 2, 3, 4)

print(resultado)

#¿Qué imprime y por qué?  >>> Imprime 10