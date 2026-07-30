from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Direccion(BaseModel):
    calle: str
    numero: str
    ciudad: str

class Usuario(BaseModel):
    nombre: str = Field(min_length=3, max_length=50)
    edad: int = Field(ge=18, le=120)
    telefono: Optional[str] = None
    activo: bool = True
    direccion: Direccion

@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    return usuario