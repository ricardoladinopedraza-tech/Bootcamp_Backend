from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Usuario(BaseModel):
    nombre: str = Field(min_length=3, max_length=50)
    edad: int = Field(ge=18, le=120)
    ciudad: str = Field(min_length=2, max_length=50)
    telefono: Optional[str] = None
    activo: bool = True


@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    return usuario