from fastapi import FastAPI, HTTPException

app = FastAPI()

productos = [
    {
        "id": 1,
        "nombre": "Laptop",
        "precio": 3000
    }
]

@app.post("/productos")
def crear_producto(producto: dict):

    nuevo_producto = {
        "id": len(productos) + 1,
        "nombre": producto["nombre"],
        "precio": producto["precio"]
    }

    productos.append(nuevo_producto)

    return nuevo_producto

@app.get("/productos/{producto_id}")
def obtener_producto(producto_id: int):

    for producto in productos:
        if producto["id"] == producto_id:
            return producto

    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )

@app.put("/productos/{producto_id}")
def actualizar_producto(producto_id: int, producto_actualizado: dict):

    for producto in productos:
        if producto["id"] == producto_id:
            producto["nombre"] = producto_actualizado["nombre"]
            producto["precio"] = producto_actualizado["precio"]

            return producto

    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )

@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int):

    for producto in productos:
        if producto["id"] == producto_id:
            productos.remove(producto)

            return {
                "mensaje": "Producto eliminado"
            }

    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )