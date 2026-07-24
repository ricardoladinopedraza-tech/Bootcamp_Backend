#Ejemoplo con requests PUT
'''
import requests

usuario = {
    "name": "Ricardo",
    "email": "ricardo@email.com",
    "city": "Tunja"
}

r = requests.put(
    "https://jsonplaceholder.typicode.com/users/5",
    json=usuario
)

print(r.status_code)
print(r.json())

#Ejemplo con requests.patch()

import requests

cambio = {
    "city": "Bogotá"
}

r = requests.patch(
    "https://jsonplaceholder.typicode.com/users/5",
    json=cambio
)

print(r.status_code)
print(r.json())
'''
#Ejemplo completo PUT PATCH

import requests

usuario = {
    "name": "Ricardo",
    "email": "ricardo@email.com",
    "city": "Tunja"
}

respuesta = requests.put(
    "https://jsonplaceholder.typicode.com/users/5",
    json=usuario
)

print("PUT")
print(respuesta.status_code)
print(respuesta.json())

print()

cambio = {
    "city": "Bogotá"
}

respuesta = requests.patch(
    "https://jsonplaceholder.typicode.com/users/5",
    json=cambio
)

print("PATCH")
print(respuesta.status_code)
print(respuesta.json())