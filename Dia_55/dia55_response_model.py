from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Usuario(BaseModel):
    nombre: str
    correo: str
    password: str


class UsuarioRespuesta(BaseModel):
    nombre: str
    correo: str


@app.post("/usuarios", response_model=UsuarioRespuesta)
def crear_usuario(usuario: Usuario):
    return usuario