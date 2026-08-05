# Día 64 – Creación automática de tablas con SQLAlchemy

## Objetivo

Aprender cómo SQLAlchemy crea automáticamente las tablas definidas mediante modelos ORM.

---

## Conceptos importantes

### Base.metadata

Base mantiene un registro de todos los modelos que heredan de ella.

---

### metadata.create_all()

```python
Base.metadata.create_all(bind=engine)
```

Recorre todos los modelos registrados y crea únicamente las tablas que aún no existen.

No elimina tablas existentes ni sobrescribe información.

---

### engine

Es la conexión permanente con la base de datos.

```python
engine = create_engine(DATABASE_URL)
```

---

### bind=engine

Indica sobre qué base de datos deben crearse las tablas.

---

### Importación de modelos

Antes de ejecutar create_all() es obligatorio importar los modelos.

Ejemplo:

```python
from App.models.usuario import Usuario
```

Aunque la variable Usuario no se utilice directamente, su importación registra el modelo en Base.

---

## Flujo

FastAPI

↓

Importa modelos

↓

Base registra las tablas

↓

metadata.create_all()

↓

SQLite

↓

Creación de tablas

---

## Modelo Usuario

```python
from sqlalchemy import Column, Integer, String

from App.database.database import Base


class Usuario(Base):

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)

    nombre = Column(String)

    correo = Column(String)
```

---

## main.py

```python
from fastapi import FastAPI

from App.database.database import Base, engine
from App.models.usuario import Usuario

app = FastAPI()

Base.metadata.create_all(bind=engine)
```

---

## Resultado obtenido

✔ Aplicación ejecutada correctamente.

✔ SQLAlchemy instalado.

✔ FastAPI funcionando.

✔ Uvicorn iniciado correctamente.

✔ Base de datos SQLite creada automáticamente.

✔ Archivo generado:

app.db

✔ Tabla creada:

usuarios

---

## Aprendizaje personal

La creación automática de tablas depende de tres elementos:

- Base
- Engine
- Modelos importados

Si alguno falta, SQLAlchemy no podrá crear las tablas.