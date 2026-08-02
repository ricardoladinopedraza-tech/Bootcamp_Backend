from fastapi import FastAPI, Depends

app = FastAPI()

def verificar_usuario():
    return "Ricardo autenticado"

@app.get("/usuarios")
def usuarios(usuario: str = Depends(verificar_usuario)):
    return {
        "mensaje": usuario
    }

@app.get("/productos")
def productos(usuario: str = Depends(verificar_usuario)):
    return {
        "mensaje": usuario
         }