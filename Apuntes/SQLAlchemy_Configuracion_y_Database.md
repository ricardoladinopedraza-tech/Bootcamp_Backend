# SQLAlchemy - Configuración inicial y database.py

## Objetivo

Preparar la aplicación para trabajar con SQLAlchemy como ORM y dejar lista la infraestructura que permitirá la comunicación con la base de datos.

---

# ¿Por qué utilizar SQLAlchemy?

Hasta este momento los datos se almacenaban en listas de Python.

```python
usuarios = []
```

Cuando la aplicación se detenía, toda la información desaparecía.

SQLAlchemy permite almacenar los datos de forma permanente utilizando una base de datos.

---

# Arquitectura general

Cliente

↓

FastAPI

↓

SQLAlchemy

↓

PostgreSQL / SQLite

↓

Disco

SQLAlchemy funciona como un puente entre los objetos de Python y la base de datos.

---

# Estructura del proyecto

App/

│

├── database/

│      ├── __init__.py

│      └── database.py

│

├── models/

├── routers/

├── schemas/

├── services/

└── main.py

Toda la configuración relacionada con la base de datos se centraliza en la carpeta **database**.

---

# Componentes principales

## Engine

El Engine administra las conexiones con la base de datos.

Existe un único Engine durante toda la ejecución de la aplicación.

Su responsabilidad es preparar y gestionar la comunicación con el motor de base de datos.

```python
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///app.db"

engine = create_engine(DATABASE_URL)
```

### Idea importante

El Engine NO consulta datos.

El Engine NO crea usuarios.

El Engine NO modifica registros.

Su única responsabilidad es administrar las conexiones.

---

## SessionLocal

SessionLocal es una fábrica de sesiones.

Cada petición crea una nueva Session utilizando SessionLocal.

```python
SessionLocal = sessionmaker(bind=engine)
```

Posteriormente:

```python
db = SessionLocal()
```

En ese momento nace una Session.

Cada usuario trabaja con su propia Session.

Cuando la petición termina, la Session se cierra.

---

## Base

Todas las clases que representen tablas deben heredar de Base.

```python
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
```

Más adelante:

```python
class Usuario(Base):
    ...
```

SQLAlchemy interpretará esta clase como una tabla de la base de datos.

---

# Archivo database.py

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///app.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
```

Este archivo constituye el punto central de toda la configuración de SQLAlchemy.

---

# Flujo completo

Cliente

↓

Router

↓

Service

↓

Session

↓

SQLAlchemy

↓

Base de Datos

↓

Respuesta

---

# Diferencia entre Engine y Session

Engine

- Existe uno solo.
- Vive mientras la aplicación está ejecutándose.
- Administra las conexiones.

Session

- Se crea para cada petición.
- Representa una conversación temporal con la base de datos.
- Se destruye al finalizar la petición.

---

# Conceptos aprendidos

- SQLAlchemy conecta FastAPI con la base de datos.
- Engine administra las conexiones.
- Session representa una conversación temporal.
- SessionLocal crea nuevas sesiones.
- Base permite convertir clases de Python en tablas.
- Toda la configuración se centraliza en database.py.

---

# Idea principal del día

Antes de crear tablas o consultar datos, es necesario preparar correctamente la infraestructura de SQLAlchemy.

Engine, SessionLocal y Base constituyen los tres pilares fundamentales de esa configuración.