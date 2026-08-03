#Día 44 – JSON y consumo real de APIs

#1. ¿Qué es JSON?
#JSON significa:  JavaScript Object Notation
#Es el formato más usado para intercambiar datos entre aplicaciones.
#Ejemplo:
'''
{
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Bogotá"
}

#En Python se convierte en:

{
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Bogotá"
}

#2. Obtener JSON desde una API
#Ejemplo:

import requests

r = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

datos = r.json()

print(type(datos))

#Pregunta:

#¿Qué tipo de dato es datos?  >>> List

#3. Acceder a elementos

usuario = datos[0]

print(usuario["name"])

#Salida:

Leanne Graham


#4. Acceder a datos anidados
#Muchos JSON contienen diccionarios dentro de otros diccionarios.

#Ejemplo:

print(
    usuario["address"]["city"]
)

#Salida:

Gwenborough

#5. Recorrer datos de una API
for usuario in datos:
    print(usuario["name"])

#Salida:

Leanne Graham
Ervin Howell
...

#6. Crear una lista útil

#Extraer solamente nombres:

nombres = [
    usuario["name"]
    for usuario in datos
]

print(nombres)

#7. Filtrar información
for usuario in datos:
    if usuario["id"] > 5:
        print(usuario["name"])
'''

#Ejercicios de análisis (sin ejecutar)
#Ejercicio 1

datos = {
    "nombre": "Ana",
    "edad": 20
}

print(datos["nombre"])

#¿Qué imprime?  >>> Imprime Ana

#Ejercicio 2

datos = [
    {"nombre": "Ana"},
    {"nombre": "Luis"}
]

print(datos[0]["nombre"])

#¿Qué imprime?  >>> Imprime Ana

#Ejercicio 3

datos = {
    "usuario": {
        "nombre": "Carlos"
    }
}

print(
    datos["usuario"]["nombre"]
)

#¿Qué imprime?  >>> Imprime Carlos

#Ejercicio 4
usuarios = [
    {"nombre": "Ana"},
    {"nombre": "Luis"},
    {"nombre": "Pedro"}
]

for usuario in usuarios:
    print(usuario["nombre"])

#¿Qué imprime?  >>> Imprime
# Ana
# Luis
# Pedro

#Ejercicio 5

usuarios = [
    {"edad": 18},
    {"edad": 25},
    {"edad": 30}
]

resultado = [
    u["edad"]
    for u in usuarios
]

print(resultado)

#¿Qué imprime?  >>> Imprime
# 18
# 25
# 30

#Mini reto extra (nivel entrevista)
#Sin ejecutar:

datos = [
    {
        "nombre": "Ana",
        "direccion": {
            "ciudad": "Bogotá"
        }
    },
    {
        "nombre": "Luis",
        "direccion": {
            "ciudad": "Medellín"
        }
    }
]

resultado = [
    persona["direccion"]["ciudad"]
    for persona in datos
]

print(resultado)

#¿Qué imprime?  >>> Imprime ['Bogota', ' Medellin']

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

Regla rápida

Si ves:

resultado = [ ... ]
print(resultado)

piensa:

"Se imprime una lista completa."

Si ves:

for x in algo:
    print(x)

piensa:

"Se imprime un elemento por línea."

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Opción 1 (recomendada): Entorno virtual

#Activar el entorno:

#Windows

entorno\Scripts\activate

#Instalar requests:

pip install requests

#Ejecutar:

python archivo.py

#Esta es la forma profesional y la que usarás en proyectos reales.

#Opción 2: Python global

#También podrías hacer:

pip install requests

#fuera de un entorno virtual y luego ejecutar:

python archivo.py

#Funcionará igual para practicar, pero no es una buena costumbre para proyectos 
#porque las dependencias de distintos proyectos pueden entrar en conflicto.