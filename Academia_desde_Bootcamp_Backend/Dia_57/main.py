from fastapi import FastAPI
from Academia.Bootcamp_Banckend.Academia_desde_Bootcamp_Backend.Dia_57.routers.usuarios import router

app = FastAPI()

app.include_router(router)