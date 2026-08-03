from fastapi import FastAPI
from Academia.Bootcamp_Banckend.Academia_desde_Bootcamp_Backend.Dia_59.services.usuarios import saludar

app = FastAPI()

@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return saludar(nombre)