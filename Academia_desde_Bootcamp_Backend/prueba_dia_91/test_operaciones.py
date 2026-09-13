from operaciones import sumar, restar, dividir
import pytest

def test_sumar():
    resultado = sumar(2, 3)

    assert resultado == 5


def test_sumar_numeros_negativos():
    resultado = sumar(-2, -3)

    assert resultado == -5


def test_restar():
    resultado = restar(10, 4)

    assert resultado == 6

def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)