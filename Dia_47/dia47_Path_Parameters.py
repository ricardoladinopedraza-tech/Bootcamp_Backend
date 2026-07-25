# Ejemplo 1
'''
from fastapi import FastAPI

app = FastAPI()


@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int):
    return {
        "mensaje": "Usuario encontrado",
        "usuario_id": usuario_id,
    }
    '''


#Mini Proyecto

from fastapi import FastAPI, HTTPException

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
]


@app.get("/usuarios")
def listar_usuarios():
    return usuarios


@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            return usuario

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado",
    )