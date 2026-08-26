Día 77 — SQLAlchemy: CRUD, UPDATE, DELETE y commit()

Objetivo

Comprender cómo SQLAlchemy permite crear, consultar, modificar y eliminar registros, y entender el papel de commit() en la confirmación de transacciones.

CRUD

C → Create → POST
R → Read   → GET
U → Update → PUT / PATCH
D → Delete → DELETE

CREATE

nuevo_usuario = Usuario(
    nombre="Carlos",
    correo="carlos@correo.com"
)

db.add(nuevo_usuario)
db.commit()

db.add() agrega el objeto a la sesión. db.commit() confirma la transacción.

READ

usuarios = (
    db.query(Usuario)
    .filter(Usuario.nombre == "Ricardo")
    .all()
)

READ normalmente no necesita commit() porque no modifica la BD.

UPDATE mediante objeto ORM

usuario = (
    db.query(Usuario)
    .filter(Usuario.id == 2)
    .first()
)

if usuario is None:
    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )

usuario.nombre = "Johana López"
db.commit()

La distinción fundamental es:

usuario.nombre = "Johana López"
        ↓
Objeto ORM modificado

db.commit()
        ↓
Transacción confirmada
        ↓
Cambio persistido en BD

También existe:

db.query(Usuario).filter(
    Usuario.id == 2
).update({
    Usuario.nombre: "Johana López"
})

db.commit()

La primera forma trabaja directamente con el objeto ORM; .update() actualiza los registros seleccionados por la consulta.

DELETE

usuario = (
    db.query(Usuario)
    .filter(Usuario.id == 2)
    .first()
)

if usuario is None:
    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )

db.delete(usuario)
db.commit()

db.delete(usuario) marca el objeto para eliminación dentro de la sesión.

db.commit() confirma la transacción.

Buscar
  ↓
Verificar existencia
  ↓
db.delete()
  ↓
db.commit()
  ↓
Eliminación confirmada

delete() ≠ commit()

db.delete()
    ↓
Marca para eliminación

db.commit()
    ↓
Confirma la transacción

flush() vs commit()

flush() sincroniza los cambios pendientes de la sesión con la BD dentro de la transacción actual.

commit() confirma la transacción.

flush()
   ↓
Sincroniza/envía cambios

commit()
   ↓
Confirma la transacción

Un commit() normalmente realiza el flush pendiente antes de confirmar, pero conceptualmente son operaciones diferentes.

Patrón de UPDATE en FastAPI

PUT /usuarios/{id}
        ↓
Buscar
        ↓
¿Existe?
   ↙         ↘
 NO           SÍ
 ↓             ↓
404        modificar
               ↓
            commit()
               ↓
             return

Patrón de DELETE

DELETE /usuarios/{id}
        ↓
Buscar
        ↓
¿Existe?
   ↙         ↘
 NO           SÍ
 ↓             ↓
404       db.delete()
               ↓
            commit()
               ↓
             return

Mapa CRUD completo

CREATE
   ↓
db.add()
   ↓
db.commit()


READ
   ↓
query() + filter()
   ↓
first() / all() / one() / one_or_none()


UPDATE
   ↓
query() + filter()
   ↓
modificar objeto
   ↓
db.commit()


DELETE
   ↓
query() + filter()
   ↓
db.delete()
   ↓
db.commit()

Idea fundamental

La secuencia general de un endpoint que modifica o elimina es:

Buscar
  ↓
Verificar existencia
  ↓
Modificar / eliminar
  ↓
commit()
  ↓
return

La modificación del objeto ORM y la confirmación de la transacción son conceptos diferentes.

Modificar un objeto no es lo mismo que confirmar la transacción. commit() confirma el cambio.

Cierre del Día 77

Se consolidó la conexión entre SQLAlchemy y las operaciones CRUD de FastAPI, especialmente UPDATE y DELETE, así como la diferencia entre cambios en la sesión y confirmación mediante commit().