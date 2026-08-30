Día 78 — SQLAlchemy: add(), commit() y refresh()

Objetivo

Comprender el flujo de creación de un registro y diferenciar Pydantic, SQLAlchemy y la sesión de BD.

Pydantic vs SQLAlchemy

UsuarioCreate es un modelo Pydantic: recibe y valida datos.
Usuario es un modelo ORM de SQLAlchemy: representa un registro de la tabla.

db.add()

Agrega el objeto ORM a la sesión. No confirma la transacción.

db.commit()

Confirma la transacción pendiente.

db.refresh()

Recarga desde la BD los valores actuales del objeto ORM. Es útil cuando la BD genera valores como el id.

Flujo

JSON → FastAPI/Pydantic → UsuarioCreate → SQLAlchemy → Usuario ORM
→ db.add() → db.commit() → db.refresh() → Response

Idea clave

Pydantic → datos de entrada/validación
SQLAlchemy → objeto ORM
db.add() → agrega a la sesión
db.commit() → confirma
db.refresh() → recarga valores actuales desde BD