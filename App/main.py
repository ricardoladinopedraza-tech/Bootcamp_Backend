from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import and_
#from sqlalchemy.orm import Session, joinedload
from sqlalchemy.orm import Session, selectinload

from App.database.database import Base, engine, SessionLocal
from App.models.usuario import Usuario
from App.models.pedido import Pedido
from App.schemas.usuario import UsuarioActualizar, UsuarioResponse, LoginRequest
#from App.schemas.usuario import UsuarioActualizar, UsuarioResponse
#from App.schemas.usuario import UsuarioActualizar
from App.schemas.pedido import (UsuarioPedidoResponse, PedidoDetalleResponse)

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

import jwt

from App.security import (
    hash_password,
    verify_password,
    create_access_token,
    decode_access_token
)

app = FastAPI()
security = HTTPBearer()

#Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.post("/usuarios", response_model=UsuarioResponse)
def crear_usuario(
    nombre: str,
    correo: str,
    password: str,
    db: Session = Depends(get_db)
):
    nuevo_usuario = Usuario(
        nombre=nombre,
        correo=correo,
        password_hash=hash_password(password)
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return nuevo_usuario


@app.get("/usuarios")
def listar_usuarios(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    try:
        decode_access_token(token)

    except jwt.PyJWTError:
        raise HTTPException(
            status_code=401,
            detail="Token inválido o expirado"
        )

    usuarios = db.query(Usuario).all()

    return usuarios


@app.get("/usuarios/con-pedidos")
def usuarios_con_pedidos(
    db: Session = Depends(get_db)
):
    usuarios = db.query(Usuario).options(
        selectinload(Usuario.pedidos)
    ).all()

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
'''
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
'''
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

'''
#Endpoint sin joinedload
@app.get(
    "/pedidos/detalle-orm",
    response_model=list[PedidoDetalleResponse]
)
def obtener_pedidos_detalle_orm(
    db: Session = Depends(get_db)
):
    pedidos = db.query(Pedido).all()

    return pedidos


#Endpoint con joinedload()
@app.get(
    "/pedidos/detalle-orm",
    response_model=list[PedidoDetalleResponse]
)
def obtener_pedidos_detalle_orm(
    db: Session = Depends(get_db)
):
    pedidos = db.query(Pedido).options(
        joinedload(Pedido.usuario)
    ).all()

    return pedidos
'''
#Endpoint con selectinload()
@app.get(
    "/pedidos/detalle-orm",
    response_model=list[PedidoDetalleResponse]
)
def obtener_pedidos_detalle_orm(
    db: Session = Depends(get_db)
):
    pedidos = db.query(Pedido).options(
        selectinload(Pedido.usuario)
    ).all()

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

@app.post("/login")
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
        Usuario.correo == data.correo
    ).first()

    if usuario is None or usuario.password_hash is None:
        raise HTTPException(
            status_code=401,
            detail="Credenciales incorrectas"
        )

    if not verify_password(
        data.password,
        usuario.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Credenciales incorrectas"
        )

    access_token = create_access_token(
    {"sub": str(usuario.id)}
)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@app.get("/protegido")
def endpoint_protegido(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    try:
        payload = decode_access_token(token)

    except jwt.PyJWTError:
        raise HTTPException(
            status_code=401,
            detail="Token inválido o expirado"
        )

    return {
        "mensaje": "Acceso permitido",
        "sub": payload["sub"]
    }

