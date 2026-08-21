Día 73 — SQLAlchemy: estrategias de carga, joinedload(), selectinload() y problema N+1

Objetivo

Comprender cómo SQLAlchemy carga las relaciones ORM y diferenciar claramente:

ForeignKey

relationship()

Lazy Loading

joinedload()

selectinload()

problema N+1

Mapa maestro

ForeignKey
    ↓
Relación en BD

relationship()
    ↓
Relación ORM entre objetos

joinedload()
    ↓
Eager loading mediante JOIN

selectinload()
    ↓
Eager loading mediante consulta agrupada

1. ForeignKey

usuario_id = Column(Integer, ForeignKey("usuarios.id"))

Define la relación a nivel de base de datos.

pedido.usuario_id → usuarios.id

2. relationship()

usuario = relationship("Usuario", back_populates="pedidos")

Define la relación ORM entre objetos Python y permite:

pedido.usuario
usuario.pedidos

relationship() crea/define la navegación ORM; no significa automáticamente que se ejecute un JOIN.

3. Lazy Loading

Con:

pedidos = db.query(Pedido).all()

obtenemos inicialmente los pedidos. Al acceder posteriormente a:

pedido.usuario

SQLAlchemy puede cargar el usuario bajo demanda.

4. Problema N+1

Si tenemos 50 pedidos, conceptualmente podemos terminar con:

1 consulta → pedidos
50 consultas → relaciones

N + 1 = 51 consultas

La cantidad exacta depende de la estrategia de carga y del estado de los objetos en la sesión, pero el patrón N+1 representa el problema de realizar cargas adicionales repetidas.

5. joinedload()

from sqlalchemy.orm import joinedload

pedidos = (
    db.query(Pedido)
    .options(joinedload(Pedido.usuario))
    .all()
)

joinedload() controla cómo se carga una relación ya existente y realiza eager loading mediante una estrategia basada en JOIN.

Después seguimos usando:

pedido.usuario

La relación no fue creada por joinedload(); ya existía gracias a relationship().

6. selectinload()

from sqlalchemy.orm import selectinload

usuarios = (
    db.query(Usuario)
    .options(selectinload(Usuario.pedidos))
    .all()
)

Conceptualmente:

Consulta 1 → usuarios
Consulta 2 → pedidos relacionados de esos usuarios

En lugar de una consulta adicional por cada usuario, los pedidos pueden obtenerse mediante una consulta agrupada.

7. Ejemplo

Datos:

Ricardo → laptop
Ricardo → mouse
Johana  → teclado

Con:

for usuario in usuarios:
    for pedido in usuario.pedidos:
        print(usuario.nombre, pedido.producto)

Resultado:

Ricardo | laptop
Ricardo | mouse
Johana  | teclado

usuario.pedidos es una colección de objetos Pedido, no una tabla ni una colección de pares Usuario/Pedido.

8. joinedload() vs selectinload()

Como orientación inicial:

Pedido → Usuario
    ↓
joinedload()

suele ser muy apropiado para una relación muchos-a-uno.

Usuario → muchos Pedido
    ↓
selectinload()

suele ser muy apropiado para una colección uno-a-muchos.

No es una regla absoluta: ambas estrategias pueden utilizarse con distintos tipos de relaciones según cardinalidad, tamaño de datos y consulta.

9. Diferencia fundamental

relationship()
    ↓
DEFINE la relación ORM

joinedload()
    ↓
CARGA anticipadamente mediante JOIN

selectinload()
    ↓
CARGA anticipadamente mediante consulta agrupada

10. Mini retos y respuestas

A–D

A: 50 pedidos pueden producir el patrón N+1, conceptualmente 51 consultas.

B: joinedload() intenta evitar las cargas adicionales de la relación mediante eager loading.

C: relationship() define la relación; joinedload() controla cómo se carga.

D: relationship() → define; joinedload() → controla la carga.

E–J

E: SQLAlchemy puede necesitar cargar Usuario cuando se accede a pedido.usuario si no estaba cargado.

F: En .options(joinedload(Pedido.usuario)) indicamos que la relación debe cargarse anticipadamente.

G: Porque definir una relación y decidir cómo cargarla son responsabilidades diferentes.

H: pedido.usuario sigue siendo necesario para acceder al objeto Usuario; joinedload() solamente hace que ya esté cargado.

I: joinedload() no crea la relación; relationship() la define.

J: ForeignKey → relación en BD; relationship() → relación ORM; joinedload() → estrategia de carga.

K–M

K: selectinload(Usuario.pedidos) carga anticipadamente los pedidos relacionados de los usuarios obtenidos.

L: No. La relación ya existe gracias a relationship().

M: Como orientación inicial, Pedido → Usuario suele encajar bien con joinedload() y Usuario → muchos Pedido con selectinload(), sin convertirlo en una regla absoluta.

N–U

N: Para Ricardo, usuario.pedidos contiene conceptualmente [Pedido(laptop), Pedido(mouse)].

O: No. usuario.pedidos funciona por relationship(); selectinload() controla su carga.

P: Sin una estrategia adecuada puede aparecer N+1 y aumentar innecesariamente las consultas.

Q: ForeignKey → relación BD; relationship() → relación ORM; selectinload() → eager loading agrupado; joinedload() → eager loading mediante JOIN.

R: Ricardo | laptop, Ricardo | mouse, Johana | teclado.

S: Conceptualmente, 2 consultas: una para usuarios y otra agrupada para pedidos relacionados.

T: Sin selectinload(), usuario.pedidos puede cargar los pedidos bajo demanda y producir N+1 con muchos usuarios.

U: relationship() establece la relación; selectinload() solamente controla cómo se carga.

🎓 Notas del Ingeniero Ricardo

relationship() define la relación; joinedload() controla cómo queremos cargar esa relación.

ForeignKey → con qué columna de la BD se relaciona.

relationship() → cómo se representa esa relación como objetos ORM.

selectinload() → eager loading mediante consulta agrupada.

joinedload() → eager loading mediante JOIN.

Regla mental

relationship() → DEFINE
joinedload()   → CARGA mediante JOIN
selectinload() → CARGA mediante consulta agrupada

Hito SQLAlchemy #2

El Día 73 queda marcado como un día importante junto con el Día 71 y el Día 72.

Día 71: ForeignKey, relationship(), back_populates, flush() vs commit().

Día 72: navegación Pedido ↔ Usuario, respuestas anidadas con Pydantic y comparación JOIN vs relationship().

Día 73: Lazy Loading, problema N+1, joinedload() y selectinload().

Estado

Día 73 completado.