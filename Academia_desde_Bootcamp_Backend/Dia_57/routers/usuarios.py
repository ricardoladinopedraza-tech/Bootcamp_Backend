from fastapi import APIRouter

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

@router.get("/")
def listar():
    return {
        "mensaje": "Lista de usuarios"
    }

@router.post("/")
def crear():
    return {
        "mensaje": "Usuario creado"
    }