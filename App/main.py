from fastapi import FastAPI

from App.database.database import Base, engine
from App.models.usuario import Usuario

app = FastAPI()

Base.metadata.create_all(bind=engine)