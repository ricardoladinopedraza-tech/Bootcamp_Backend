Día 79 — SQLAlchemy: flush(), rollback() y transacciones

Objetivo

Comprender cambios pendientes, errores y transacciones cuando varias operaciones deben ejecutarse como una unidad.

flush()

Envía cambios pendientes hacia la BD dentro de la transacción actual, pero no confirma la transacción. Un uso importante es obtener un id generado por la BD antes del commit.

db.add(usuario) → db.flush() → obtener usuario.id
→ crear pedido → db.add() → db.commit()

commit()

Confirma la transacción.

rollback()

Revierte la transacción pendiente cuando ocurre un error antes de confirmar.

try:
    ...
    db.commit()
except Exception:
    db.rollback()
    raise

No debemos ocultar el error.

Atomicidad

Todas las operaciones deben completarse correctamente o la transacción debe revertirse.

Crear Usuario → flush() → crear Pedido → ¿todo correcto?
NO → rollback()
SÍ → commit()

Responsabilidades

HTTPException → respuesta HTTP de error
rollback() → revierte transacción pendiente
commit() → confirma transacción

Recordatorio ORM

pedido.usuario_id → valor de la Foreign Key
pedido.usuario → objeto Usuario relacionado