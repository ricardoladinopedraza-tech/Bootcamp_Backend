Día 90 — Repaso PostgreSQL + SQLAlchemy

Objetivo

Consolidar los conceptos estudiados desde SQLAlchemy hasta PostgreSQL antes de iniciar Testing.

1. Flujo completo de una petición

GET /usuarios/1
      ↓
FastAPI
      ↓
SQLAlchemy
      ↓
psycopg
      ↓
PostgreSQL
      ↓
bootcamp_backend
      ↓
tabla usuarios

La respuesta vuelve en sentido contrario hasta el cliente.

2. pedido.usuario_id vs pedido.usuario

pedido.usuario_id → valor de la Foreign Key
pedido.usuario    → objeto Usuario relacionado

3. ForeignKey() vs relationship()

ForeignKey()    → relación a nivel de base de datos
relationship() → relación entre objetos ORM

4. psycopg

FastAPI → SQLAlchemy → psycopg → PostgreSQL

psycopg es el driver que permite la comunicación entre Python/SQLAlchemy y PostgreSQL.

5. create_all() vs Alembic

create_all() → crea tablas inexistentes
Alembic      → versiona y aplica cambios de estructura

6. Secuencias

Después de insertar IDs manualmente se sincronizaron las secuencias para que el siguiente ID fuera 4.

7. Transacciones

flush()    → envía cambios pendientes sin cerrar la transacción
commit()   → confirma la transacción
rollback() → revierte la transacción pendiente
refresh()  → recarga valores actuales de la BD

Ejercicio integrador:

nuevo_usuario = Usuario(
    nombre="Carlos",
    correo="carlos@correo.com"
)

db.add(nuevo_usuario)
db.flush()

nuevo_pedido = Pedido(
    producto="Laptop",
    usuario_id=nuevo_usuario.id
)

db.add(nuevo_pedido)
db.commit()

Un solo commit() confirma ambas operaciones.

8. N+1

Para 500 usuarios, un lazy loading mal usado puede producir aproximadamente:

1 consulta de usuarios + 500 consultas de pedidos = 501 consultas

Con selectinload() puede reducirse aproximadamente a 2 consultas.

9. join() vs joinedload()

join()       → participa en la construcción de la consulta
joinedload() → controla carga anticipada de una relación ORM

10. Métodos de resultado

.all()         → todos
.first()       → primero o None
.one()         → exactamente uno
.one_or_none() → cero o uno

11. SQLAlchemy vs Pydantic

SQLAlchemy → objetos ORM / base de datos
Pydantic   → validación y estructura de entrada/salida

Resultado

Día 90 — COMPLETADO