from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def inicio():
    return {"mensaje": "Hola desde FastAPI"}

@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int):
    if usuario_id != 5:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return {
        "id": usuario_id,
        "nombre": "Ricardo"
    }