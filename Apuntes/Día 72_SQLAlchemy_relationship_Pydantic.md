Día 72 — SQLAlchemy ORM: relationship() y respuestas anidadas con Pydantic

Objetivo

Comprender y comprobar en la práctica cómo SQLAlchemy navega una relación ORM entre Pedido y Usuario, y cómo Pydantic transforma esa relación en una respuesta JSON anidada.

1. Consulta de pedidos

Partimos de:

pedidos = db.query(Pedido).all()

Esto devuelve una colección de objetos Pedido:

[Pedido, Pedido, Pedido]

Cada objeto Pedido tiene disponible:

pedido.usuario

gracias a relationship().

Por tanto podemos navegar:

Pedido → Usuario

2. Pydantic construyó el objeto anidado

Nuestro modelo:

class PedidoDetalleResponse(BaseModel):
    id: int
    producto: str
    usuario: UsuarioPedidoResponse

    model_config = {
        "from_attributes": True
    }

El campo:

usuario: UsuarioPedidoResponse

indica que la respuesta contiene un objeto usuario anidado.

Con:

from_attributes=True

Pydantic puede construir el modelo utilizando los atributos del objeto ORM.

El resultado fue conceptualmente:

{
    "id": 1,
    "producto": "laptop",
    "usuario": {
        "id": 1,
        "nombre": "Ricardo",
        "correo": "ricardol@correo.com"
    }
}

Esto demuestra:

Pedido
   ↓
pedido.usuario
   ↓
Usuario
   ↓
Pydantic
   ↓
JSON anidado

3. Comparación: JOIN vs relationship()

Con JOIN

El endpoint anterior producía:

[
    {
        "producto": "laptop",
        "nombre": "Ricardo"
    },
    {
        "producto": "mouse",
        "nombre": "Ricardo"
    }
]

Flujo conceptual:

SQL
 ↓
JOIN
 ↓
tuplas
 ↓
diccionarios
 ↓
JSON

Con relationship()

El nuevo endpoint produce:

[
    {
        "id": 1,
        "producto": "laptop",
        "usuario": {
            "id": 1,
            "nombre": "Ricardo",
            "correo": "ricardol@correo.com"
        }
    }
]

Flujo conceptual:

SQLAlchemy
 ↓
Pedido
 ↓
pedido.usuario
 ↓
Usuario
 ↓
Pydantic
 ↓
JSON anidado

Diferencia importante

JOIN es una operación de consulta SQL.

relationship() representa una relación entre objetos ORM y permite navegar entre ellos.

4. Distinción fundamental: usuario_id vs usuario

No debemos confundir:

pedido.usuario_id

con:

pedido.usuario

pedido.usuario_id

Es el valor de la Foreign Key.

Ejemplo:

1

Es un dato.

pedido.usuario

Es el objeto Usuario relacionado mediante relationship().

Conceptualmente:

Usuario(...)

Por eso:

pedido.usuario.nombre

significa navegar:

Pedido
   ↓
Usuario
   ↓
nombre

Esta distinción debe conservarse como referencia fundamental para futuras revisiones de SQLAlchemy.

5. Navegación bidireccional

La relación permite navegar en ambos sentidos.

Desde Usuario:

usuario.pedidos

obtenemos la lista de pedidos.

Desde Pedido:

pedido.usuario

obtenemos el usuario relacionado.

Conceptualmente:

Usuario
   │
   └── pedidos → [Pedido, Pedido, Pedido]
                         │
                         └── usuario → Usuario

6. Error observado en FastAPI

Al utilizar:

/pedidos/detalle-orm

FastAPI inicialmente intentó interpretarlo como:

/pedidos/{pedido_id}

Como pedido_id estaba declarado como entero, intentó convertir:

detalle-orm

a int.

Esto produjo:

Input should be a valid integer

Lección

Los errores de FastAPI permiten reconstruir qué creyó el framework que estábamos solicitando.

No se trata solamente de corregir el error: debemos leerlo para comprender la interpretación que hizo FastAPI.

7. Mini reto final

Suponiendo que usuario es Ricardo y tiene tres pedidos:

A

usuario.pedidos

Respuesta:

Lista de los 3 pedidos de Ricardo.

B

usuario.pedidos[1]

Respuesta:

El segundo pedido.

C

usuario.pedidos[1].producto

Respuesta:

El producto del segundo pedido.

D

usuario.pedidos[1].usuario

Respuesta:

El objeto Usuario correspondiente al segundo pedido.

E

usuario.pedidos[1].usuario.nombre

Respuesta:

El nombre del usuario del segundo pedido: Ricardo.

F

usuario.pedidos[1].usuario_id

Respuesta:

El valor de la Foreign Key del segundo pedido.

G

Diferencia fundamental:

pedido.usuario_id
    ↓
valor de la Foreign Key

pedido.usuario
    ↓
objeto Usuario relacionado mediante relationship()

Resumen del Día 72

La idea central es:

usuario.pedidos
      ↓
lista de Pedido
      ↓
pedido.usuario
      ↓
objeto Usuario
      ↓
usuario.nombre

Y la distinción que debemos recordar:

pedido.usuario_id → dato / Foreign Key

pedido.usuario    → objeto ORM relacionado

También consolidamos:

relationship()

navegación ORM

navegación bidireccional

modelos Pydantic anidados

from_attributes=True

respuestas JSON anidadas

diferencia conceptual entre JOIN y relationship()

interpretación de errores de parámetros de ruta en FastAPI

Estado

Día 72 completado.