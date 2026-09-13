Día 89 — Migración definitiva del Proyecto 1: SQLite → PostgreSQL

Objetivo

Migrar los datos reales del Proyecto 1 desde SQLite (app.db) hacia PostgreSQL (bootcamp_backend), conservando IDs y relaciones, y dejar PostgreSQL como base de datos definitiva del proyecto.

Punto de partida

La estructura ya existía en PostgreSQL gracias a SQLAlchemy y Alembic.

Tabla usuarios

id
nombre
correo
telefono
ciudad

Tabla pedidos

id
producto
usuario_id

La Foreign Key permanecía activa:

pedidos.usuario_id → usuarios.id

1. Datos existentes en SQLite

usuarios

(1, 'Ricardo', 'ricardol@correo.com')
(2, 'Ana', 'ana@correo.com')
(3, 'Ricardo', 'ricardo@nuevo.com')

pedidos

(1, 'laptop', 1)
(2, 'mouse', 1)
(3, 'teclado', 1)

SQLite no contenía todavía los campos telefono y ciudad.

2. Migración de usuarios

INSERT INTO usuarios (id, nombre, correo)
VALUES
(1, 'Ricardo', 'ricardol@correo.com'),
(2, 'Ana', 'ana@correo.com'),
(3, 'Ricardo', 'ricardo@nuevo.com');

3. Migración de pedidos

INSERT INTO pedidos (id, producto, usuario_id)
VALUES
(1, 'laptop', 1),
(2, 'mouse', 1),
(3, 'teclado', 1);

4. Sincronización de secuencias

Al insertar IDs manualmente, las secuencias automáticas podían quedar desactualizadas.

SELECT setval('usuarios_id_seq', 3);
SELECT setval('pedidos_id_seq', 3);

Así, el siguiente ID automático quedó listo para ser 4.

5. Verificación de relaciones

Se comprobó mediante JOIN:

laptop  → Ricardo
mouse   → Ricardo
teclado → Ricardo

Y mediante LEFT JOIN:

Ricardo (id 1) → 3 pedidos
Ana     (id 2) → 0 pedidos
Ricardo (id 3) → 0 pedidos

6. PostgreSQL como base definitiva

En App/main.py se dejó:

# Base.metadata.create_all(bind=engine)

A partir de este punto, la evolución del esquema queda gestionada mediante Alembic.

7. Verificación desde FastAPI

Se inició:

uvicorn App.main:app --reload

Resultado:

Application startup complete.

GET /usuarios devolvió los usuarios migrados. Los campos telefono y ciudad aparecieron como null.

GET /pedidos/1 devolvió:

{
  "id": 1,
  "producto": "laptop",
  "usuario": {
    "id": 1,
    "nombre": "Ricardo",
    "correo": "ricardol@correo.com"
  }
}

8. Prueba de ID automático

Se creó un nuevo usuario Carlos y PostgreSQL generó:

id = 4

Esto confirmó que las secuencias quedaron correctamente sincronizadas.

Conceptos clave

create_all() → crea estructura, no migra datos
Alembic      → versiona cambios de estructura
INSERT       → transfiere registros
setval()     → sincroniza secuencias
ForeignKey   → conserva integridad de relaciones

Resultado

Día 89 — COMPLETADO