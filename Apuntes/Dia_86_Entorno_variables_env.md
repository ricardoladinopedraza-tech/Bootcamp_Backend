Día 86 — Variables de entorno, .env y seguridad

Objetivo

Sacar información sensible del código fuente y gestionarla mediante variables de entorno.

Problema

No es recomendable escribir directamente en el código:

DATABASE_URL = "postgresql+psycopg://usuario:contraseña@localhost:5432/bootcamp_backend"

La credencial quedaría expuesta en el código fuente.

.env

En desarrollo local utilizamos .env para almacenar configuración:

DATABASE_URL=postgresql+psycopg://...
SECRET_KEY=...
DEBUG=True

.gitignore

Se incluye:

.env

Esto indica a Git que no debe rastrear ese archivo.

Distinción fundamental:

.env
 ↓
configuración fuera del código

.gitignore
 ↓
evita que Git rastree .env

.env por sí solo no impide que un archivo sea publicado; .gitignore evita que Git lo incluya en el repositorio.

python-dotenv

from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

load_dotenv() carga las variables del archivo .env y os.getenv() permite leerlas.

Cadena completa

.env
 ↓
load_dotenv()
 ↓
os.getenv("DATABASE_URL")
 ↓
DATABASE_URL
 ↓
create_engine()
 ↓
SQLAlchemy
 ↓
psycopg
 ↓
PostgreSQL

Verificación realizada

Se comprobó que os.getenv("DATABASE_URL") sin cargar .env devuelve None. Después de load_dotenv() la variable fue leída correctamente.

También se comprobó que .env no aparece como archivo pendiente de seguimiento en git status.

Idea clave para entrevista

Sacamos la información sensible del código fuente mediante variables de entorno y evitamos que .env sea rastreado por Git mediante .gitignore.

Estado

Día 86 completado.