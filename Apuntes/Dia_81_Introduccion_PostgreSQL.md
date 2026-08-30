Día 81 — Introducción a PostgreSQL

Objetivo

Comprender la arquitectura básica de PostgreSQL y su relación con FastAPI + SQLAlchemy.

PostgreSQL

PostgreSQL es un sistema gestor de bases de datos relacional.

Servidor

El servidor PostgreSQL recibe conexiones y administra bases de datos.

Base de datos

Una base de datos está dentro del servidor y contiene estructuras como tablas.

Tablas y registros

Para nuestro proyecto:

PostgreSQL Server
      ↓
bootcamp_backend
      ↓
usuarios / pedidos
      ↓
registros

bootcamp_backend es una base de datos; usuarios es una tabla; Ricardo es un registro de nuestra aplicación.

Usuario PostgreSQL vs usuario de aplicación

Usuario/rol PostgreSQL ≠ Usuario de nuestra aplicación

El primero participa en autenticación/permisos de PostgreSQL. El segundo es un registro de la tabla usuarios.

Arquitectura

FastAPI
   ↓
SQLAlchemy
   ↓
Conexión
   ↓
PostgreSQL Server
   ↓
Base de datos
   ↓
Tablas
   ↓
Registros

Actualmente:

FastAPI → SQLAlchemy → SQLite → app.db

Posteriormente:

FastAPI → SQLAlchemy → PostgreSQL → bootcamp_backend

No se modificó todavía el proyecto; primero se consolidó el modelo mental.