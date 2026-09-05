Día 87 — Alembic: Introducción a las migraciones

Objetivo

Comprender por qué create_all() no sustituye un sistema de migraciones y aprender a utilizar Alembic para versionar y aplicar cambios controlados sobre la estructura de una base de datos PostgreSQL.

1. ¿Por qué necesitamos migraciones?

Base.metadata.create_all(bind=engine) permite crear tablas que todavía no existen. Sin embargo, una aplicación real evoluciona y necesitamos modificar estructuras existentes sin eliminarlas ni perder sus datos.

Ejemplo:

telefono = Column(String)

Si usuarios ya existe en PostgreSQL, necesitamos agregar la columna de forma controlada.

Ese es el problema que resuelve un sistema de migraciones.

2. create_all() vs Alembic

create_all()

Base.metadata.create_all(bind=engine)

Su función principal es crear estructuras que no existen. No es un sistema de historial ni de evolución controlada del esquema.

Alembic

Alembic permite:

registrar cambios del esquema;

crear versiones de esos cambios;

aplicar migraciones;

conocer la versión actual de la base de datos;

avanzar o retroceder mediante upgrade() y downgrade().

Conceptualmente:

Modelo SQLAlchemy
       ↓
Cambio detectado
       ↓
Migración
       ↓
PostgreSQL

3. Instalación e inicialización

Se instaló Alembic:

pip install alembic

Versión verificada:

alembic 1.19.1

Se inicializó:

alembic init alembic

Se creó la estructura alembic/, alembic/versions/ y alembic.ini.

4. Configuración

En alembic.ini se dejó:

sqlalchemy.url =

La conexión se obtiene desde .env.

En env.py se incorporó la carga de variables de entorno y los modelos:

import os
from dotenv import load_dotenv

from App.database.database import Base
from App.models.usuario import Usuario
from App.models.pedido import Pedido

Y:

load_dotenv()
database_url = os.getenv("DATABASE_URL")
config.set_main_option("sqlalchemy.url", database_url)

También:

target_metadata = Base.metadata

Los modelos se importan para que sus tablas queden registradas en Base.metadata.

5. Migración inicial

Se ejecutó:

alembic revision --autogenerate -m "estado inicial"

Se creó:

3965e7b974fd_estado_inicial.py

Como PostgreSQL ya tenía la estructura correspondiente a los modelos, la migración inicial no necesitó operaciones estructurales.

Se aplicó con:

alembic upgrade head

6. Primera migración real

Se agregó al modelo Usuario:

telefono = Column(String)

Después:

alembic revision --autogenerate -m "agregar telefono a usuarios"

Alembic detectó:

Detected added column 'usuarios.telefono'

y generó:

d8848d64e7cc_agregar_telefono_a_usuarios.py

La migración contiene:

def upgrade() -> None:
    op.add_column(
        'usuarios',
        sa.Column('telefono', sa.String(), nullable=True)
    )

def downgrade() -> None:
    op.drop_column('usuarios', 'telefono')

7. Cadena de migraciones

3965e7b974fd
       ↓
d8848d64e7cc (HEAD)

La segunda migración tiene como down_revision la primera, por lo que Alembic conoce el orden de ejecución.

8. Aplicación y verificación

Se ejecutó:

alembic upgrade head

Resultado:

Running upgrade 3965e7b974fd -> d8848d64e7cc,
agregar telefono a usuarios

Luego:

alembic current

Resultado:

d8848d64e7cc (head)

Esto confirma que la base de datos está en la última migración disponible.

9. Verificación física en PostgreSQL

Se abrió PostgreSQL:

psql -U postgres -d bootcamp_backend

Y se consultó:

\d usuarios

PostgreSQL confirmó:

id       | integer
nombre   | character varying
correo   | character varying
telefono | character varying

La columna telefono existe físicamente en la tabla.

También se verificó que la Foreign Key de pedidos.usuario_id hacia usuarios.id permanece intacta.

10. Flujo completo

Modelo SQLAlchemy
       ↓
Se modifica el modelo
       ↓
alembic revision --autogenerate
       ↓
Archivo de migración
       ↓
alembic upgrade head
       ↓
PostgreSQL modifica el esquema
       ↓
alembic current
       ↓
Verificación de versión
       ↓
psql / \d usuarios
       ↓
Verificación física

11. Comandos fundamentales

Comando

Función

alembic init alembic

Inicializa Alembic

alembic revision --autogenerate -m "mensaje"

Genera una migración

alembic upgrade head

Aplica las migraciones hasta la última

alembic current

Muestra la versión actual de la BD

alembic heads

Muestra la última revisión disponible

12. Diferencia conceptual fundamental

create_all()
    ↓
CREAR estructuras inexistentes

Alembic
    ↓
EVOLUCIONAR estructuras existentes
    ↓
de forma controlada y versionada

create_all() ayuda a crear la estructura inicial; Alembic permite gestionar su evolución.

13. Relación con los temas anteriores

FastAPI
    ↓
SQLAlchemy
    ↓
psycopg
    ↓
PostgreSQL
    ↓
bootcamp_backend
    ↓
usuarios / pedidos

Ahora incorporamos:

Alembic
    ↓
control de evolución del esquema

SQLAlchemy define y utiliza los modelos ORM. Alembic utiliza esa información para detectar y gestionar cambios en la estructura de la base de datos.

14. Idea clave para entrevista

Alembic es una herramienta de migraciones para SQLAlchemy que permite versionar y aplicar cambios controlados al esquema de una base de datos, evitando tener que reconstruir las tablas cada vez que cambia el modelo.

Estado

Día 87 completado.