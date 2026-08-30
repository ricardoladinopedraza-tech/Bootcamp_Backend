Día 80 — SQLAlchemy: joinedload() y selectinload()

Objetivo

Comprender la carga de relaciones ORM y evitar el problema N+1.

Problema N+1

Si obtenemos 50 pedidos y después se consulta individualmente el usuario de cada pedido, conceptualmente podríamos tener:

1 consulta → pedidos
50 consultas → usuarios
= 51 consultas

relationship()

Define la relación ORM entre objetos.

usuario.pedidos
pedido.usuario

joinedload()

Controla la carga anticipada mediante JOIN.

db.query(Pedido).options(
    joinedload(Pedido.usuario)
).all()

selectinload()

Carga anticipadamente mediante consultas adicionales agrupadas.

db.query(Usuario).options(
    selectinload(Usuario.pedidos)
).all()

Conceptualmente:

Consulta 1 → Usuarios
Consulta 2 → Pedidos relacionados

Diferencias

ForeignKey() → vínculo a nivel de BD
relationship() → relación ORM
joinedload() → eager loading mediante JOIN
selectinload() → eager loading mediante consultas agrupadas

Ni joinedload() ni selectinload() crean la relación; esta ya existe gracias a relationship().

Comprobación práctica

Sin joinedload() se observó una consulta adicional para cargar el usuario.
Con joinedload() SQLAlchemy generó un LEFT OUTER JOIN.
Con selectinload() se observaron dos consultas: una para usuarios/pedidos principales y otra agrupada mediante IN.

Regla mental

relationship() → define
joinedload() → carga anticipadamente mediante JOIN
selectinload() → carga anticipadamente mediante consultas agrupadas