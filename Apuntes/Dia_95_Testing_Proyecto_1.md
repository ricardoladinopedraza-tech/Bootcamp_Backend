Día 95 ---  Testing del Proyecto 1

Objetivo

Aplicar al Proyecto 1 real lo aprendido en los Días 91--94, probando
endpoints FastAPI con TestClient sin modificar los datos de la base
real bootcamp_backend.

Problema identificado

Los endpoints del proyecto obtienen una sesión mediante:

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Si un test utilizara directamente esa dependencia, podría ejecutar
INSERT, UPDATE o DELETE sobre la base real.

Por ello se decidió separar completamente el entorno:

Aplicación normal
    ↓
get_db
    ↓
SessionLocal
    ↓
bootcamp_backend

Testing
    ↓
get_db_override
    ↓
TestingSessionLocal
    ↓
bootcamp_backend_test

Base de datos de testing

Se creó en PostgreSQL:

CREATE DATABASE bootcamp_backend_test;

Se verificó que coexistieran:

bootcamp_backend
bootcamp_backend_test

Conexión exclusiva para tests

Se creó test/test_database.py con un test_engine y
TestingSessionLocal apuntando exclusivamente a
bootcamp_backend_test.

La conexión se comprobó desde Python y posteriormente con SQL:

SELECT current_database();

Resultado:

bootcamp_backend_test

Organización de los tests

La estructura quedó separada del código de la aplicación:

Bootcamp_Banckend/
├── App/
│   ├── __init__.py
│   ├── main.py
│   └── ...
├── test/
│   ├── __init__.py
│   ├── test_database.py
│   └── test_main.py
└── ...

Se aprendió también que __init__.py permite tratar la carpeta como
paquete para resolver imports.

Dependency Override

Se creó una dependencia de testing:

def get_db_override():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

y se indicó a FastAPI que durante los tests sustituya get_db:

app.dependency_overrides[get_db] = get_db_override

Conceptualmente:

TestClient
    ↓
FastAPI
    ↓
Depends(get_db)
    ↓
dependency_overrides
    ↓
get_db_override()
    ↓
TestingSessionLocal
    ↓
bootcamp_backend_test

Preparación de tablas

Como la base de testing estaba vacía, se creó únicamente allí la
estructura ORM:

Base.metadata.create_all(bind=test_engine)

Se verificaron las tablas mediante inspect(test_engine):

['usuarios', 'pedidos']

Esto no reactivó Base.metadata.create_all(bind=engine) en la
aplicación real; PostgreSQL real continúa gestionado mediante Alembic.

Pruebas realizadas

1. TestClient

Se comprobó una ruta inexistente /:

assert response.status_code == 404
assert response.json() == {"detail": "Not Found"}

2. Conexión a la base de testing

Se comprobó que TestingSessionLocal llegara a:

bootcamp_backend_test

3. Existencia de tablas

Se verificó que existieran:

usuarios
pedidos

4. Inserción controlada

Se creó un Usuario Test directamente con TestingSessionLocal,
confirmando que los datos de prueba se almacenan en la base de testing.

5. Endpoint real con base de testing

Se creó un usuario:

Endpoint Test
endpoint@test.com

y se consultó mediante:

GET /usuarios/{usuario_id}

El endpoint respondió 200 y devolvió el usuario creado en
bootcamp_backend_test. Esto demostró que el dependency override
funciona realmente.

Se verificaron automáticamente status_code y JSON mediante assert.

6. Caso 404

Se probó:

GET /usuarios/99999

Resultado:

{"detail": "Usuario no encontrado"}

con código HTTP 404.

Resultado final

collected 6 items
6 passed

Concepto adicional detectado

Los IDs de prueba fueron aumentando entre ejecuciones porque los tests
actuales dejan registros persistidos en bootcamp_backend_test.

Esto permitió reconocer un principio importante:

Idealmente, los tests deben ejecutarse de manera aislada y no depender
del estado dejado por ejecuciones anteriores.

La limpieza automática, fixtures y aislamiento avanzado se dejan para
una etapa posterior para no profundizar fuera del objetivo del Día 95.

Conclusión

El Proyecto 1 ya puede probar endpoints reales de FastAPI contra una
base PostgreSQL separada y segura.

Se consolidaron:

pytest

TestClient

base PostgreSQL exclusiva para testing

TestingSessionLocal

dependency_overrides

creación de estructura en la base de prueba

pruebas de endpoints con datos controlados

validación de respuestas 200 y 404

protección de la información de la base real

Estado: COMPLETADO.