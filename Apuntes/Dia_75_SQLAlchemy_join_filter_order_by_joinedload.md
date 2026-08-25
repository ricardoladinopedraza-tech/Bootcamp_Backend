Día 75 — SQLAlchemy: join(), filter(), order_by() y joinedload()

Objetivo

Consolidar la diferencia entre join(), filter(), order_by() y joinedload(), entendiendo qué papel cumple cada uno dentro de una consulta SQLAlchemy.

Conceptos

join()

Participa en la construcción de la consulta e incorpora una entidad relacionada para poder utilizarla en la consulta. No crea la relación ORM.

db.query(Pedido).join(Usuario)

filter()

Determina qué registros forman parte del resultado.

.filter(Usuario.nombre == "Ricardo")

order_by()

Determina el orden de los resultados.

.order_by(Pedido.producto)

Sin especificar .desc(), el orden es ascendente.

Puede utilizar varios criterios:

.order_by(Usuario.nombre, Pedido.producto)

Primero ordena por usuario y, dentro de cada usuario, por producto.

joinedload()

Controla la carga anticipada de una relación ORM que ya existe.

.options(joinedload(Pedido.usuario))

No crea la relación; esta ya fue definida con relationship().

Mapa fundamental

ForeignKey
    ↓
Relación en la BD

relationship()
    ↓
Relación ORM entre objetos Python

join()
    ↓
Participa en la consulta

filter()
    ↓
Determina qué registros obtenemos

order_by()
    ↓
Determina el orden

joinedload()
    ↓
Controla la carga anticipada

Ejemplo integrado

pedidos = (
    db.query(Pedido)
    .join(Usuario)
    .filter(Usuario.nombre == "Ricardo")
    .options(
        joinedload(Pedido.usuario)
    )
    .order_by(Pedido.producto)
    .all()
)

Lectura:

Obtener los pedidos de Ricardo, incorporar Usuario a la consulta para poder filtrarlo, cargar anticipadamente Pedido.usuario y ordenar los pedidos por producto.

Idea clave

La consulta debe leerse como una secuencia lógica:

query()
   ↓
¿Qué entidad consulto?

join()
   ↓
¿Qué entidad relacionada participa?

filter()
   ↓
¿Qué registros quiero?

joinedload()
   ↓
¿Cómo cargo anticipadamente la relación?

order_by()
   ↓
¿En qué orden?

all()
   ↓
Obtengo todos los resultados

Cierre del Día 75

Se consolidó la diferencia entre relación ORM, participación en la consulta, filtrado, ordenamiento y carga anticipada.