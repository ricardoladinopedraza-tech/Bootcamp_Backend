from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from App.database.database import Base


class Usuario(Base):

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)

    nombre = Column(String)

    correo = Column(String)

    pedidos = relationship(
        "Pedido",
        back_populates="usuario"
    )