#Ejemplo
'''
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/usuarios")
def listar_usuarios(
    limite: int = Query(default=2, ge=1, le=10),
):
    return {
        "limite_solicitado": limite,
    }
'''
#Ejemplo mini reto

from fastapi import FastAPI, Query

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
    {
        "id": 4,
        "nombre": "Carlos",
        "email": "carlos@email.com",
    },
]


@app.get("/usuarios")
def listar_usuarios(
    nombre: str | None = Query(
        default=None,
        min_length=2,
        max_length=20,
    ),
    limite: int = Query(
        default=10,
        ge=1,
        le=10,
    ),
):
    usuarios_filtrados = usuarios

    if nombre is not None:
        usuarios_filtrados = [
            usuario
            for usuario in usuarios
            if nombre.lower() in usuario["nombre"].lower()
        ]

    return usuarios_filtrados[:limite]