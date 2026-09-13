Día 93 — Testing de endpoints con FastAPI + TestClient

Objetivo

Aprender a probar endpoints FastAPI simulando peticiones HTTP mediante TestClient.

1. Secuencia de aprendizaje

Día 91 → función
Día 92 → service
Día 93 → endpoint HTTP

2. TestClient

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

Permite:

response = client.get("/")

y comprobar:

response.status_code
response.json()

3. Endpoint inicial

@app.get("/")
def inicio():
    return {"mensaje": "Hola desde FastAPI"}

Test:

def test_inicio():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "mensaje": "Hola desde FastAPI"
    }

4. Path Parameter

@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int):
    if usuario_id != 5:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return {
        "id": usuario_id,
        "nombre": "Ricardo"
    }

5. Usuario existente

def test_obtener_usuario():
    response = client.get("/usuarios/5")

    assert response.status_code == 200
    assert response.json() == {
        "id": 5,
        "nombre": "Ricardo"
    }

6. ID inválido — 422

def test_usuario_id_invalido():
    response = client.get("/usuarios/abc")

    assert response.status_code == 422

FastAPI intenta convertir "abc" a int; como no puede, responde 422 antes de ejecutar el endpoint.

7. Recurso inexistente — 404

def test_usuario_no_encontrado():
    response = client.get("/usuarios/10")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Usuario no encontrado"
    }

422 → formato/tipo inválido
404 → dato válido, recurso inexistente

8. Resultado final

4 passed, 2 warnings

Las warnings observadas no fueron fallos.

Modelo mental

TestClient
    ↓
HTTP request
    ↓
FastAPI
    ↓
endpoint
    ↓
HTTP response
    ↓
status_code / json()
    ↓
assert

Resultado

Día 93 — COMPLETADO