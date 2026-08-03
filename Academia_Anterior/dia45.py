#Día 45 — APIs: Parámetros, Headers y Manejo de Errores

1. Parámetros en una API

Hasta ahora hacíamos:

import requests

r = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

Muchas APIs permiten enviar parámetros:

import requests

r = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}
)

print(r.url)

#Resultado aproximado:   https://jsonplaceholder.typicode.com/posts?userId=1
#requests construye la URL automáticamente.

#2. Varios parámetros
params = {
    "userId": 1,
    "id": 5
}

r = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)

print(r.json())