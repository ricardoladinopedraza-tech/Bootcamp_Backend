from pydantic import BaseModel


class UsuarioActualizar(BaseModel):
    nombre: str | None = None
    correo: str | None = None