# Día 70 – Relaciones entre tablas, ForeignKey y JOIN con SQLAlchemy

## Objetivo

Comprender cómo SQLAlchemy establece relaciones entre tablas mediante ForeignKey y cómo utilizar JOIN para combinar información de diferentes tablas.

---

## 1. ForeignKey

Una ForeignKey establece una relación entre una columna de una tabla y la Primary Key de otra tabla.

En nuestro proyecto:

```python
usuario_id = Column(Integer, ForeignKey("usuarios.id"))

La relación es:

pedidos.usuario_id
        ↓
ForeignKey
        ↓
usuarios.id

La tabla usuarios contiene la Primary Key:

usuarios.id

y la tabla pedidos contiene la Foreign Key:

pedidos.usuario_id
2. Relación uno a muchos (1:N)

Un usuario puede tener muchos pedidos.

Ejemplo:

Usuario 1 → Ricardo

        ↓
        ├── Pedido 1 → laptop
        ├── Pedido 2 → mouse
        └── Pedido 3 → teclado

Los tres pedidos pueden tener:

usuario_id = 1

No se almacena nuevamente el nombre de Ricardo en cada pedido.

3. Verificación directa en SQLite

Se comprobó la estructura de la tabla pedidos:

CREATE TABLE pedidos (
    id INTEGER NOT NULL,
    producto VARCHAR,
    usuario_id INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY(usuario_id) REFERENCES usuarios (id)
)

También se verificó que los pedidos estaban almacenados:

db.execute("SELECT * FROM pedidos").fetchall()

Resultado:

[(1, 'laptop', 1),
 (2, 'mouse', 1),
 (3, 'teclado', 1)]
4. Consulta de pedidos por usuario

Se creó el endpoint:

@app.get("/pedidos/usuario/{usuario_id}")
def listar_pedidos_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    pedidos = db.query(Pedido).filter(
        Pedido.usuario_id == usuario_id
    ).all()

    return pedidos

La consulta:

db.query(Pedido).filter(
    Pedido.usuario_id == usuario_id
).all()

permite obtener todos los pedidos relacionados con un usuario.

Para:

GET /pedidos/usuario/1

se obtuvo:

[
  {
    "producto": "laptop",
    "usuario_id": 1,
    "id": 1
  },
  {
    "producto": "mouse",
    "usuario_id": 1,
    "id": 2
  },
  {
    "producto": "teclado",
    "usuario_id": 1,
    "id": 3
  }
]
5. ForeignKey vs JOIN

Conceptos fundamentales:

ForeignKey establece la relación entre las tablas.
JOIN utiliza esa relación para combinar información de las tablas.

Relación:

usuarios.id ←→ pedidos.usuario_id

JOIN:

Pedido + Usuario
6. Primer JOIN con SQLAlchemy

Se utilizó:

resultados = db.query(
    Pedido.producto,
    Usuario.nombre
).join(
    Usuario,
    Pedido.usuario_id == Usuario.id
).all()

La condición del JOIN es:

Pedido.usuario_id == Usuario.id

Conceptualmente:

pedidos.usuario_id = usuarios.id
7. Error 500 durante el JOIN

Inicialmente se intentó devolver directamente:

return resultados

Esto produjo:

500 Internal Server Error

El error no estaba en el JOIN.

Se investigó qué estaba devolviendo SQLAlchemy mediante:

print(resultados)

Resultado:

[
    ('laptop', 'Ricardo'),
    ('mouse', 'Ricardo'),
    ('teclado', 'Ricardo')
]

Se comprobó que SQLAlchemy estaba devolviendo una lista de tuplas.

8. Diferencia entre resultados

Cuando se consulta:

db.query(Pedido).all()

se obtienen objetos Pedido.

Cuando se consulta:

db.query(
    Pedido.producto,
    Usuario.nombre
).join(...)

se obtiene una lista de tuplas:

[
    ('laptop', 'Ricardo'),
    ('mouse', 'Ricardo'),
    ('teclado', 'Ricardo')
]

FastAPI no pudo serializar directamente esas filas en este caso.

9. Transformación a diccionarios

Se transformaron las tuplas mediante una comprensión de listas:

return [
    {
        "producto": producto,
        "nombre": nombre
    }
    for producto, nombre in resultados
]

Resultado final:

[
  {
    "producto": "laptop",
    "nombre": "Ricardo"
  },
  {
    "producto": "mouse",
    "nombre": "Ricardo"
  },
  {
    "producto": "teclado",
    "nombre": "Ricardo"
  }
]
10. Flujo completo aprendido
ForeignKey
    ↓
Establece la relación
    ↓
usuarios.id ←→ pedidos.usuario_id
    ↓
JOIN
    ↓
Combina información
    ↓
SQLAlchemy
    ↓
Lista de tuplas
    ↓
Diccionarios Python
    ↓
JSON
    ↓
FastAPI Response
11. Aprendizaje clave

Cuando aparece un error, primero se debe investigar qué tipo de dato se está obteniendo antes de intentar solucionarlo.

En este ejercicio:

500 Internal Server Error
        ↓
Inspección del resultado
        ↓
[('laptop', 'Ricardo'), ...]
        ↓
Identificación: lista de tuplas
        ↓
Transformación a diccionarios
        ↓
JSON válido
        ↓
200 OK

El error permitió comprender la diferencia entre objetos ORM, tuplas y estructuras serializables por FastAPI.

Mini reto de cierre
ForeignKey establece la relación entre las tablas.
JOIN utiliza esa relación para combinar información entre las tablas.
SQLAlchemy devolvió una lista de tuplas.
Fue necesario transformar las tuplas en diccionarios para producir una respuesta JSON adecuada.
ForeignKey establece la relación → JOIN combina información → JSON representa la respuesta.