def calcular_total(precio, cantidad):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero")

    return precio * cantidad