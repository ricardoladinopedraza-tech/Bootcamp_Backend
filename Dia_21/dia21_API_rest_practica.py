#Ejemplo 
'''
import requests

nuevo_usuario = {
    "name": "Ricardo",
    "email": "ricardo@email.com"
}

r = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=nuevo_usuario
)

print(r.status_code)

print(r.json())

#Ejemplo completo

import requests

nuevo_usuario = {
    "name": "Ricardo",
    "email": "ricardo@email.com"
}

r = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=nuevo_usuario
)

print("Código:", r.status_code)

print()

print("Respuesta:")

print(r.json())
'''
#mini proyecto

import requests

nuevo_usuario = {
    "name": "Ricardo",
    "email": "ricardo@email.com"
}

respuesta = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=nuevo_usuario
)

print("Código:", respuesta.status_code)

if respuesta.status_code == 201:
    print("Usuario creado correctamente.")
    print(respuesta.json())
else:
    print("Error:", respuesta.status_code)