#Día 41 — Módulos y Paquetes

#¿Qué es un módulo?
#Un módulo es simplemente un archivo .py.
#Por ejemplo:

# calculadora.py
'''
def sumar(a, b):
    return a + b

#Ese archivo ya es un módulo.

#Importar un módulo

import math

print(math.sqrt(25))

#Importar funciones específicas

from math import sqrt

print(sqrt(36))

#Importar con alias

import math as m

print(m.pi)

#Crear nuestro propio módulo
#Archivo:

# operaciones.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

#Archivo principal:

import operaciones

print(
    operaciones.sumar(3, 4)
)

print(
    operaciones.restar(3, 4)
)

#>>>>>>>>>> ¿Qué es un paquete? >>>>>>>>>>>>

#Una carpeta que contiene módulos Python.
#Ejemplo:

# proyecto/

#├── main.py
#├── utilidades/
#│   ├── __init__.py
#│   ├── calculos.py
#│   └── texto.py

#¿Por qué es importante?
#Cuando construyas APIs con FastAPI, un proyecto real tendrá una estructura parecida a:

#app/
#├── main.py
#├── routes/
#├── models/
#├── database/
#└── services/

#Todo eso depende de entender módulos y paquetes.
#>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
'''
#Ejercicios de análisis (sin ejecutar)
#Ejercicio 1

import math

print(math.sqrt(49))

#¿Qué imprime?  >>> imprime 7

#Ejercicio 2

from math import pi

print(pi)

#¿Qué imprime aproximadamente?  >>> Imprime 3,14159265

#Ejercicio 3

import math as m

print(m.factorial(4))

#¿Qué imprime?  >>> Imprime 24

#Ejercicio 4
from math import sqrt

resultado = sqrt(81)

print(resultado)

#¿Qué imprime?  >>> Imprime 9

#Mini reto extra (nivel entrevista)
#Sin ejecutar:

from math import sqrt

a = sqrt(16)
b = sqrt(25)

print(a + b)

#¿Qué imprime y por qué?  >>> Imprime 9


