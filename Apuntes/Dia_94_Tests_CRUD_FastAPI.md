Día 94 — Tests de CRUD con FastAPI

Objetivo

Probar las operaciones CRUD mediante TestClient, verificando códigos HTTP, respuestas JSON y cambios de estado.

CRUD

CREATE → POST
READ   → GET
UPDATE → PUT
DELETE → DELETE

Para concentrarnos en testing, se utilizó una lista en memoria.

1. Estado inicial

productos = [
    {
        "id": 1,
        "nombre": "Laptop",
        "precio": 3000
    }
]

2. CREATE — POST

Se creó POST /productos.

Test:

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

3. READ — GET

Se creó GET /productos/{producto_id}.

Test exitoso:

def test_obtener_producto():
    response = client.get("/productos/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "nombre": "Laptop",
        "precio": 3000
    }

Test de recurso inexistente:

def test_producto_no_encontrado():
    response = client.get("/productos/10")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Producto no encontrado"
    }

4. UPDATE — PUT

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

El ID se mantiene; solo cambian los atributos.

5. DELETE

def test_eliminar_producto():
    response = client.delete("/productos/1")

    assert response.status_code == 200
    assert response.json() == {
        "mensaje": "Producto eliminado"
    }

Verificación posterior:

def test_producto_eliminado_no_existe():
    response = client.get("/productos/1")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Producto no encontrado"
    }

Resultado:

6 passed

6. Estado compartido

Los tests usan una misma lista mutable. Un test puede cambiar el estado que otro test observa.

Regla importante:

Idealmente, cada test debería poder ejecutarse de forma independiente.

No se profundizó todavía en fixtures ni aislamiento avanzado para respetar el roadmap.

Resultado

Día 94 — COMPLETADO