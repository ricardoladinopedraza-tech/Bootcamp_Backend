from fastapi import FastAPI
from services.usuarios import saludar

app = FastAPI()

@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return saludar(nombre)