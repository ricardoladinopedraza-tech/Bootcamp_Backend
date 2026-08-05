# Configuración inicial de SQLAlchemy

## Objetivo

Preparar la aplicación para utilizar SQLAlchemy como ORM y establecer la base de la comunicación con PostgreSQL.

---

## ¿Qué problema resuelve SQLAlchemy?

Hasta ahora los datos se almacenaban en listas de Python.

```python
usuarios = []
```

Al detener la aplicación, toda la información se perdía.

SQLAlchemy permite almacenar la información de forma permanente en una base de datos.

---

## Arquitectura

Cliente

↓

FastAPI

↓

SQLAlchemy

↓

PostgreSQL

↓

Disco

SQLAlchemy actúa como intermediario entre los objetos de Python y la base de datos.

---

## Engine

El Engine administra las conexiones entre la aplicación y la base de datos.

Su función principal es preparar y gestionar la comunicación con PostgreSQL.

Ejemplo:

```python
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://usuario:password@localhost/base_datos"
)
```

### Idea clave

El Engine no consulta datos ni ejecuta lógica de negocio.

Su responsabilidad es administrar las conexiones.

---

## Session

Una Session representa una conversación temporal con la base de datos.

Durante una misma Session pueden realizarse varias operaciones:

- SELECT
- INSERT
- UPDATE
- DELETE

Cuando finaliza el trabajo, la Session se cierra.

### Ventajas

- Agrupa operaciones relacionadas.
- Evita abrir una conexión por cada línea de código.
- Permite confirmar (`commit`) o deshacer (`rollback`) cambios.

---

## Base

Las clases que representarán tablas deben heredar de Base.

Ejemplo:

```python
class Usuario(Base):
    ...
```

Gracias a esto SQLAlchemy entiende que esa clase corresponde a una tabla de la base de datos.

---

## Organización del proyecto

La configuración de SQLAlchemy se almacenará dentro de:

```
App/
│
└── database/
      ├── database.py
      └── __init__.py
```

En `database.py` se centralizarán:

- Engine
- SessionLocal
- Base

---

## Flujo de trabajo

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

PostgreSQL

↓

Respuesta

---

## Conceptos clave

- Engine administra las conexiones.
- Session representa una conversación temporal con la base de datos.
- Base permite convertir clases de Python en tablas.
- SQLAlchemy traduce objetos Python a consultas SQL.

---

## Idea principal del día

Engine, Session y Base constituyen los tres pilares fundamentales sobre los que construiremos toda la capa de persistencia de nuestra aplicación.