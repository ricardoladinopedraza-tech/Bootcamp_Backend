Día 76 — SQLAlchemy: all(), first(), one() y one_or_none()

Objetivo

Elegir el método de obtención de resultados según la cantidad de registros que esperamos de una consulta.

Métodos

.all()

Devuelve todos los resultados como lista.

usuarios = (
    db.query(Usuario)
    .filter(Usuario.nombre == "Ricardo")
    .all()
)

Sin resultados:

[]

.first()

Devuelve el primer resultado o None si no existe ninguno.

usuario = (
    db.query(Usuario)
    .filter(Usuario.id == usuario_id)
    .first()
)

Importante: first() no comprueba unicidad. Si hay varios resultados, devuelve solamente el primero.

Patrón típico con FastAPI:

usuario = (
    db.query(Usuario)
    .filter(Usuario.id == usuario_id)
    .first()
)

if usuario is None:
    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )

return usuario

SQLAlchemy devuelve None; nuestro código FastAPI decide convertirlo en HTTP 404.

.one()

Expresa que esperamos exactamente un resultado.

0 resultados       → excepción
1 resultado        → objeto
más de 1 resultado → excepción

.one_or_none()

Expresa:

Puede no existir, pero si existe debe ser único.

0 resultados       → None
1 resultado        → objeto
más de 1 resultado → excepción

Es especialmente apropiado cuando el modelo garantiza unicidad, por ejemplo:

correo → UNIQUE

Comparación

Método

0 resultados

1 resultado

Más de 1

.all()

[]

lista

lista

.first()

None

objeto

primer objeto

.one()

excepción

objeto

excepción

.one_or_none()

None

objeto

excepción

Cardinalidad esperada

0..muchos
    ↓
all()

0..1
    ↓
one_or_none()

1 exacto
    ↓
one()

1 o más, pero solo quiero el primero
    ↓
first()

La pregunta correcta es:

¿Cuántos resultados espero que pueda producir esta consulta?

Buscar por ID vs. buscar por nombre

Un ID normalmente es único:

.filter(Usuario.id == usuario_id)

Por tanto, esperamos como máximo un usuario.

Un nombre puede repetirse:

.filter(Usuario.nombre == "Ricardo")

Por lo que podemos obtener cero, uno o varios usuarios.

first() vs. one_or_none()

first()
    ↓
Dame el primero.
No me importa si existen otros.

one_or_none()
    ↓
Puede no existir.
Pero si existe, debe ser único.

Conexión con FastAPI

Para:

GET /usuarios/{usuario_id}

un patrón práctico es:

usuario = (
    db.query(Usuario)
    .filter(Usuario.id == usuario_id)
    .first()
)

if usuario is None:
    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )

return usuario

Idea clave

La elección del método debe responder a la cardinalidad esperada y a las reglas reales del modelo de datos.

Ejemplo:

correo UNIQUE
    ↓
0 o 1
    ↓
one_or_none() expresa muy bien la intención

Si el campo puede repetirse y queremos todos:

nombre NO UNIQUE
    ↓
0, 1 o muchos
    ↓
all()

Cierre del Día 76

El aprendizaje central fue pasar de memorizar métodos a razonar:

¿Qué cantidad de resultados espero y qué reglas de unicidad tiene mi modelo?