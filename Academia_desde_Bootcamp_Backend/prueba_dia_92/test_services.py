from services import calcular_total
import pytest

def test_calcular_total():
    resultado = calcular_total(100, 3)
    assert resultado == 300

def test_cantidad_cero():
    with pytest.raises(ValueError, match="La cantidad debe ser mayor que cero"):
        calcular_total(100, 0)

def test_cantidad_negativa():
    with pytest.raises(ValueError, match="La cantidad debe ser mayor que cero"):
        calcular_total(100, -2)