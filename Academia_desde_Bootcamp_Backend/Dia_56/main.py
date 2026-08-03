from fastapi import FastAPI
from Academia.Bootcamp_Banckend.Academia_desde_Bootcamp_Backend.Dia_56.usuarios import router

app = FastAPI()

app.include_router(router)