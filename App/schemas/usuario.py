from pydantic import BaseModel
from App.schemas.pedido import PedidoResponse


class UsuarioActualizar(BaseModel):
    nombre: str | None = None
    correo: str | None = None
    password: str | None = None


class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    correo: str
    telefono: str | None = None
    ciudad: str | None = None

    model_config = {
        "from_attributes": True
    }

class UsuarioConPedidosResponse(BaseModel):
    id: int
    nombre: str
    correo: str
    telefono: str | None = None
    ciudad: str | None = None
    pedidos: list[PedidoResponse]

    model_config = {
        "from_attributes": True
    }

class LoginRequest(BaseModel):
    correo: str
    password: str