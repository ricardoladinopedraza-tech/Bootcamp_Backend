Día 71 – Relationship en SQLAlchemy

Objetivo

Comprender cómo SQLAlchemy ORM representa y permite trabajar con relaciones entre tablas mediante ForeignKey, relationship() y back_populates.

Este día fue considerado especialmente importante porque el concepto de relaciones ORM resultó más complejo que otros temas y debe conservarse como material de revisión.

1. ForeignKey

Una ForeignKey establece la relación a nivel de base de datos.

En nuestro proyecto:

usuario_id = Column(
    Integer,
    ForeignKey("usuarios.id")
)

Esto significa:

pedidos.usuario_id
        ↓
usuarios.id

usuarios.id es la Primary Key y pedidos.usuario_id es la Foreign Key.

La Foreign Key almacena el identificador del usuario relacionado.

2. relationship()

relationship() permite trabajar con la relación directamente desde los objetos Python.

En Pedido:

usuario = relationship(
    "Usuario",
    back_populates="pedidos"
)

En Usuario:

pedidos = relationship(
    "Pedido",
    back_populates="usuario"
)

Esto crea una relación bidireccional a nivel del ORM.

Podemos navegar:

pedido.usuario

para obtener el objeto Usuario relacionado.

Y:

usuario.pedidos

para obtener los objetos Pedido relacionados.

3. Diferencia fundamental: usuario_id vs usuario

Esta fue una de las partes más importantes del día.

pedido.usuario_id

Representa el valor de la Foreign Key:

pedido.usuario_id

Ejemplo:

1

Es un identificador.

pedido.usuario

Representa el objeto Usuario relacionado:

pedido.usuario

Por ejemplo:

Usuario(id=1, nombre="Ricardo", ...)

Por eso podemos hacer:

pedido.usuario.nombre

y obtener:

Ricardo

Resumen:

pedido.usuario_id
        ↓
        1

pedido.usuario
        ↓
Objeto Usuario
        ↓
pedido.usuario.nombre
        ↓
"Ricardo"

usuario_id es el dato que identifica la relación; usuario es el objeto que representa esa relación en Python.

4. Prueba práctica de navegación ORM

Se consultaron los pedidos:

pedidos = db.query(Pedido).all()

y se recorrieron:

for pedido in pedidos:
    print(pedido.producto, "->", pedido.usuario.nombre)

Resultado:

laptop -> Ricardo
mouse -> Ricardo
teclado -> Ricardo

Esto demostró que no era necesario realizar manualmente otra consulta a Usuario.

SQLAlchemy utilizó la relación definida mediante relationship().

5. Creación de un Pedido utilizando un objeto Usuario

Se realizó una prueba:

usuario = db.query(Usuario).filter(
    Usuario.id == 2
).first()

pedido = Pedido(
    producto="celular",
    usuario=usuario
)

La relación podía utilizarse inmediatamente:

pedido.usuario.nombre

Resultado:

Ana

Esto demuestra que la relación ORM puede existir en memoria antes de confirmar la transacción.

6. db.add(), flush() y commit()

Se comprobó experimentalmente la diferencia.

Primero:

pedido.usuario_id

no tenía todavía el valor sincronizado.

Después:

db.add(pedido)

el objeto pasó a formar parte de la sesión, pero la Foreign Key todavía no se había sincronizado en el objeto.

Luego:

db.flush()

y:

pedido.usuario_id

devolvió:

2

Conceptualmente:

relationship()
      ↓
relación entre objetos Python

db.add()
      ↓
objeto gestionado por la sesión

db.flush()
      ↓
sincronización de cambios con la transacción

db.commit()
      ↓
confirmación definitiva de la transacción

Importante:

flush() no equivale a commit().

flush() sincroniza los cambios con la transacción actual; commit() confirma la transacción.

La prueba se terminó con rollback() para no guardar el pedido de prueba.

7. back_populates

back_populates conecta ambos lados de la relación.

En Pedido:

usuario = relationship(
    "Usuario",
    back_populates="pedidos"
)

En Usuario:

pedidos = relationship(
    "Pedido",
    back_populates="usuario"
)

De esta manera:

Usuario
   │
   │ pedidos
   ↓
Pedido
   │
   │ usuario
   ↓
Usuario

8. Error encontrado durante el día

Al realizar una prueba apareció:

sqlalchemy.exc.InvalidRequestError:
When initializing mapper Mapper[Usuario(usuarios)],
expression 'Pedido' failed to locate a name ('Pedido')

La causa estaba relacionada con que SQLAlchemy necesitaba conocer las clases relacionadas para configurar correctamente el mapper.

La solución fue importar ambos modelos antes de realizar la consulta:

from App.models.usuario import Usuario
from App.models.pedido import Pedido

Esto permitió posteriormente utilizar:

usuario.pedidos

correctamente.

9. Error de FastAPI y JOIN

En sesiones anteriores se había encontrado también un error al devolver directamente las tuplas producidas por una consulta SQL/JOIN.

FastAPI esperaba estructuras que pudiera serializar correctamente a JSON.

La solución fue transformar los resultados en diccionarios:

resultado.append({
    "producto": pedido.producto,
    "nombre": pedido.usuario.nombre
})

Resultado:

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

10. ForeignKey vs relationship vs JOIN

Es importante no confundirlos.

ForeignKey

Establece la relación en la base de datos.

pedidos.usuario_id → usuarios.id

relationship()

Permite trabajar con esa relación desde los objetos Python.

pedido.usuario

JOIN

Es una operación SQL que permite combinar información de diferentes tablas.

Resumen:

ForeignKey
    ↓
establece la relación

relationship()
    ↓
permite navegar la relación desde Python

JOIN
    ↓
combina información de tablas en una consulta SQL

11. Mini reto conceptual

Respuestas consolidadas:

pedido.usuario devuelve el objeto Usuario relacionado.

pedido.usuario.id devuelve el ID del usuario relacionado.

pedido.usuario.nombre devuelve el nombre.

pedido.usuario.correo devuelve el correo.

pedido.usuario_id devuelve el valor de la Foreign Key, mientras que pedido.usuario devuelve el objeto relacionado.

12. Errores de Python encontrados

Durante las pruebas apareció:

IndentationError: expected an indented block

La causa fue no colocar correctamente la indentación después de:

for pedido in pedidos:

La forma correcta:

for pedido in pedidos:
    print(pedido.producto, "->", pedido.usuario.nombre)

Este error no estaba relacionado con SQLAlchemy.

Conclusiones del Día 71

Se consolidaron los siguientes conceptos:

ForeignKey

Primary Key

relationship()

back_populates

relaciones bidireccionales

navegación entre objetos ORM

pedido.usuario_id

pedido.usuario

usuario.pedidos

db.add()

db.flush()

db.commit()

db.rollback()

diferencia entre ORM y SQL

diferencia entre ForeignKey, relationship() y JOIN

serialización de resultados para FastAPI

Punto de especial atención

Este tema fue más complejo que otros contenidos del bootcamp.

Debe conservarse como tema de revisión, especialmente:

pedido.usuario_id
        vs
pedido.usuario

y:

relationship()
      ↓
db.add()
      ↓
db.flush()
      ↓
db.commit()

La prioridad continúa siendo comprender el mecanismo y no memorizar únicamente la sintaxis.

Estado

✅ Día 71 completado.

Tema: Relaciones ORM con SQLAlchemy – ForeignKey, relationship() y back_populates

Tema marcado para revisión futura.