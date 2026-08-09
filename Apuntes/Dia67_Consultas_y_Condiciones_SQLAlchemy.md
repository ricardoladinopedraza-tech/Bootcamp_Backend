# Día 67 — Consultas y condiciones con SQLAlchemy

## Objetivo

Aprender a realizar consultas más específicas con SQLAlchemy utilizando:

- `filter()`
- `filter_by()`
- Operadores de comparación
- `and_()`
- `or_()`
- `.contains()`
- `.all()`
- `.first()`

---

# 1. Consultas con filter()

`filter()` permite establecer condiciones sobre las columnas de un modelo.

Ejemplo:

```python
usuarios = db.query(Usuario).filter(
    Usuario.id > 2
).all()

La consulta busca todos los usuarios cuyo ID sea mayor que 2.

2. Operadores de comparación

SQLAlchemy permite utilizar expresiones como:

==    igual
!=    diferente
>     mayor que
<     menor que
>=    mayor o igual
<=    menor o igual

Ejemplo:

usuarios = db.query(Usuario).filter(
    Usuario.id > 2
).all()
3. filter() y filter_by()
filter_by()

Se utiliza principalmente para condiciones sencillas y directas.

usuarios = db.query(Usuario).filter_by(
    nombre="Ricardo"
).all()
filter()

Es más flexible y permite utilizar condiciones más complejas.

usuarios = db.query(Usuario).filter(
    Usuario.id > 2
).all()

También permite utilizar and_(), or_() y métodos como .contains().

4. and_()

and_() permite combinar condiciones que deben cumplirse simultáneamente.

from sqlalchemy import and_

usuarios = db.query(Usuario).filter(
    and_(
        Usuario.nombre == "Ricardo",
        Usuario.id > 1
    )
).all()

Las dos condiciones deben ser verdaderas.

Conceptualmente:

condición A
    Y
condición B
    ↓
resultado
5. or_()

or_() permite combinar condiciones donde basta que una de ellas sea verdadera.

from sqlalchemy import or_

usuarios = db.query(Usuario).filter(
    or_(
        Usuario.nombre == "Ricardo",
        Usuario.id == 4
    )
).all()

Conceptualmente:

condición A
    O
condición B
    ↓
resultado
6. Igualdad exacta con ==

La expresión:

Usuario.nombre == "Ricardo"

busca una coincidencia exacta.

Por ejemplo:

Ricardo

coincide.

Pero:

Ana, Ricardo, Josefo

no coincide porque el contenido completo de la columna es diferente.

7. Búsqueda con contains()

.contains() permite buscar un texto dentro del contenido de una columna.

usuarios = db.query(Usuario).filter(
    Usuario.nombre.contains("Ricardo")
).all()

Esta consulta puede encontrar:

Ricardo
Ana, Ricardo, Josefo

porque ambos contienen el texto "Ricardo".

Diferencia fundamental:

Usuario.nombre == "Ricardo"

→ coincidencia exacta.

Usuario.nombre.contains("Ricardo")

→ el texto contiene "Ricardo".

8. Combinando contains() y and_()

También podemos combinar una búsqueda de texto con otra condición:

usuarios = db.query(Usuario).filter(
    and_(
        Usuario.nombre.contains(nombre),
        Usuario.id > 1
    )
).all()

En nuestro proyecto, buscando "Ricardo" produjo:

ID 3 → Ana, Ricardo, Josefo

porque:

nombre contiene "Ricardo" → True
id > 1                    → True

El usuario con ID 1 quedó fuera porque no cumple id > 1.

9. .all() y .first()

.all() devuelve todos los registros que cumplen la consulta:

usuarios = db.query(Usuario).filter(
    Usuario.nombre == "Ricardo"
).all()

.first() devuelve solamente el primer registro que cumple la condición:

usuario = db.query(Usuario).filter(
    Usuario.id == usuario_id
).first()

Si no encuentra ninguno, .first() devuelve None.

10. Flujo de una consulta

Podemos visualizar una consulta de esta manera:

db
 ↓
query(Usuario)
 ↓
filter()
 ↓
condición
 ↓
all() / first()
 ↓
resultado

Ejemplo:

usuarios = db.query(Usuario).filter(
    Usuario.nombre.contains("Ricardo")
).all()

Lectura conceptual:

Desde la sesión db, consultar la tabla representada por Usuario, filtrar los registros cuyo nombre contenga "Ricardo" y devolver todos los resultados.

11. Conceptos aprendidos
Elemento	Función
db	Session que permite comunicarse con la BD
Usuario	Modelo que representa la tabla
filter()	Permite establecer condiciones
filter_by()	Consultas sencillas por igualdad
and_()	Todas las condiciones deben cumplirse
or_()	Basta con que una condición se cumpla
==	Coincidencia exacta
.contains()	Busca texto contenido dentro de una columna
.all()	Devuelve todos los resultados
.first()	Devuelve el primer resultado
12. Aprendizaje práctico

Durante este día se realizaron consultas reales desde Swagger.

Se comprobó la diferencia entre:

Usuario.nombre == "Ricardo"

y:

Usuario.nombre.contains("Ricardo")

También se comprobó una consulta combinada:

and_(
    Usuario.nombre.contains(nombre),
    Usuario.id > 1
)

El resultado permitió comprobar que SQLAlchemy puede combinar diferentes condiciones para construir consultas más específicas.

Reflexión técnica

Las consultas con SQLAlchemy permiten pasar de obtener simplemente todos los registros a realizar búsquedas específicas.

filter() resulta especialmente importante porque permite construir condiciones que posteriormente pueden combinarse mediante and_() y or_().

También comprendí que una consulta debe analizarse desde el punto de vista lógico antes de ejecutarla. Esto permite predecir qué registros deberían aparecer y posteriormente comprobarlo contra la base de datos.

Conclusión

El Día 67 permitió avanzar desde consultas básicas hacia consultas con condiciones.

La estructura conceptual quedó:

Consulta
   ↓
Modelo
   ↓
Filtro
   ↓
Condición
   ↓
Resultado

Y se comprobó que SQLAlchemy permite construir consultas progresivamente más complejas sin tener que escribir directamente las sentencias SQL.