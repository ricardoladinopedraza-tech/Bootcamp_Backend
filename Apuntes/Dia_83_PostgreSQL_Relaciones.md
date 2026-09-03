Día 83 — PostgreSQL: Relaciones entre tablas

Objetivo

Comprender Primary Key (PK), Foreign Key (FK), JOIN y cardinalidad.

Primary Key

La PK identifica de forma única cada registro de una tabla.

usuarios
id (PK) | nombre
1       | Ricardo
2       | Ana

Foreign Key

La FK referencia una PK de otra tabla y establece la relación a nivel de base de datos.

usuarios.id
     ↑
     │
pedidos.usuario_id (FK)

En SQLAlchemy:

usuario_id = Column(Integer, ForeignKey("usuarios.id"))

JOIN

JOIN combina información de tablas relacionadas dentro de una consulta SQL.

SELECT pedidos.producto, usuarios.nombre
FROM pedidos
JOIN usuarios ON pedidos.usuario_id = usuarios.id;

Cardinalidad

Describe cuántos registros pueden relacionarse.

Nuestro proyecto:

Usuario 1 ─────────── N Pedido

Es una relación 1. Un usuario puede tener cero, uno o muchos pedidos.

Diferencias fundamentales

PK → identifica un registro
FK → referencia un registro de otra tabla
JOIN → combina información en una consulta
Cardinalidad → describe cuántos registros pueden relacionarse

Relación con SQLAlchemy

ForeignKey()
    ↓
Relación en la BD

relationship()
    ↓
Relación ORM entre objetos Python

JOIN
    ↓
Operación de consulta SQL

Estos conceptos están relacionados, pero no son lo mismo.

Estado

Día 83 completado.