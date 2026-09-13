from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_crear_producto():
    response = client.post(
        "/productos",
        json={
            "nombre": "Mouse",
            "precio": 100
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "nombre": "Mouse",
        "precio": 100
    }

def test_obtener_producto():
    response = client.get("/productos/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "nombre": "Laptop",
        "precio": 3000
    }

def test_producto_no_encontrado():
    response = client.get("/productos/10")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Producto no encontrado"
    }

def test_actualizar_producto():
    response = client.put(
        "/productos/1",
        json={
            "nombre": "Laptop Pro",
            "precio": 4000
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "nombre": "Laptop Pro",
        "precio": 4000
    }

def test_eliminar_producto():
    response = client.delete("/productos/1")

    assert response.status_code == 200
    assert response.json() == {
        "mensaje": "Producto eliminado"
    }

def test_producto_eliminado_no_existe():
    response = client.get("/productos/1")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Producto no encontrado"
    }