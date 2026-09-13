from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_inicio():
    response = client.get("/")

    print(response.status_code)
    print(response.json())

    assert response.status_code == 200
    assert response.json() == {"mensaje": "Hola desde FastAPI"}

def test_obtener_usuario():
    response = client.get("/usuarios/5")

    assert response.status_code == 200
    assert response.json() == {
        "id": 5,
        "nombre": "Ricardito"
    }

# Test con error de id abc
'''
def test_obtener_usuario():
    response = client.get("/usuarios/abc")

    assert response.status_code == 200
    assert response.json() == {
        "id": abc,
        "nombre": "Ricardo"
    }
'''

def test_usuario_id_invalido():
    response = client.get("/usuarios/abc")

    print(response.status_code)
    print(response.json())

    assert response.status_code == 422

def test_usuario_no_encontrado():
    response = client.get("/usuarios/10")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Usuario no encontrado"
    }