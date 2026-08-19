from pydantic import BaseModel


class UsuarioPedidoResponse(BaseModel):
    id: int
    nombre: str
    correo: str

    model_config = {
        "from_attributes": True
    }


class PedidoDetalleResponse(BaseModel):
    id: int
    producto: str
    usuario: UsuarioPedidoResponse

    model_config = {
        "from_attributes": True
    }