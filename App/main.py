from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import and_
from sqlalchemy.orm import Session

from App.database.database import Base, engine, SessionLocal
from App.models.usuario import Usuario
from App.models.pedido import Pedido
from App.schemas.usuario import UsuarioActualizar
from App.schemas.pedido import (UsuarioPedidoResponse, PedidoDetalleResponse)

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.post("/usuarios")
def crear_usuario(
    nombre: str,
    correo: str,
    db: Session = Depends(get_db)
):
    nuevo_usuario = Usuario(
        nombre=nombre,
        correo=correo
    )

    db.add(nuevo_usuario)

    db.commit()

    db.refresh(nuevo_usuario)

    return nuevo_usuario


@app.get("/usuarios")
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return usuarios


@app.get("/usuarios/{usuario_id}")
def obtener_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return usuario


@app.get("/usuarios/buscar/{nombre}")
def buscar_usuario(
    nombre: str,
    db: Session = Depends(get_db)
):
    usuarios = db.query(Usuario).filter(
        and_(
            Usuario.nombre.contains(nombre),
            Usuario.id > 1
        )
    ).all()

    return usuarios

@app.patch("/usuarios/{usuario_id}")
def actualizar_usuario(
    usuario_id: int,
    datos: UsuarioActualizar,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    datos_actualizados = datos.model_dump(
    exclude_unset=True
)

    for campo, valor in datos_actualizados.items():
        setattr(usuario, campo, valor)

    db.commit()

    db.refresh(usuario)

    return usuario

@app.delete("/usuarios/{usuario_id}")
def eliminar_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    db.delete(usuario)
    db.commit()

    return {
        "mensaje": "Usuario eliminado correctamente"
    }


@app.post("/pedidos")
def crear_pedido(
    producto: str,
    usuario_id: int,
    db: Session = Depends(get_db)
):
    nuevo_pedido = Pedido(
        producto=producto,
        usuario_id=usuario_id
    )

    db.add(nuevo_pedido)
    db.commit()
    db.refresh(nuevo_pedido)

    return nuevo_pedido

@app.get("/pedidos/usuario/{usuario_id}")
def listar_pedidos_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    pedidos = db.query(Pedido).filter(
        Pedido.usuario_id == usuario_id
    ).all()

    return pedidos

@app.get("/pedidos/detalle")
def detalle_pedidos(db: Session = Depends(get_db)):

    resultados = db.query(
        Pedido.producto,
        Usuario.nombre
    ).join(
        Usuario,
        Pedido.usuario_id == Usuario.id
    ).all()

    return [
        {
            "producto": producto,
            "nombre": nombre
        }
        for producto, nombre in resultados
    ]

@app.get(
    "/usuarios/{usuario_id}/pedidos",
    response_model=list[UsuarioPedidoResponse]
)
def obtener_pedidos_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return usuario.pedidos

@app.get(
    "/usuarios/{usuario_id}/pedidos",
    response_model=list[UsuarioPedidoResponse]
)
def obtener_pedidos_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return usuario.pedidos

@app.get(
    "/pedidos/detalle-orm",
    response_model=list[PedidoDetalleResponse]
)
def obtener_pedidos_detalle_orm(
    db: Session = Depends(get_db)
):
    pedidos = db.query(Pedido).all()

    return pedidos

@app.get(
    "/pedidos/{pedido_id}",
    response_model=PedidoDetalleResponse
)
def obtener_pedido(
    pedido_id: int,
    db: Session = Depends(get_db)
):
    pedido = db.query(Pedido).filter(
        Pedido.id == pedido_id
    ).first()

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail="Pedido no encontrado"
        )

    return pedido

