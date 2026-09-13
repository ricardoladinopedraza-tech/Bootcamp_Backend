Día 88 — Migraciones reales con Alembic

Objetivo

Aprender a modificar la estructura de una tabla existente de PostgreSQL mediante una migración controlada y versionada, sin eliminar ni recrear la tabla.

Punto de partida

Al finalizar el Día 87:

PostgreSQL estaba configurado como base de datos.

SQLAlchemy y psycopg estaban conectados.

.env proporcionaba DATABASE_URL.

Alembic estaba inicializado y conectado.

Cadena de migraciones:
3965e7b974fd → d8848d64e7cc (HEAD).

usuarios contenía id, nombre, correo y telefono.

1. Migración real

Una migración real modifica una estructura de base de datos que ya existe. El objetivo es hacer cambios controlados y versionados, evitando borrar y recrear tablas.

2. create_all() vs Alembic

Base.metadata.create_all() crea tablas que no existen. No constituye un sistema completo de migraciones.
Alembic permite registrar y aplicar cambios de esquema a lo largo del tiempo.

3. revision --autogenerate vs upgrade

alembic revision --autogenerate compara el modelo SQLAlchemy con la estructura de la base de datos y genera un archivo de migración. No ejecuta el cambio.

alembic upgrade head ejecuta las migraciones pendientes y modifica PostgreSQL.

Flujo:

Modelo → revision --autogenerate → archivo de migración → revisión → upgrade head → PostgreSQL

4. Ejercicio

Se agregó al modelo Usuario:

telefono = Column(String)
ciudad = Column(String)

Antes de aplicar la migración, PostgreSQL tenía:

id
nombre
correo
telefono

El modelo tenía además ciudad.

5. Generación

Se ejecutó:

alembic revision --autogenerate -m "agregar ciudad a usuarios"

Alembic detectó:

Detected added column 'usuarios.ciudad'

y generó:

alembic/versions/47e20a3d7e7f_agregar_ciudad_a_usuarios.py

6. Revisión de la migración

La migración contenía esencialmente:

def upgrade() -> None:
    op.add_column(
        'usuarios',
        sa.Column('ciudad', sa.String(), nullable=True)
    )

def downgrade() -> None:
    op.drop_column('usuarios', 'ciudad')

upgrade() agrega ciudad; downgrade() la elimina.

La cadena quedó:

3965e7b974fd
      ↓
d8848d64e7cc
      ↓
47e20a3d7e7f (HEAD)

7. Aplicación

Se ejecutó:

alembic upgrade head

Resultado:

Running upgrade d8848d64e7cc -> 47e20a3d7e7f, agregar ciudad a usuarios

8. Verificación física

En PostgreSQL:

\d usuarios

se comprobó:

id
nombre
correo
telefono
ciudad

También se verificó que la Foreign Key de pedidos.usuario_id hacia usuarios.id permaneció intacta.

9. Estado de Alembic

Se ejecutó:

alembic current

Resultado:

47e20a3d7e7f (head)

10. Conceptos fundamentales

revision --autogenerate: detecta diferencias y genera una migración.

upgrade(): define el cambio hacia adelante.

downgrade(): define el cambio hacia atrás.

upgrade head: aplica las migraciones pendientes.

current: muestra la revisión aplicada actualmente.

Regla mental:

CAMBIO EN MODELO
      ↓
revision --autogenerate
      ↓
MIGRACIÓN
      ↓
REVISIÓN
      ↓
upgrade head
      ↓
CAMBIO REAL EN POSTGRESQL
      ↓
VERIFICACIÓN

Resultado

Día 88 — COMPLETADO

Se aprendió a generar, revisar, aplicar y verificar una migración real sobre una tabla existente.