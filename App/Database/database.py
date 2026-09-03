#modificacion despues de dotenv() 

from dotenv import load_dotenv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Cargar variables del archivo .env
load_dotenv()

# Obtener la URL desde las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

# Crear el motor de SQLAlchemy
engine = create_engine(DATABASE_URL)

# Crear la fábrica de sesiones
SessionLocal = sessionmaker(bind=engine)


# Clase base para todos los modelos ORM
class Base(DeclarativeBase):
    pass











# prueba de que Python puede leer .env.
'''
import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("DATABASE_URL"))




from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

#DATABASE_URL = "sqlite:///app.db" #La base de datos que vamos a utilizar es SQLite y está en app.db.

DATABASE_URL = "postgresql+psycopg://postgres:x0tr.u21H@localhost:5432" \
"/bootcamp_backend" #ahora la baase de datos esta en PostgreSQL


engine = create_engine(DATABASE_URL) #Codigo hasta dia 72
'''
'''
#Codigo agregado dia 80
engine = create_engine(
    DATABASE_URL,
    echo=True
)
'''
'''
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
    '''