
# Codigo 1. params=

import requests

parametros = {
    "categoria": "teclados"
}

r = requests.get(
    "https://api.tienda.com/productos",
    params=parametros
)

#requests construirá automáticamente la URL:

#https://api.tienda.com/productos?categoria=teclados

# Verifica si la petición fue exitosa (código 200)

if r.status_code == 200:
    # Convierte la respuesta JSON en un diccionario de Python
    productos = r.json()
    print(productos)
else:
    print(f"Error en la petición: {r.status_code}")

'''
#Codigo 2 headers=

#Ejemplo:

headers = {
    "User-Agent": "MiAplicacion"
}

r = requests.get(
    url,
    headers=headers
)

#Otro ejemplo:

headers = {
    "Accept": "application/json"
}

#Con esto el cliente está diciendo:

#"Espero recibir la respuesta en formato JSON."

#Codigo 3 Body

#Ejemplo:

import requests

datos = {
    "nombre": "Ricardo",
    "edad": 40
}

r = requests.post(
    "https://api.ejemplo.com/usuarios",
    json=datos
)

#requests hace dos cosas automáticamente:

#Convierte el diccionario en JSON.
#Añade el Header:

#      Content-Type: application/json

#Es una gran ventaja porque evita hacerlo manualmente.

# Codigo 4 data=

#Ejemplo:

datos = {
    "usuario": "ricardo",
    "clave": "1234"
}

r = requests.post(
    url,
    data=datos
)

#Hoy basta con recordar que:

#json= → APIs modernas.
#data= → Formularios o servicios más antiguos.
'''

#Ejemplo completo
'''
import requests

headers = {
    "User-Agent": "MiAplicacion"
}

params = {
    "categoria": "teclados"
}

r = requests.get(
    "https://api.ejemplo.com/productos",
    headers=headers,
    params=params
)
'''