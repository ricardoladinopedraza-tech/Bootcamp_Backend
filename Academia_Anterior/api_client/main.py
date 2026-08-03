'''
# Codigo dia 46

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Hola Mundo"}


@app.get("/saludo")
def saludo():
    return {"mensaje": "Bienvenido"}

'''
#>>>>>>>>>>>>>>>>  Analicemos el codigo   >>>>>>>>>>>>>>>>
'''
Analicemos línea por línea

Importamos FastAPI

from fastapi import FastAPI

Creamos la aplicación

app = FastAPI()

Todo ocurre sobre el objeto app.

El decorador
@app.get("/")

Aquí aparece algo nuevo.

Se llama decorador.

Por ahora puedes verlo como una instrucción que dice:

"Cuando alguien visite esta ruta, ejecuta esta función."

No necesitas aprender cómo funcionan internamente todavía. Más adelante los estudiaremos con detalle.

La función
def inicio():

Se ejecutará cuando alguien entre a:

/
El retorno
return {
    "mensaje": "Hola Mundo"
}

FastAPI convierte automáticamente el diccionario en JSON.

No necesitas usar:

json.dumps()

Eso lo hace FastAPI por ti.
'''

#>>>>>>>>>>>>>>   Ejecutar la API    <<<<<<<<<<<<<<<<

'''
Desde la terminal:

uvicorn main:app --reload

¿Qué significa?

main

Nombre del archivo.

main.py
app

Nombre del objeto:

app = FastAPI()
--reload

Cada vez que guardes el archivo, el servidor se reinicia automáticamente.

Muy útil durante el desarrollo.

Si todo salió bien

Verás algo parecido a:

INFO:
Uvicorn running on

http://127.0.0.1:8000

>>>>>>>>>>>>>>>> Lo mejor de FastAPI  >>>>>>>>>>>>>>>>>>

Tiene documentación automática.

Ve a:

http://127.0.0.1:8000/docs

Verás una página donde puedes probar tu API sin usar otro programa.
'''


# Codigo dia 47
'''
from fastapi import FastAPI

app = FastAPI()

@app.get("/usuarios/{id}")
def obtener_usuario(id: int):
    return {
        "id": id
    }
'''
#   $%$%$%$%$%$%%$% Codigo dia 45 %$%$%$%$%$%$%$%$%$%$
'''
#1. Parámetros en una API
#Hasta ahora hacíamos:

#import requests

#r = requests.get(
#    "https://jsonplaceholder.typicode.com/users"
#)

#Muchas APIs permiten enviar parámetros:

import requests

r = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}
)

print(r.url)

#Resultado aproximado:
#https://jsonplaceholder.typicode.com/posts?userId=1
#   requests construye la URL automáticamente.
'''
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