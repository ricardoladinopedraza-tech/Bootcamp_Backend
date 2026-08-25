Objetivo

Diferenciar ForeignKey, relationship(), join(), joinedload(), JOIN SQL y filter().

Conceptos consolidados

ForeignKey

Establece la relación a nivel de base de datos.

ForeignKey
    ↓
Relación en la BASE DE DATOS

relationship()

Define la relación ORM entre objetos Python.

pedido.usuario
usuario.pedidos

relationship()
    ↓
Define la RELACIÓN ORM

join()

Participa en la construcción de la consulta e incorpora la entidad relacionada para poder trabajar con ella, por ejemplo, para filtrar u ordenar.

pedidos = (
    db.query(Pedido)
    .join(Usuario)
    .filter(Usuario.nombre == "Ricardo")
    .all()
)

join() no filtra por sí mismo; la condición la establece filter().

joinedload()

Controla la carga anticipada de una relación ORM ya existente.

pedidos = (
    db.query(Pedido)
    .options(joinedload(Pedido.usuario))
    .all()
)

Diferencia fundamental

join()
    ↓
Construcción de la consulta
    ↓
combinar / filtrar / ordenar

joinedload()
    ↓
Carga anticipada de una relación ORM

Uso conjunto

pedidos = (
    db.query(Pedido)
    .join(Usuario)
    .filter(Usuario.nombre == "Ricardo")
    .options(joinedload(Pedido.usuario))
    .all()
)

join(Usuario) → incorpora Usuario a la consulta.

filter(...) → limita los resultados a Ricardo.

joinedload(Pedido.usuario) → carga anticipadamente Pedido → Usuario.

JOIN SQL ≠ joinedload()

JOIN SQL
    ↓
Combina datos de tablas dentro de una consulta

joinedload()
    ↓
Controla la carga anticipada de una relación ORM

Aunque joinedload() utilice una estrategia basada en JOIN internamente, su objetivo dentro del ORM es diferente.

Mapa maestro

ForeignKey
    ↓
Relación en BD

relationship()
    ↓
Relación ORM

join()
    ↓
Participa en la consulta

filter()
    ↓
Establece condiciones

joinedload()
    ↓
Carga anticipadamente la relación ORM

Resultado del reto final

Con:

Pedido 1 → Ricardo → laptop
Pedido 2 → Ricardo → mouse
Pedido 3 → Johana  → teclado
Pedido 4 → Ana     → monitor

la consulta con filtro a Ricardo obtiene dos pedidos:

laptop
mouse

joinedload() hace que la relación Pedido → Usuario se cargue anticipadamente.

Frases clave de Ricardo

FK → relación en la base de datos.

relationship() → define la relación ORM.

join() → participa en la consulta.

joinedload() → carga una relación ya existente.

Hito

Día 71 → ForeignKey + relationship()
Día 72 → navegación ORM y respuestas anidadas
Día 73 → lazy loading, N+1, joinedload(), selectinload()
Día 74 → join() vs joinedload()

Estado: Día 74 completado.