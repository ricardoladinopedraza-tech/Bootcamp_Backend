Día 85 — PostgreSQL + SQLAlchemy: cambio de SQLite a PostgreSQL

Objetivo

Comprender qué cambia y qué permanece igual al pasar de SQLite a PostgreSQL.

Antes

FastAPI
   ↓
SQLAlchemy
   ↓
SQLite
   ↓
app.db

Ahora

FastAPI
   ↓
SQLAlchemy
   ↓
psycopg
   ↓
PostgreSQL
   ↓
bootcamp_backend

Qué cambió

Principalmente cambió la URL de conexión para que SQLAlchemy utilizara PostgreSQL mediante psycopg.

Qué permaneció

Los modelos y las operaciones ORM principales continúan siendo los mismos:

db.query(...)
db.add(...)
db.delete(...)
db.commit()
db.refresh(...)

create_all()

Base.metadata.create_all(bind=engine)

Permitió crear en PostgreSQL las tablas definidas por nuestros modelos.

Pero:

create_all() ≠ migración de datos

Si SQLite tenía registros, esos registros no aparecen automáticamente en PostgreSQL.

Diferencia SQLite / PostgreSQL

SQLite
  ↓
archivo local: app.db

PostgreSQL
  ↓
servidor
  ↓
base de datos: bootcamp_backend
  ↓
tablas

Respuesta de entrevista

Principalmente cambié la configuración de conexión para que SQLAlchemy utilizara PostgreSQL mediante el driver psycopg. Los modelos y las operaciones ORM principales permanecieron iguales.

Y:

create_all() crea la estructura de las tablas; no realiza una migración de los datos existentes.

Estado

Día 85 completado.