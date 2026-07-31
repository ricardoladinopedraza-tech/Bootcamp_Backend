from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Producto(BaseModel):
    nombre: str
    precio: float = Field(gt=0)
    cantidad: int = Field(gt=0)

class Pedido(BaseModel):
    cliente: str
    productos: List[Producto]

@app.post("/pedidos")
def crear_pedido(pedido: Pedido):
    return pedido