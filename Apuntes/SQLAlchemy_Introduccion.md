# Introducción a SQLAlchemy

## ¿Qué es SQLAlchemy?

SQLAlchemy es un ORM (Object Relational Mapper) para Python.

Permite trabajar con bases de datos utilizando clases y objetos de Python, sin escribir directamente la mayoría de las consultas SQL.

---

## ¿Qué problema resuelve?

Hasta ahora nuestra aplicación trabajaba con datos en memoria.

Ejemplo:

```python
usuarios = []
```

Cuando la aplicación se detenía, toda la información desaparecía.

SQLAlchemy permite almacenar esa información de forma permanente en una base de datos.

---

## ¿Qué es un ORM?

ORM significa:

Object Relational Mapper

Su función es convertir automáticamente:

Objetos Python

↓

Filas de una tabla

y viceversa.

En lugar de escribir:

SELECT * FROM usuarios;

podremos trabajar con objetos Python.

---

## Relación entre Python y la Base de Datos

Cliente

↓

FastAPI

↓

SQLAlchemy (ORM)

↓

PostgreSQL

↓

Respuesta

---

## Ventajas

- Menos código SQL manual.
- Código más limpio.
- Mayor mantenimiento.
- Independencia del motor de base de datos.
- Integración completa con FastAPI.

---

## Componentes que iremos aprendiendo

- Engine
- Session
- Base
- Models
- Tablas
- CRUD
- Relaciones

---

## Idea clave

SQLAlchemy es el puente entre los objetos de Python y las tablas de la base de datos.

Hasta ahora trabajábamos con listas y diccionarios.

A partir de este punto trabajaremos con datos persistentes almacenados en PostgreSQL.

---

## Inicio de una nueva etapa

Durante este día también se reorganizó el proyecto para adoptar una arquitectura profesional.

A partir de este momento:

- Todo el código nuevo se desarrollará dentro de `App/`.
- Los apuntes permanecerán en `Apuntes/`.
- El proyecto evolucionará diariamente sobre una única aplicación.