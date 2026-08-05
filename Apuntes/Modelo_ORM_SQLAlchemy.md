# Día 63 – Primer Modelo ORM con SQLAlchemy

## Objetivo

Aprender a crear el primer modelo ORM utilizando SQLAlchemy y comprender cómo una clase de Python representa una tabla dentro de la base de datos.

---

# ¿Qué es un ORM?

ORM (Object Relational Mapping) es una técnica que permite representar tablas de una base de datos mediante clases de Python.

Relación:

Clase → Tabla

Atributo → Columna

Objeto → Registro

SQLAlchemy realiza automáticamente esta conversión.

---

# Estructura del proyecto

App/

├── database/

├── models/

│      └── usuario.py

├── routers/

├── schemas/

├── services/

└── main.py

Los modelos se almacenan dentro de la carpeta **models**.

---

# Importaciones

```python
from sqlalchemy import Column, Integer, String
from App.database.database import Base
```

Se importan:

- Column para definir columnas.
- Integer y String como tipos de datos.
- Base para indicar que la clase representa una tabla.

---

# Creación del modelo

```python
class Usuario(Base):

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)

    nombre = Column(String)

    correo = Column(String)
```

---

# Explicación

## class Usuario(Base)

Indica que la clase será interpretada por SQLAlchemy como una tabla.

---

## __tablename__

Define el nombre que tendrá la tabla dentro de la base de datos.

```python
__tablename__ = "usuarios"
```

La tabla creada será:

usuarios

---

## Column()

Define una columna.

Ejemplo:

```python
nombre = Column(String)
```

---

## Tipos de datos

Integer

Representa números enteros.

String

Representa cadenas de texto.

---

## Primary Key

```python
id = Column(Integer, primary_key=True)
```

Identifica de manera única cada registro de la tabla.

---

# Flujo ORM

Clase Python

↓

Modelo ORM

↓

Tabla SQL

↓

Registros

---

# Modelo implementado

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

# Conceptos aprendidos

- Un modelo ORM representa una tabla.
- Base permite que SQLAlchemy reconozca la clase.
- __tablename__ define el nombre de la tabla.
- Column() crea las columnas.
- Integer y String representan tipos de datos.
- primary_key=True define la llave primaria.

---

# Idea principal del día

A partir de este momento comenzamos a diseñar la estructura de la base de datos utilizando clases de Python en lugar de escribir tablas manualmente.