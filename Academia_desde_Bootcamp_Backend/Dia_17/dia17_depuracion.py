# Depuracion

import requests

r = requests.get(
    "https://jsonplaceholder.typicode.com/usuarios"
)

usuarios = r.json() #Convertir JSON a Python

#Pado 2. Verificar estado

print(r.status_code)  #Resultado para este caso 200

print(r.reason)

print(r.url)

print(r.headers)


'''
#Que tipo de dato es

print(type(usuarios))

#¿Cuántos usuarios llegaron?

print(len(usuarios))

#Primer usuario

print(usuarios[0])

#Obtener solamente el nombre

print(usuarios[0]["name"])

#Obtener el correo

print(usuarios[0]["email"])

#Analicemos un campo más complejo address

print(type(usuarios[0]["address"]))

print(usuarios[0]["address"])

#Obtener solamente la ciudad

print(usuarios[0]["address"]["city"])

#Ahora observemos la empresa

print(usuarios[0]["company"])

#Obtener el nombre de la empresa

print(usuarios[0]["company"]["name"])

'''