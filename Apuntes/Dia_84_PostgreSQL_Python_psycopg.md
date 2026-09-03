Día 84 — PostgreSQL + Python: conexión

Objetivo

Comprender cómo Python se comunica con PostgreSQL y qué función cumple psycopg.

psycopg

psycopg es el driver que permite que Python se comunique con PostgreSQL.

Python
  ↓
psycopg
  ↓
PostgreSQL

SQLAlchemy + psycopg

Nuestro proyecto utiliza SQLAlchemy como ORM y psycopg como driver:

FastAPI
   ↓
SQLAlchemy
   ↓
psycopg
   ↓
PostgreSQL
   ↓
bootcamp_backend

SQLAlchemy proporciona la capa ORM; psycopg proporciona la comunicación con PostgreSQL.

URL de conexión

postgresql+psycopg://usuario:contraseña@localhost:5432/bootcamp_backend

postgresql → motor

psycopg → driver

usuario/contraseña → autenticación de PostgreSQL

localhost → servidor local

5432 → puerto

bootcamp_backend → base de datos

La contraseña es información sensible y posteriormente se gestionará mediante variables de entorno.

Usuario PostgreSQL vs usuario de aplicación

Usuario PostgreSQL ≠ Usuario de la aplicación

El primero participa en la conexión y permisos de PostgreSQL; el segundo es un registro de la tabla usuarios.

Cambio conceptual

Antes:

FastAPI → SQLAlchemy → SQLite → app.db

Ahora:

FastAPI → SQLAlchemy → psycopg → PostgreSQL → bootcamp_backend

Idea clave

SQLAlchemy es la capa ORM; psycopg es el driver que permite la comunicación con PostgreSQL.

Estado

Día 84 completado.