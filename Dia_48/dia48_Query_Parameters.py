#Ejemplo con nombre obligatorio.
'''
from fastapi import FastAPI

app = FastAPI()


@app.get("/saludo")
def saludar(nombre: str):
    return {
        "mensaje": f"Hola, {nombre}",
    }



#Ahora haremos que nombre sea opcional. 

from fastapi import FastAPI

app = FastAPI()


@app.get("/saludo")
def saludar(nombre: str | None = None):
    if nombre is None:
        return {
            "mensaje": "Hola, visitante",
        }

    return {
        "mensaje": f"Hola, {nombre}",
    }
'''
#Mini proyecto.  filtrar usuarios por nombre.

from fastapi import FastAPI

app = FastAPI()

usuarios = [
    {
        "id": 1,
        "nombre": "Ricardo",
        "email": "ricardo@email.com",
    },
    {
        "id": 2,
        "nombre": "Ana",
        "email": "ana@email.com",
    },
    {
        "id": 3,
        "nombre": "Andrés",
        "email": "andres@email.com",
    },
]


@app.get("/usuarios")
def listar_usuarios(nombre: str | None = None):
    if nombre is None:
        return usuarios

    usuarios_filtrados = [
        usuario
        for usuario in usuarios
        if nombre.lower() in usuario["nombre"].lower()
    ]

    return usuarios_filtrados