from pydantic import BaseModel


class UsuarioActualizar(BaseModel):
    nombre: str | None = None
    correo: str | None = None


class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    correo: str
    telefono: str | None = None
    ciudad: str | None = None

    model_config = {
        "from_attributes": True
    }