from fastapi.testclient import TestClient
from sqlalchemy import text, inspect

from App.main import app, get_db
from App.database.database import Base
from test.test_database import TestingSessionLocal, test_engine

from App.models.usuario import Usuario

def get_db_override():
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = get_db_override

client = TestClient(app)

def test_ruta_inexistente():
    response = client.get("/")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Not Found"
    }

def test_conexion_base_de_prueba():
    db = TestingSessionLocal()

    try:
        nombre_bd = db.execute(
            text("SELECT current_database();")
        ).scalar()

        print(nombre_bd)

        assert nombre_bd == "bootcamp_backend_test"

    finally:
        db.close()

def test_crear_tablas_base_prueba():
    Base.metadata.create_all(bind=test_engine)

    inspector = inspect(test_engine)
    tablas = inspector.get_table_names()

    print(tablas)

    assert "usuarios" in tablas
    assert "pedidos" in tablas

def test_crear_usuario_en_base_prueba():
    db = TestingSessionLocal()

    try:
        usuario = Usuario(
            nombre="Usuario Test",
            correo="test@correo.com"
        )

        db.add(usuario)
        db.commit()
        db.refresh(usuario)

        print(usuario.id)
        print(usuario.nombre)

        assert usuario.nombre == "Usuario Test"
        assert usuario.correo == "test@correo.com"

    finally:
        db.close()

def test_endpoint_obtener_usuario():
    db = TestingSessionLocal()

    usuario = Usuario(
        nombre="Endpoint Test",
        correo="endpoint@test.com"
    )

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    usuario_id = usuario.id

    db.close()

    response = client.get(f"/usuarios/{usuario_id}")

    print(response.status_code)
    print(response.json())

    assert response.status_code == 200

    assert response.json() == {
        "id": usuario_id,
        "nombre": "Endpoint Test",
        "correo": "endpoint@test.com",
        "telefono": None,
        "ciudad": None
    }

def test_usuario_no_encontrado():
    response = client.get("/usuarios/99999")

    print(response.status_code)
    print(response.json())

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Usuario no encontrado"
    }