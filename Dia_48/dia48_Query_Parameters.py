#Ejemplo con nombre obligatorio.
'''
from fastapi import FastAPI ______________________________

app = FastAPI()


@app.get("/saludo")
def saludar(nombre: str):
    return {
        "mensaje": f"Hola, {nombre}",
    }

#Ejemplo de parametros opcionales ________________________

from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/usuarios")
def usuarios(ciudad: Optional[str] = None):
    return {"ciudad": ciudad}

#Varios Query Parameters  ______________________________________

from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/usuarios")
def usuarios(
    ciudad: str,
    edad: int
):
    return {
        "ciudad": ciudad,
        "edad": edad
    }


#Ahora haremos que nombre sea opcional.  _________________________________

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
'''

#Ejemplo de combinacion de Path y Query Parameters ________________________

from fastapi import FastAPI

app = FastAPI()

#@app.get("/usuarios/{id}")
#def obtener_usuario(
#    id: int,
#    ciudad: str
#):
#    return {
#        "id": id,
#        "ciudad": ciudad
#    }

#VArios Query parameters en el mismo ejemplo 

@app.get("/usuarios/{id}")
def usuario(
    id: int,
    ciudad: str,
    edad: int
):
    return {
        "id": id,
        "ciudad": ciudad,
        "edad": edad
    }