from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///app.db"

#engine = create_engine(DATABASE_URL) #Codigo hasta dia 72

#Codigo agregado dia 80
engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass