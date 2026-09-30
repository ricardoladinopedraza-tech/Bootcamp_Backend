Día 110 --- Publicación remota del Proyecto 1 con Railway
Objetivo
Publicar el Proyecto 1 (FastAPI + PostgreSQL) en Internet mediante
Railway, usando Docker, variables de entorno y migraciones Alembic.
Estado: COMPLETADO ✅
Progreso: 110 / 112
Arquitectura final
Navegador
 ↓ HTTPS
Railway Public Networking
 ↓ puerto 8080
Docker / Uvicorn / FastAPI
 ↓
SQLAlchemy
 ↓
psycopg 3
 ↓
PostgreSQL Railway + volumen
Configuración de producción
Se conectó el repositorio GitHub Bootcamp_Backend a Railway y se creó
PostgreSQL remoto. Las variables sensibles quedaron fuera del
repositorio:
DATABASE_URL → referencia al PostgreSQL de Railway
SECRET_KEY   → secreto independiente de producción
DEBUG        → False
El Dockerfile arranca con:
CMD ["sh", "-c", "alembic upgrade head && uvicorn App.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
&& garantiza que Uvicorn solo arranque si Alembic termina
correctamente.
Problema 1 --- Windows vs Linux
Railway produjo:
ModuleNotFoundError: No module named 'App.database'
Git contenía App/Database, App/Models, App/Routers y
App/Services, mientras los imports utilizaban minúsculas. Windows
ocultaba la diferencia; Linux distingue mayúsculas y minúsculas.
Se normalizó:
Database → database
Models → models
Routers → routers
Services → services
Se usó git mv para registrar correctamente los cambios de
capitalización.
Problema 2 --- psycopg2 vs psycopg 3
Railway entregó una URL postgresql://.... SQLAlchemy intentó cargar
psycopg2, pero el proyecto utiliza psycopg 3.
En App/database/database.py se normalizó:
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL and DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgresql://",
        "postgresql+psycopg://",
        1
    )
Problema 3 --- Alembic tenía su propio camino de conexión
Aunque FastAPI quedó corregido, Alembic continuó fallando porque
alembic/env.py lee DATABASE_URL y crea otro engine mediante
engine_from_config().
Se aplicó allí la misma normalización:
database_url = os.getenv("DATABASE_URL")

if database_url and database_url.startswith("postgresql://"):
    database_url = database_url.replace(
        "postgresql://",
        "postgresql+psycopg://",
        1
    )

config.set_main_option("sqlalchemy.url", database_url)
Concepto:
DATABASE_URL
 ├─ database.py → create_engine()
 └─ alembic/env.py → engine_from_config()
Usar la misma variable no significa compartir automáticamente el mismo
objeto Engine.
Problema 4 --- Puerto público
Los logs demostraron:
Application startup complete.
Uvicorn running on http://0.0.0.0:8080
Railway había definido PORT=8080, por lo que ${PORT:-8000} eligió
8080. Public Networking inicialmente apuntaba al 8000 y produjo un 502.
Se corrigió:
Railway Public Networking → target 8080
Uvicorn                    → 8080
Swagger comenzó a responder públicamente.
Verificación final
Se ejecutó públicamente:
GET /usuarios/1
Respuesta:
{
  "detail": "Usuario no encontrado"
}
HTTP 404 fue correcto: la consulta llegó a PostgreSQL Railway, pero la
base remota no tenía ese usuario.
Esquema vs datos
Durante el proyecto existieron bases diferentes:
PostgreSQL Windows → usuarios de práctica
PostgreSQL Docker  → Docker Test
PostgreSQL Railway → inicialmente vacío
Alembic migró el esqueleto de la base:
- tablas
- columnas
- PK/FK
- constraints
- estructura
No trasladó automáticamente los registros.
Migración de esquema ≠ migración de datos.
Los datos requieren otro proceso: exportación/importación, scripts de
migración o seed controlado.
Método de diagnóstico consolidado
error
 ↓
logs / traceback
 ↓
identificar causa
 ↓
hacer UN cambio
 ↓
probar en Docker/Linux local
 ↓
commit + push
 ↓
deployment
 ↓
verificación real
Respuesta útil para entrevista
Dockericé una API FastAPI y la desplegué en Railway conectada a
PostgreSQL. Configuré secretos mediante variables de entorno, ejecuté
Alembic antes de Uvicorn y utilicé el puerto proporcionado por el
entorno. Durante el despliegue resolví diferencias de capitalización
entre Windows y Linux, la selección del driver psycopg, la
configuración independiente de Alembic y un problema de enrutamiento
entre el puerto público y el puerto interno. Finalmente verifiqué
Swagger y una consulta real contra PostgreSQL remoto.

Resultado
Día 110 completado ✅