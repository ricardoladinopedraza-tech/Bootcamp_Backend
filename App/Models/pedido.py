from sqlalchemy import Column, Integer, String, ForeignKey

from App.database.database import Base


class Pedido(Base):

    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True)

    producto = Column(String)

    usuario_id = Column(
        Integer,
        ForeignKey("usuarios.id")
    )