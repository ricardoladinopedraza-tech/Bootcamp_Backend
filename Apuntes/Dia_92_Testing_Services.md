Día 92 — Testing de Services

Objetivo

Aprender a probar lógica de negocio de forma aislada, sin depender de FastAPI ni de PostgreSQL.

1. Service inicial

def calcular_total(precio, cantidad):
    return precio * cantidad

Test:

from services import calcular_total

def test_calcular_total():
    resultado = calcular_total(100, 3)
    assert resultado == 300

Resultado:

1 passed

2. Regla de negocio

def calcular_total(precio, cantidad):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero")

    return precio * cantidad

3. Cantidad cero

def test_cantidad_cero():
    with pytest.raises(
        ValueError,
        match="La cantidad debe ser mayor que cero"
    ):
        calcular_total(100, 0)

4. Cantidad negativa

def test_cantidad_negativa():
    with pytest.raises(
        ValueError,
        match="La cantidad debe ser mayor que cero"
    ):
        calcular_total(100, -2)

Resultado final:

3 passed

Idea fundamental

Un test unitario de service debe intentar probar la lógica de negocio de forma aislada.

service → regla de negocio → pytest → assert / pytest.raises()

Se habló conceptualmente de mocks, pero no se implementaron para no adelantar el roadmap.

Resultado

Día 92 — COMPLETADO