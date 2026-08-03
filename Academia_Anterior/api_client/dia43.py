#Día 43 – APIs en Python: Consumo de APIs con Requests

#Parte 1: ¿Qué es una API?
#API significa:
#Application Programming Interface
#Una API permite que dos programas se comuniquen.
#Ejemplo:

#   Tu programa
#         ↓
#       API
#         ↓
#   Servidor

#Cuando consultas:

#clima
#tasas de cambio
#información de usuarios

#normalmente estás usando una API.

#Parte 2: Instalar Requests
#Dentro de tu entorno virtual:

#pip install requests
'''
#Parte 3: Primera petición

import requests

respuesta = requests.get("https://jsonplaceholder.typicode.com/users")

print(respuesta.status_code)


#Parte 4: Obtener JSON
#Las APIs suelen responder en JSON.

import requests

respuesta = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

datos = respuesta.json()

print(datos)


#Parte 5: Acceder a la información

import requests

respuesta = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

usuarios = respuesta.json()

print(usuarios[0]["name"])


#Parte 6: Recorrer resultados

import requests

respuesta = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

usuarios = respuesta.json()

for usuario in usuarios:
    print(usuario["name"])


#Parte 7: Verificar errores
import requests

respuesta = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)''

if respuesta.status_code == 200:
    print("Todo bien")
else:
    print("Error")
    '

#Parte 8: Códigos HTTP importantes
#Código	        Significado
#200	        OK
#201	        Creado
#400	        Solicitud incorrecta
#401	        No autorizado
#403	        Prohibido
#404	        No encontrado
#500	        Error del servidor

#Ejercicios de análisis (sin ejecutar)
#Ejercicio 1

import requests

r = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

print(r.status_code)

#¿Qué imprime?  >>> Imprime. Codigo 200, puesto que la url es valida.
'''
#Ejercicio 2

datos = [
    {"nombre": "Ana"},
    {"nombre": "Luis"}
]

print(datos[1]["nombre"])

#¿Qué imprime?  >>> Imprime Luis

#Ejercicio 3
usuarios = [
    {"nombre": "Ana"},
    {"nombre": "Luis"}
]

for usuario in usuarios:
    print(usuario["nombre"])

#¿Qué imprime?  >>> Imprime  
# Ana 
# Luis

#Ejercicio 4
respuesta = {
    "id": 10,
    "nombre": "Carlos"
}

print(respuesta["id"])

#¿Qué imprime?  >>> 10

#Ejercicio 5
codigo = 404

if codigo == 200:
    print("OK")
else:
    print("Error")

#¿Qué imprime?  >>> Error

#Mini reto extra (nivel entrevista)
#Sin ejecutar:

usuarios = [
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Luis", "edad": 25},
    {"nombre": "Carlos", "edad": 30}
]

for usuario in usuarios:
    if usuario["edad"] >= 25:
        print(usuario["nombre"])

#¿Qué imprime?  >>> Imprime 
# Luis
# Carlos