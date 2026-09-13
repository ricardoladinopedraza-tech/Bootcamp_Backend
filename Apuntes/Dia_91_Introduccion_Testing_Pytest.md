Día 91 — Introducción a Testing con pytest

Objetivo

Comprender qué es un test automatizado, para qué sirve pytest, cómo funciona assert y cómo probar funciones pequeñas.

1. Testing

Los tests comprueban automáticamente que el código continúa comportándose como esperamos y ayudan a detectar regresiones.

2. pytest

pytest

3. assert

assert resultado == 5

Significa: esta condición debe ser verdadera.

verdadera → PASS
falsa    → FAIL

4. Primer ejercicio

operaciones.py:

def sumar(a, b):
    return a + b

test_operaciones.py:

from operaciones import sumar

def test_sumar():
    resultado = sumar(2, 3)
    assert resultado == 5

Resultado:

1 passed

5. Fallo intencional

Se cambió temporalmente a:

assert resultado == 10

Pytest mostró:

assert 5 == 10

6. Excepciones esperadas

def dividir(a, b):
    return a / b

import pytest

def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)

Una excepción esperada puede representar un test exitoso.

Al cambiar temporalmente a dividir(10, 2), pytest mostró:

Failed: DID NOT RAISE ZeroDivisionError

Modelo mental

FUNCIÓN → resultado → ASSERT → PASS / FAIL

Para excepciones:

FUNCIÓN → excepción esperada → pytest.raises() → PASS

Resultado

Día 91 — COMPLETADO