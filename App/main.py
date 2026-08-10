from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import and_
from sqlalchemy.orm import Session

from App.database.database import Base, engine, SessionLocal
from App.models.usuario import Usuario
from App.schemas.usuario import UsuarioActualizar

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