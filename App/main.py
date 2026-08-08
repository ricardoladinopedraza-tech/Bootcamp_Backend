from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from App.database.database import Base, engine, SessionLocal
from App.models.usuario import Usuario

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

@app.get("/usuarios")
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return usuarios

    db.add(nuevo_usuario)

    db.commit()

    db.refresh(nuevo_usuario)

    return nuevo_usuario

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