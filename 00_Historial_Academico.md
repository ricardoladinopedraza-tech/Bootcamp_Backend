# Historial Académico – Python Backend
**Estudiante:** Ricardo Ladino Pedraza

---

# Objetivo

Prepararme para obtener un empleo remoto como Desarrollador Backend Python, construyendo una base sólida en programación, APIs, FastAPI, bases de datos, Docker y despliegue, acompañada de proyectos reales documentados y versionados con Git y GitHub.

---

# Metodología de estudio

Cada sesión sigue la siguiente estructura:

1. Explicación del tema.
2. Ejemplos comentados.
3. Mini reto teórico.
4. Ejercicio de razonamiento.
5. Mini proyecto.
6. Actualización de documentación Markdown.
7. Uso de Git.
8. Publicación en GitHub.
9. Relación con el siguiente tema.

---

# FASE 1 – Fundamentos de Python

Temas estudiados:

- Variables
- Tipos de datos
- Operadores
- Condicionales
- Ciclos
- Funciones
- Listas
- Tuplas
- Diccionarios
- Sets
- Manejo de archivos
- Excepciones
- Programación Orientada a Objetos
- Módulos
- Decoradores
- Generadores
- Lambdas
- Comprensiones
- zip()
- enumerate()
- any()
- all()
- sorted()
- *args y **kwargs
- Módulo math

---

# FASE 2 – Herramientas de desarrollo

Temas estudiados:

- Entornos virtuales
- pip
- Instalación de paquetes
- requests

---

# FASE 3 – Bootcamp Backend

## Módulo 1

Fundamentos de Internet.

---

## Módulo 2

HTTP

Aprendidos:

- Cliente
- Servidor
- Request
- Response
- Headers
- Body
- Métodos HTTP
- Status Code

---

## Módulo 3

Requests en profundidad

Aprendidos:

- requests.get()
- requests.post()
- requests.put()
- requests.patch()
- requests.delete()
- params
- headers
- json
- data
- elapsed
- reason
- url
- content
- text

---

## Módulo 4

Depuración de APIs

Aprendidos:

- status_code
- reason
- headers
- type()
- len()
- get()
- Manejo de errores
- KeyError
- IndexError
- TypeError
- Validación de respuestas

---

## Módulo 5

JSON en profundidad

Aprendidos:

- Objetos
- Listas
- JSON reales
- Conversión a objetos Python
- Acceso seguro
- Navegación de estructuras anidadas

---

## Módulo 6

APIs REST

Aprendidos:

- Recursos
- URLs REST
- CRUD

Métodos:

- GET
- POST
- PUT
- PATCH
- DELETE

Conceptos:

- Create
- Read
- Update
- Delete

Diferencia entre PUT y PATCH.

---

# Git

Repositorio creado:

Git_Practicas

Temas dominados:

- git init
- git status
- git add
- git commit
- git log
- git log --oneline
- git diff
- git diff --staged
- git remote
- git push
- ramas
- GitHub

---

# Markdown

Aprendidos:

- Encabezados
- Listas
- Bloques de código
- Tablas
- Organización de documentación técnica

Documentos creados:

- 00_Entorno_Desarrollo.md
- Requests.md

---

# Organización del repositorio

Bootcamp_Backend/

Actualmente contiene los módulos del Bootcamp y continuará creciendo durante el plan de estudio.

---

# Estado actual

Python:

Fundamentos consolidados.

HTTP:

Comprendido.

JSON:

Comprendido.

Requests:

Comprendido.

REST:

Comprendido.

Git:

Uso diario.

GitHub:

Integrado al flujo de trabajo.

Markdown:

Integrado a la documentación.

---

# Próxima etapa

Retorno a FastAPI.

Punto de inicio:

**Día 47 del plan principal de Python Backend.**

A partir de este punto:

- desarrollo de APIs propias
- documentación continua
- uso permanente de Git
- proyectos incrementales

---

# Proyectos planeados

Proyecto 1

API de Gestión de Usuarios

Tecnologías:

- FastAPI
- Pydantic
- Git
- GitHub

---

Proyecto 2

Sistema de Inventario

Tecnologías:

- FastAPI
- PostgreSQL
- SQLAlchemy

---

Proyecto 3

API Clínica

Tecnologías:

- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT
- Docker
- Deploy

---

# Objetivo final

Al finalizar el plan contar con:

- Portafolio profesional en GitHub.
- Tres proyectos backend completos.
- Documentación técnica propia.
- Dominio de FastAPI.
- Dominio de PostgreSQL.
- Dominio de Docker.
- Preparación para entrevistas técnicas.

# Forma de trabajo

Durante todo el proceso de formación se mantendrán los siguientes principios:

- Comprender antes de memorizar.
- No dejar vacíos conceptuales.
- Relacionar cada tema con los anteriores.
- Documentar el aprendizaje en archivos Markdown.
- Versionar el trabajo con Git desde el inicio.
- Publicar el progreso en GitHub de forma incremental.
- Construir proyectos reales que evolucionen con cada módulo.
- Priorizar la calidad y el entendimiento sobre la velocidad.

#######      Actualizacion    ###############

## Módulo FastAPI

**Estado:** 🔄 En progreso

### Temas completados

- Introducción a FastAPI
- Path Parameters
- Query Parameters
- Validación con Path()
- Validación con Query()
- Request Body
- BaseModel
- Field()
- Campos opcionales (`Optional`)
- Valores por defecto
- Modelos anidados (Nested Models)
- Listas de modelos (`List[Modelo]`)





### Proyecto en desarrollo

**Proyecto 1 – API de Gestión de Usuarios**

Funcionalidades implementadas:

- Endpoints GET y POST.
- Recepción de Path y Query Parameters.
- Validación de parámetros.
- Modelos con Pydantic.
- Validación con `Field()`.
- Campos opcionales.
- Valores por defecto.
- Modelos anidados.
- Pruebas funcionales con Swagger.

### Día 55 – Response Models

Temas estudiados:

- Response Models (`response_model`)
- Separación entre modelos de entrada y salida
- Filtrado automático de datos
- Seguridad en respuestas HTTP
- Validación de respuestas
- Documentación automática en Swagger

### Día 56 – Routers

Temas estudiados:

- APIRouter
- Organización modular de APIs
- include_router()
- Separación de endpoints
- Estructura profesional de proyectos FastAPI
- Organización para trabajo en equipo

### Día 57 – Prefix y Tags

Temas estudiados:

- prefix en APIRouter
- tags para documentación
- Organización de rutas
- Organización de Swagger
- Buenas prácticas para proyectos FastAPI

### Día 58 – Depends()

Temas estudiados:

- Inyección de dependencias
- Depends()
- Reutilización de lógica
- Separación de responsabilidades
- Modularidad de la aplicación

### Día 59 – Services

Temas estudiados:

- Separación de la lógica del negocio.
- Carpeta services.
- Reutilización de código.
- Responsabilidad de los endpoints.
- Arquitectura en capas.

### Día 60 – Variables de Entorno

Temas estudiados:

- Variables de entorno.
- Archivo `.env`.
- Configuración de aplicaciones.
- Separación entre código y configuración.
- Buenas prácticas de seguridad.

# ✅ Día 61 — Introducción a SQLAlchemy

## Temas estudiados

- ¿Qué es un ORM?
- Introducción a SQLAlchemy
- Objetos vs tablas
- Persistencia de datos
- Arquitectura general SQLAlchemy + FastAPI
- Inicio de la transición hacia PostgreSQL

## Conceptos clave

- SQLAlchemy actúa como puente entre Python y la base de datos.
- Un ORM permite trabajar con objetos en lugar de escribir SQL constantemente.
- Los datos dejarán de almacenarse únicamente en memoria.
- SQLAlchemy será la base para implementar el CRUD sobre PostgreSQL.

## Reorganización del proyecto

Como parte del inicio de esta nueva etapa se reorganizó completamente el proyecto:

- Se creó la carpeta `App/` para centralizar el desarrollo.
- Se organizaron las carpetas `core`, `database`, `models`, `routers`, `schemas` y `services`.
- Los apuntes técnicos se centralizaron en `Apuntes/`.
- Se preparó la estructura que se utilizará durante el resto del bootcamp.

Estado del proyecto: Arquitectura profesional preparada para comenzar el desarrollo con SQLAlchemy.

# ✅ Día 62 — Configuración inicial de SQLAlchemy

## Temas estudiados

- Arquitectura SQLAlchemy + PostgreSQL.
- Engine.
- Session.
- Base.
- Organización de la carpeta `database`.
- Flujo de comunicación entre FastAPI y PostgreSQL.

## Conceptos clave

- SQLAlchemy actúa como puente entre FastAPI y PostgreSQL.
- El Engine administra las conexiones con la base de datos.
- Una Session representa una conversación temporal para realizar operaciones sobre la base de datos.
- Las clases que heredan de Base representan tablas.

## Flujo general

Cliente

↓

Router

↓

Service

↓

Session

↓

SQLAlchemy

↓

PostgreSQL

↓

Respuesta

## Aprendizajes destacados

- Comprensión del papel de Engine, Session y Base.
- Inicio de la configuración de SQLAlchemy dentro de una arquitectura profesional.
- Relación entre FastAPI, SQLAlchemy y PostgreSQL.
- Preparación de la aplicación para comenzar a trabajar con datos persistentes.

Estado del proyecto: Aplicación preparada para comenzar la implementación del acceso a la base de datos mediante SQLAlchemy.

# ✅ Día 62 — Configuración inicial de SQLAlchemy

## Temas estudiados

- Arquitectura SQLAlchemy.
- Engine.
- Session.
- SessionLocal.
- Base.
- Archivo database.py.
- Organización de la carpeta database.
- Flujo FastAPI → SQLAlchemy → Base de datos.

## Conceptos clave

- SQLAlchemy actúa como intermediario entre FastAPI y la base de datos.
- El Engine administra todas las conexiones de la aplicación y existe una única instancia durante su ejecución.
- SessionLocal funciona como una fábrica que crea una nueva Session para cada petición.
- Una Session representa una conversación temporal con la base de datos.
- Base permite que las clases de Python representen tablas.

## Archivo principal

App/

└── database/

&nbsp;&nbsp;&nbsp;&nbsp;└── database.py

Contiene:

- Engine
- SessionLocal
- Base

## Flujo de trabajo

Cliente

↓

Router

↓

Service

↓

Session

↓

SQLAlchemy

↓

Base de datos

↓

Respuesta

## Aprendizajes destacados

- Comprensión de la arquitectura básica de SQLAlchemy.
- Diferenciación clara entre Engine y Session.
- Preparación del proyecto para comenzar la creación de modelos y tablas.
- Inicio de la capa de persistencia de la aplicación.

**Estado del proyecto:** Infraestructura de SQLAlchemy preparada. La aplicación está lista para comenzar la definición de modelos y la creación de tablas.

# ✅ Día 63 — Primer Modelo ORM con SQLAlchemy

## Temas estudiados

- Concepto de ORM (Object Relational Mapping).
- Creación del primer modelo.
- Herencia de Base.
- __tablename__.
- Column().
- Tipos Integer y String.
- Llave primaria (Primary Key).

## Conceptos clave

- Cada clase representa una tabla.
- Cada atributo representa una columna.
- Cada objeto representa un registro.
- Base permite que SQLAlchemy interprete la clase como una tabla.
- __tablename__ define el nombre físico de la tabla.
- Column() define cada uno de los campos de la tabla.

## Modelo implementado

```python
class Usuario(Base):

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)

    nombre = Column(String)

    correo = Column(String)
```

## Aprendizajes destacados

- Primer modelo ORM creado correctamente.
- Comprensión de la relación entre objetos de Python y tablas SQL.
- Inicio del diseño de la base de datos mediante clases.
- Preparación para la creación física de tablas.

**Estado del proyecto:** Primer modelo ORM implementado correctamente. La aplicación está lista para generar su primera tabla en la base de datos.

## ✅ Día 64 – Creación automática de tablas

### Temas vistos

- Base.metadata
- metadata.create_all()
- Registro de modelos ORM
- Creación automática de tablas
- Importación de modelos
- Archivo SQLite app.db

### Logros

- Configuración correcta de SQLAlchemy.
- Instalación de dependencias faltantes.
- Solución de errores de importación.
- Ejecución exitosa de FastAPI.
- Creación automática de la base de datos SQLite.
- Primera tabla creada mediante ORM.

### Estado

✅ Completado.


✅ Día 65 – CRUD (Create): insertar registros con SQLAlchemy. Uso de Session, add(), commit(), refresh(). Primeros endpoints POST y GET conectados a SQLite.

### Día 66 — Consultas con SQLAlchemy

- Consultas mediante `db.query()`.
- Obtención de múltiples registros con `.all()`.
- Obtención de un registro con `.first()`.
- Uso de `filter()` para establecer condiciones.
- Manejo de resultados inexistentes mediante `None`.
- Uso de `HTTPException`.
- Respuesta `404 Not Found` cuando un usuario no existe.
- Endpoint `GET /usuarios/{usuario_id}`.
- Diferencia entre obtener todos los registros y obtener uno específico.

### Día 67 — Consultas y condiciones con SQLAlchemy
- Consultas con `filter()` y `filter_by()`.
- Operadores de comparación.
- Uso de `and_()` y `or_()`.
- Diferencia entre igualdad exacta (`==`) y búsqueda parcial (`contains()`).
- Combinación de múltiples condiciones.
- Uso de `.all()` y `.first()`.
- Práctica real de consultas desde Swagger.

### Día 68 – Actualización parcial con PATCH y SQLAlchemy

- Implementación de actualización parcial mediante `PATCH`.
- Modelo Pydantic con campos opcionales.
- Diferencia entre campo no enviado, `None` y valor enviado.
- Uso de `model_dump()`.
- Uso de `exclude_unset=True` para identificar únicamente los campos enviados.
- Uso de `setattr()` para actualizar atributos dinámicamente.
- Flujo de actualización: búsqueda → validación → modificación → `commit()` → `refresh()`.
- Manejo de `404 Not Found` cuando el usuario no existe.
- Diferencia conceptual entre `PATCH` (actualización parcial) y `PUT` (reemplazo/actualización completa).
- Pruebas reales realizadas mediante Swagger.
- Se verificó que modificar un campo mediante PATCH no altera los demás campos.

### Día 69 – DELETE y eliminación de registros con SQLAlchemy

- Implementación del endpoint `DELETE /usuarios/{usuario_id}`.
- Búsqueda del usuario mediante `query()`, `filter()` y `first()`.
- Verificación de existencia antes de eliminar.
- Manejo de `404 Not Found` para usuarios inexistentes.
- Uso de `db.delete()` para preparar la eliminación.
- Uso de `db.commit()` para confirmar y persistir la eliminación.
- Comprensión de por qué `refresh()` no es necesario después de eliminar.
- Pruebas realizadas mediante Swagger.
- Eliminación exitosa del usuario con ID 4.
- Verificación mediante `GET /usuarios`.
- Prueba de eliminación de un usuario inexistente (`ID 999`) con respuesta 404.
- Consolidación del CRUD: POST, GET, PATCH y DELETE.

### Día 70 – Relaciones entre tablas, ForeignKey y JOIN con SQLAlchemy

Estado: ✅ Finalizado

Temas estudiados:

- Relaciones entre tablas.
- Primary Key y Foreign Key.
- Relación uno a muchos (1:N).
- Modelo Usuario y modelo Pedido.
- `ForeignKey("usuarios.id")`.
- Consultas de pedidos mediante `filter()`.
- JOIN entre `Pedido` y `Usuario`.
- `Pedido.usuario_id == Usuario.id`.
- Diferencia entre consultar objetos ORM y columnas específicas.
- Resultados de SQLAlchemy como lista de tuplas.
- Transformación de tuplas a diccionarios.
- Serialización de resultados para FastAPI.
- Depuración de un `500 Internal Server Error`.
- Verificación directa de las tablas y datos mediante SQLite.

Práctica realizada:

- Creación de pedidos relacionados con el usuario `id=1`.
- Verificación directa en SQLite.
- Consulta de todos los pedidos de un usuario.
- Implementación de un JOIN entre usuarios y pedidos.
- Resolución de un error de serialización producido por el resultado del JOIN.

Conceptos consolidados:

- ForeignKey establece la relación entre tablas.
- JOIN utiliza esa relación para combinar información.
- Una ForeignKey permite que múltiples registros de una tabla secundaria hagan referencia al mismo usuario.
- El resultado de una consulta de columnas específicas puede ser una lista de tuplas.
- FastAPI necesita una estructura adecuada para serializar el resultado como JSON.

Resultado final:

```text
laptop  → Ricardo
mouse   → Ricardo
teclado → Ricardo

Día 71 – Relaciones ORM con SQLAlchemy

Se estudió y practicó la relación entre modelos mediante SQLAlchemy ORM.

Temas vistos

ForeignKey

relationship()

back_populates

Relaciones bidireccionales

Navegación entre objetos relacionados

pedido.usuario_id vs pedido.usuario

usuario.pedidos

db.add()

db.flush()

db.commit()

db.rollback()

Diferencia entre ForeignKey, relationship() y JOIN

Uso de relaciones ORM desde FastAPI

Serialización de resultados para respuestas JSON

Comprobaciones prácticas

Se comprobó directamente en el proyecto que:

pedido.usuario.nombre

permite acceder al nombre del usuario relacionado y que:

pedido.usuario_id

representa el valor de la Foreign Key.

También se comprobó experimentalmente que flush() sincroniza la Foreign Key con la transacción antes de commit().

Observación académica

El tema de relaciones ORM fue considerado especialmente complejo y queda marcado como contenido de revisión futura.

Estado

✅ Día 71 completado.

Día 72 — Registro de aprendizaje

Tema principal

SQLAlchemy ORM: navegación mediante relationship() y respuestas anidadas con Pydantic.

Se comprobó que:

usuario.pedidos

permite navegar desde un Usuario hacia sus pedidos, mientras:

pedido.usuario

permite navegar desde un Pedido hacia su usuario.

Distinción fundamental

Debe conservarse especialmente:

pedido.usuario_id

representa el valor de la Foreign Key.

Mientras:

pedido.usuario

representa el objeto Usuario relacionado mediante relationship().

Pydantic

Se utilizó un modelo anidado con:

model_config = {
    "from_attributes": True
}

Esto permitió convertir la relación ORM en una respuesta JSON anidada.

Ejemplo:

{
    "id": 1,
    "producto": "laptop",
    "usuario": {
        "id": 1,
        "nombre": "Ricardo",
        "correo": "ricardol@correo.com"
    }
}

Comparación importante

JOIN

SQL → JOIN → tuplas → diccionarios → JSON

relationship()

SQLAlchemy → Pedido → pedido.usuario → Usuario → Pydantic → JSON anidado

Se consolidó que JOIN y relationship() son conceptos diferentes:

JOIN es una operación de consulta SQL.

relationship() representa una asociación entre objetos ORM y permite navegar entre ellos.

FastAPI — aprendizaje adicional

Al utilizar:

/pedidos/detalle-orm

FastAPI intentó inicialmente interpretarlo como:

/pedidos/{pedido_id}

Como pedido_id era int, produjo:

Input should be a valid integer

Esto reforzó la importancia de leer los errores de FastAPI para entender cómo el framework interpretó la solicitud.

Hito conceptual del Día 72

Este día consolida:

Foreign Key ≠ relationship

Específicamente:

pedido.usuario_id → valor de Foreign Key

pedido.usuario → objeto Usuario relacionado

Y la navegación:

usuario.pedidos → lista de Pedido

pedido.usuario → Usuario

queda como referencia fundamental para las siguientes sesiones.

Estado

Día 72 completado.

Progreso

Día 71: SQLAlchemy — relationship(), ForeignKey, back_populates, navegación bidireccional, flush() vs commit().

Día 72: SQLAlchemy ORM — navegación Pedido → Usuario, respuestas anidadas con Pydantic y comparación JOIN vs relationship().

Día 73: SQLAlchemy — Lazy Loading, problema N+1, joinedload() y selectinload().

Hitos SQLAlchemy

⭐ Día 71 — Relaciones ORM

ForeignKey
relationship()
back_populates
flush()
commit()

Distinción crítica:

pedido.usuario_id → valor de Foreign Key
pedido.usuario    → objeto Usuario relacionado

⭐ Día 72 — Navegación ORM y respuestas anidadas

usuario.pedidos → lista de Pedido
pedido.usuario  → Usuario

Se consolidó Pydantic con from_attributes=True y la diferencia conceptual entre JOIN y relationship().

⭐ Día 73 — Estrategias de carga

Se consolidaron:

lazy loading
N + 1
joinedload()
selectinload()

Mapa central:

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

Nota importante

joinedload() y selectinload() no crean relaciones. La relación ya está definida por relationship().

relationship() → DEFINE
joinedload()   → CARGA mediante JOIN
selectinload() → CARGA mediante consulta agrupada

Problema N+1

Se comprendió que, sin una estrategia adecuada de carga, recorrer relaciones puede provocar una consulta inicial más consultas adicionales repetidas:

1 + N

Esto puede generar trabajo y tráfico innecesarios para la base de datos.

Notas del Ingeniero Ricardo

relationship() define la relación; joinedload() controla cómo queremos cargar esa relación.

ForeignKey → con qué columna de la BD se relaciona.

relationship() → cómo se representa esa relación como objetos ORM.

selectinload() → eager loading mediante consulta agrupada.

joinedload() → eager loading mediante JOIN.

Estado

Día 73 completado.

Siguiente paso del Bootcamp: Día 74 — profundizar en join() vs joinedload() y cuándo utilizar cada uno.

Día 74

Se consolidó:

join()
    ↓
participa en la construcción de la consulta

frente a:

joinedload()
    ↓
carga anticipadamente una relación ORM existente

Pueden utilizarse conjuntamente:

db.query(Pedido)    .join(Usuario)    .filter(Usuario.nombre == "Ricardo")    .options(joinedload(Pedido.usuario))

Mapa maestro

ForeignKey
    ↓
Relación en BD
    ↓
relationship()
    ↓
Relación ORM
    ↓
┌─────────────────────────────┐
│                             │
join()                    carga ORM
│                             │
↓                       ┌─────┴─────┐
Consulta               joinedload() selectinload()
│                       │             │
filter / order_by      JOIN          consulta agrupada

Notas importantes

pedido.usuario_id es el valor de la Foreign Key; pedido.usuario es el objeto Usuario relacionado.

relationship() define la relación; join() participa en la consulta; joinedload() controla la carga anticipada.

Estado: Día 74 completado.

Día 75 — join(), filter(), order_by() y joinedload()

join() → participa en la construcción de la consulta e incorpora una entidad relacionada.

filter() → determina qué registros forman parte del resultado.

order_by() → determina el orden.

joinedload() → controla la carga anticipada de una relación ORM ya existente.

Se trabajó el ordenamiento por múltiples criterios:
order_by(Usuario.nombre, Pedido.producto).

Se consolidó la lectura de una consulta como secuencia:
query → join → filter → joinedload → order_by → all.

Día 76 — all(), first(), one() y one_or_none()

.all() → todos los resultados como lista; sin resultados devuelve [].

.first() → primer resultado o None; no comprueba unicidad.

.one() → exige exactamente un resultado; cero o más de uno producen excepción.

.one_or_none() → cero o un resultado; más de uno produce excepción.

Se introdujo la cardinalidad esperada para elegir el método:

0..muchos → .all()

0..1 → .one_or_none()

1 exacto → .one()

1 o más, pero solo interesa el primero → .first()

Conexión con FastAPI: first() puede devolver None, y el endpoint puede convertirlo en HTTPException(404).

Buscar por ID suele implicar como máximo un registro; buscar por nombre puede producir varios.

one_or_none() expresa muy bien una búsqueda sobre un campo que realmente sea UNIQUE.

Cadena de conceptos prioritarios

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
Qué registros

order_by()
    ↓
Qué orden

joinedload()
    ↓
Carga anticipada

all() / first() / one() / one_or_none()
    ↓
Cuántos resultados esperamos

Distinción crítica para futuras revisiones

pedido.usuario_id
    ↓
dato de la Foreign Key

pedido.usuario
    ↓
objeto Usuario relacionado

Mantener especialmente destacados para futuras revisiones: ForeignKey, relationship(), back_populates, flush() vs. commit(), joinedload(), selectinload(), join() y la diferencia entre pedido.usuario_id y pedido.usuario.

Día 77 — CRUD, UPDATE, DELETE y commit()

Se inició formalmente la conexión entre SQLAlchemy y CRUD.

CREATE → POST
READ   → GET
UPDATE → PUT / PATCH
DELETE → DELETE

CREATE

db.add(nuevo_usuario)
db.commit()

UPDATE

usuario.nombre = "Johana López"
db.commit()

Modificar el objeto ORM y confirmar la transacción son operaciones diferentes.

DELETE

db.delete(usuario)
db.commit()

db.delete() marca el objeto para eliminación y db.commit() confirma la transacción.

READ

Normalmente no requiere commit() porque solamente consulta.

flush() vs commit()

flush() sincroniza los cambios pendientes de la sesión con la BD dentro de la transacción.

commit() confirma la transacción.

Cadena de conceptos prioritarios

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
Filtra registros

order_by()
    ↓
Ordena resultados

joinedload()
    ↓
Carga anticipadamente una relación

all() / first() / one() / one_or_none()
    ↓
Determinan cómo obtenemos resultados

db.add()
    ↓
Agrega objeto a la sesión

db.delete()
    ↓
Marca objeto para eliminación

db.commit()
    ↓
Confirma la transacción

Distinción crítica para futuras revisiones

pedido.usuario_id
    ↓
Valor de la Foreign Key

pedido.usuario
    ↓
Objeto Usuario relacionado

Mantener especialmente destacados para futuras revisiones: ForeignKey, relationship(), back_populates, flush() vs commit(), joinedload(), selectinload(), join() y la diferencia entre pedido.usuario_id y pedido.usuario.

Estado actual

Día 77 completado.

El aprendizaje ha evolucionado desde consultas básicas hasta relaciones ORM, carga anticipada, construcción de consultas y operaciones CRUD con SQLAlchemy/FastAPI.

Día 78

Se consolidaron db.add(), db.commit() y db.refresh(), además de la diferencia entre modelos Pydantic y modelos ORM de SQLAlchemy.

Día 79

Se estudiaron flush(), rollback() y commit(), el manejo de errores y la atomicidad de transacciones, incluyendo el flujo Usuario + Pedido.

Día 80

Se consolidaron N+1, relationship(), joinedload() y selectinload(). Se comprobó el SQL generado por SQLAlchemy y se eliminó el endpoint duplicado que provocaba el warning de Duplicate Operation ID.

Día 81

Inicio del Bloque 2: PostgreSQL. Se estudiaron servidor, base de datos, tablas, registros, conexión y la diferencia entre usuarios/roles de PostgreSQL y usuarios de la aplicación.

Día 82

SQL fundamental: SELECT, INSERT, UPDATE, DELETE y WHERE. Se relacionaron estos comandos con las operaciones de SQLAlchemy y se aclaró la diferencia entre DELETE FROM usuarios; y DROP TABLE usuarios;.

Estado

El plan se retoma estrictamente desde el Día 81, evitando profundizar innecesariamente en temas fuera del objetivo diario.

Día 83 — Relaciones SQL

Se estudiaron:

Primary Key (PK).

Foreign Key (FK).

JOIN.

Cardinalidad.

Relación del proyecto:

Usuario 1 ─────────── N Pedido

Se consolidó:

PK → identifica
FK → relaciona
JOIN → combina información en una consulta
Cardinalidad → describe cuántos registros pueden relacionarse

Día 84 — PostgreSQL + Python

Se estudió la conexión desde Python mediante psycopg.

FastAPI
   ↓
SQLAlchemy
   ↓
psycopg
   ↓
PostgreSQL

Se consolidó la diferencia entre SQLAlchemy como ORM y psycopg como driver.

Día 85 — PostgreSQL + SQLAlchemy

Se realizó el cambio de SQLite a PostgreSQL:

SQLite → app.db

a:

PostgreSQL → bootcamp_backend

Los modelos y operaciones ORM principales permanecieron iguales.

Se comprobó que:

Base.metadata.create_all(bind=engine)

crea la estructura de las tablas, pero:

create_all() ≠ migración de datos

Los registros existentes de SQLite no se transfieren automáticamente.

Día 86 — Variables de entorno y .env

Se estudió:

variables de entorno;

.env;

python-dotenv;

load_dotenv();

os.getenv();

.gitignore;

seguridad de credenciales.

Cadena consolidada:

.env
 ↓
load_dotenv()
 ↓
os.getenv("DATABASE_URL")
 ↓
DATABASE_URL
 ↓
SQLAlchemy
 ↓
psycopg
 ↓
PostgreSQL

Distinción fundamental:

.env
 ↓
configuración fuera del código

.gitignore
 ↓
evita que Git rastree .env

Se verificó que la aplicación utiliza correctamente PostgreSQL mediante DATABASE_URL y que .env no aparece como archivo pendiente de seguimiento en Git.

Cadena maestra actual

FastAPI
    ↓
SQLAlchemy
    ↓
psycopg
    ↓
PostgreSQL
    ↓
bootcamp_backend
    ↓
usuarios / pedidos

Relaciones:

ForeignKey
    ↓
relación en BD

relationship()
    ↓
relación ORM

join()
    ↓
consulta

joinedload() / selectinload()
    ↓
estrategia de carga

Transacciones:

db.add()
db.flush()
db.commit()
db.rollback()
db.refresh()

Estado actual

Día 86 completado.

Día 87 — Alembic: introducción a migraciones

Se estudió por qué create_all() no sustituye un sistema de migraciones.

Alembic permite:

versionar cambios del esquema;

generar migraciones;

aplicar migraciones;

consultar la versión actual de la base de datos;

avanzar mediante upgrade();

retroceder mediante downgrade().

Se instaló:

alembic 1.19.1

Se inicializó:

alembic init alembic

Se configuró alembic.ini para obtener la conexión desde .env.

En env.py se configuró:

load_dotenv()
database_url = os.getenv("DATABASE_URL")
config.set_main_option("sqlalchemy.url", database_url)

y:

target_metadata = Base.metadata

Se importaron los modelos Usuario y Pedido para registrar sus tablas en Base.metadata.

Migración inicial

Se generó:

3965e7b974fd_estado_inicial.py

Como PostgreSQL ya tenía la estructura correspondiente a los modelos, la migración inicial no necesitó operaciones estructurales.

Primera migración real

Se agregó al modelo Usuario:

telefono = Column(String)

Alembic detectó:

Detected added column 'usuarios.telefono'

y generó:

d8848d64e7cc_agregar_telefono_a_usuarios.py

La migración contiene:

def upgrade() -> None:
    op.add_column(
        'usuarios',
        sa.Column('telefono', sa.String(), nullable=True)
    )

def downgrade() -> None:
    op.drop_column('usuarios', 'telefono')

Cadena:

3965e7b974fd
       ↓
d8848d64e7cc (HEAD)

Se ejecutó:

alembic upgrade head

Después:

alembic current

Resultado:

d8848d64e7cc (head)

Finalmente se verificó directamente en PostgreSQL mediante:

\d usuarios

PostgreSQL confirmó:

id       | integer
nombre   | character varying
correo   | character varying
telefono | character varying

La columna telefono existe físicamente y la Foreign Key de pedidos.usuario_id hacia usuarios.id permanece intacta.

Concepto consolidado

create_all()
    ↓
crear estructuras inexistentes

Alembic
    ↓
evolucionar estructuras existentes
    ↓
de forma controlada y versionada

Estado

Día 87 completado.

Cadena maestra actual

FastAPI
    ↓
SQLAlchemy
    ↓
psycopg
    ↓
PostgreSQL
    ↓
bootcamp_backend
    ↓
usuarios / pedidos

Control del esquema:

Modelos SQLAlchemy
       ↓
Alembic
       ↓
Migraciones versionadas
       ↓
PostgreSQL

Relaciones:

ForeignKey
    ↓
relación en BD

relationship()
    ↓
relación ORM

join()
    ↓
consulta

joinedload() / selectinload()
    ↓
estrategia de carga

Transacciones:

db.add()
db.flush()
db.commit()
db.rollback()
db.refresh()

Estado actual

Día 87 completado.

Día 88 — Migraciones reales

Se agregó ciudad al modelo Usuario:

ciudad = Column(String)

Alembic detectó:

Detected added column 'usuarios.ciudad'

y generó:

47e20a3d7e7f_agregar_ciudad_a_usuarios.py

La migración agregó usuarios.ciudad mediante upgrade() y la elimina mediante downgrade().

Se aplicó:

alembic upgrade head

Se verificó físicamente con:

\d usuarios

La tabla quedó:

id
nombre
correo
telefono
ciudad

La FK pedidos.usuario_id → usuarios.id permaneció intacta.

Finalmente:

alembic current

mostró:

47e20a3d7e7f (head)

Estado

Día 88 de 112 — COMPLETADO

Día 89 — Migración definitiva SQLite → PostgreSQL

Se migraron los registros reales del Proyecto 1 desde app.db hacia PostgreSQL.

Usuarios:

1 → Ricardo
2 → Ana
3 → Ricardo

Pedidos:

1 → laptop  → usuario 1
2 → mouse   → usuario 1
3 → teclado → usuario 1

Se conservaron IDs y relaciones.

Se sincronizaron secuencias:

SELECT setval('usuarios_id_seq', 3);
SELECT setval('pedidos_id_seq', 3);

Se verificó que el siguiente usuario creado recibió id = 4.

Se dejó comentado:

# Base.metadata.create_all(bind=engine)

Día 89 completado.

Día 90 — Repaso PostgreSQL + SQLAlchemy

Se repasaron y consolidaron:

ForeignKey() vs relationship().

pedido.usuario_id vs pedido.usuario.

join() vs joinedload().

selectinload() y N+1.

.all(), .first(), .one(), .one_or_none().

flush(), commit(), rollback(), refresh().

SQLAlchemy vs Pydantic.

create_all() vs Alembic.

secuencias de PostgreSQL.

atomicidad de transacciones.

flujo FastAPI → SQLAlchemy → psycopg → PostgreSQL.

Día 90 completado.

Bloque 3 — Testing

Día 91 — Introducción a Testing

Se inició Testing con pytest.

pytest
assert
unit test
PASS
FAIL
pytest.raises()

Se probaron funciones pequeñas y excepciones esperadas.

Día 91 completado.

Día 92 — Testing de Services

Se probaron funciones de lógica de negocio de forma aislada.

Se verificaron:

caso válido;

cantidad cero;

cantidad negativa;

ValueError esperado.

Se consolidó que un test unitario de service debe intentar aislar la lógica de negocio de PostgreSQL.

Día 92 completado.

Día 93 — Testing de endpoints

Se incorporó TestClient.

TestClient
    ↓
HTTP request
    ↓
FastAPI
    ↓
endpoint
    ↓
HTTP response
    ↓
assert

Se verificaron:

200 correcto;

422 por tipo inválido;

404 por recurso inexistente;

response.json().

Resultado:

4 passed

Día 93 completado.

Día 94 — Tests de CRUD

Se probaron las cuatro operaciones CRUD:

CREATE → POST
READ   → GET
UPDATE → PUT
DELETE → DELETE

Tests realizados:

1. Crear producto
2. Consultar producto
3. Consultar producto inexistente
4. Actualizar producto
5. Eliminar producto
6. Verificar que el producto eliminado ya no existe

Resultado:

6 passed

Se identificó un concepto importante: los tests estaban compartiendo una lista mutable en memoria, por lo que el orden podía afectar el estado observado por otros tests.

Regla consolidada:

Idealmente, cada test debe poder ejecutarse de forma independiente.

No se profundizó todavía en fixtures ni aislamiento avanzado para respetar el roadmap.

Día 94 completado.

Estado actual

Día 94 de 112 — COMPLETADO

Progreso del roadmap

Bloque PostgreSQL
Día 81 → Día 90 ✅ COMPLETADO

Bloque Testing
Día 91 ✅
Día 92 ✅
Día 93 ✅
Día 94 ✅
Día 95 ⏳ Testing del Proyecto 1

Día 95 --- Testing del Proyecto 1

Se aplicó testing al Proyecto 1 real manteniendo separada la información
de producción. Se creó la base PostgreSQL bootcamp_backend_test, una
conexión exclusiva mediante test_engine y TestingSessionLocal, y se
usó app.dependency_overrides[get_db] = get_db_override para redirigir
los endpoints durante pytest.

Se verificó:

TestClient
    ↓
FastAPI
    ↓
Depends(get_db)
    ↓
get_db_override
    ↓
TestingSessionLocal
    ↓
bootcamp_backend_test

Se crearon las tablas usuarios y pedidos únicamente en la base de
testing, se insertaron datos controlados, se probó un endpoint real
GET /usuarios/{id} con respuesta 200, y se comprobó el caso 404
para un usuario inexistente.

Resultado final: 6 passed.

También se observó que los datos persisten entre ejecuciones y los IDs
continúan aumentando. Se reconoció la importancia del aislamiento de
tests, dejando fixtures y limpieza automática para una etapa posterior.

Estado: COMPLETADO.

Estado general

Día actual completado: 95 / 112
Bloque PostgreSQL: COMPLETADO
Bloque Testing: Días 91–95 COMPLETADOS
Próximo: Día 96 — Autenticación vs Autorización

Metodología vigente

Continuar una modificación a la vez: comprender → modificar → ejecutar →
observar → consolidar. Evitar profundizar fuera del objetivo diario y
mantener el avance según la ruta de 112 días.

Día 96 — Autenticación vs. Autorización — COMPLETADO

Autenticación

Responde: ¿Quién eres?

Está relacionada con la identidad. Sin autenticación válida, el concepto HTTP asociado estudiado es:

401 Unauthorized

Autorización

Responde: ¿Qué puedes hacer?

Está relacionada con permisos y roles. Un usuario puede estar correctamente autenticado pero no tener permiso para una operación:

usuario autenticado
        ↓
sin permiso
        ↓
403 Forbidden

Concepto central

AUTENTICACIÓN
      ↓
¿Quién eres?
      ↓
identidad

AUTORIZACIÓN
      ↓
¿Qué puedes hacer?
      ↓
permisos / roles

Reto final consolidado:

Ana
JWT válido
rol = usuario
DELETE /usuarios/5 requiere admin

Autenticada       → Sí
Autorizada DELETE → No
Respuesta         → 403

Si el rol cambia a admin, la autenticación permanece igual; lo que cambia es la autorización.

Estado del Día 96: COMPLETADO Y CONSOLIDADO.

Estado actual

Días completados: 96 / 112
PostgreSQL:       completado
Testing:          completado
Seguridad:        iniciado

Próximos días

Día 97  → Hashing de contraseñas
Día 98  → Login
Día 99  → JWT
Día 100 → JWT + FastAPI: protección de endpoints
Día 101 → get_current_user
Día 102 → Roles y permisos
Día 103 → Seguridad del Proyecto 1
Día 104 → Docker
Día 105 → Dockerizar FastAPI
Día 106 → Docker Compose: FastAPI + PostgreSQL
Día 107 → Variables de entorno + Docker
Día 108 → Proyecto 1 dockerizado
Día 109 → Conceptos de despliegue
Día 110 → Publicar Proyecto 1
Día 111 → Proyecto 2
Día 112 → Cierre, GitHub, README, CV y entrevistas

Día 96 — Autenticación vs. Autorización — COMPLETADO

Autenticación → ¿Quién eres?       → identidad → 401 si no es válida
Autorización  → ¿Qué puedes hacer? → permisos  → 403 si falta permiso

Se consolidó que autenticación no implica autorización total.

Día 97 — Hashing de contraseñas — COMPLETADO

Se implementó hashing con pwdlib + Argon2.

Se creó App/security.py con:

hash_password(...)
verify_password(...)

SQLAlchemy:

password_hash = Column(String, nullable=True)

Alembic:

e76e34cf8d6b → agregar password_hash a usuarios

El POST /usuarios ahora realiza:

password → hash_password() → password_hash → PostgreSQL

Se creó UsuarioResponse y se utilizó response_model para evitar exponer el hash.

Comprobación final:

Contraseña original almacenada → NO
Hash Argon2 almacenado          → SÍ
Hash expuesto por la API        → NO

También se detectó que PowerShell no está resolviendo correctamente los ejecutables del venv aunque muestre (venv). El entorno está sano y temporalmente se usan rutas explícitas:

.\venv\Scripts\python.exe -m uvicorn App.main:app --reload
.\venv\Scripts\alembic.exe ...
.\venv\Scripts\python.exe -m pip ...

Estado

Días completados: 97 / 112
PostgreSQL:       COMPLETADO
Testing:          COMPLETADO
Seguridad:        Días 96–97 completados

Próximos días

Día 98  → Login
Día 99  → JWT
Día 100 → JWT + FastAPI
Día 101 → get_current_user
Día 102 → Roles y permisos
Día 103 → Seguridad Proyecto 1
Día 104 → Docker
Día 105 → Dockerizar FastAPI
Día 106 → Docker Compose
Día 107 → Variables de entorno + Docker
Día 108 → Proyecto 1 dockerizado
Día 109 → Deploy: conceptos
Día 110 → Publicar Proyecto 1
Día 111 → Proyecto 2
Día 112 → Cierre, GitHub, README, CV e entrevistas

Día 98 — Login — COMPLETADO

Se creó:

class LoginRequest(BaseModel):
    correo: str
    password: str

Consulta:

usuario = db.query(Usuario).filter(
    Usuario.correo == data.correo
).first()

Protección:

if usuario is None or usuario.password_hash is None:
    raise HTTPException(
        status_code=401,
        detail="Credenciales incorrectas"
    )

Verificación:

if not verify_password(
    data.password,
    usuario.password_hash
):
    raise HTTPException(
        status_code=401,
        detail="Credenciales incorrectas"
    )

Respuesta temporal de éxito:

{"mensaje": "Login correcto"}

Pruebas verificadas:

Correo válido + password correcta       → Login correcto
Correo válido + password incorrecta     → 401
Usuario antiguo con password_hash NULL  → 401
Correo inexistente                      → 401 por diseño

Se consolidó que Credenciales incorrectas evita revelar si una cuenta concreta existe.

Estado actual

Días completados: 98 / 112
PostgreSQL 81–90 → COMPLETADO
Testing    91–95 → COMPLETADO
Seguridad  96–98 → COMPLETADO hasta Día 98

Restan 14 días del plan.

Próximos días

Día 99  → JWT
Día 100 → JWT + FastAPI: proteger endpoints
Día 101 → get_current_user
Día 102 → Roles y permisos
Día 103 → Seguridad Proyecto 1
Día 104 → Docker
Día 105 → Dockerizar FastAPI
Día 106 → Docker Compose
Día 107 → Variables de entorno + Docker
Día 108 → Proyecto 1 dockerizado
Día 109 → Deploy: conceptos
Día 110 → Publicar Proyecto 1
Día 111 → Proyecto 2
Día 112 → Cierre, GitHub, README, documentación, CV e entrevistas

Día 99 — JWT — COMPLETADO

Se instaló PyJWT 2.14.0.

En App/security.py:

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
create_access_token(...)
decode_access_token(...)

La clave permanece en .env. Se corrigió una clave inicial demasiado corta tras InsecureKeyLengthWarning, generando una nueva con secrets.token_hex(32). La longitud comprobada de la cadena fue 64 bytes UTF-8.

El token incorpora:

sub → ID del usuario
exp → instante de expiración

Expiración configurada a 30 minutos.

Se comprobó un token expirado:

ExpiredSignatureError: Signature has expired

POST /login ahora devuelve:

{
  "access_token": "...",
  "token_type": "bearer"
}

Verificación final del token generado:

{'sub': '6', 'exp': 1789605350}

Nota de entorno vigente

PowerShell puede mostrar (venv) aunque algunos comandos resuelvan el Python global. El venv está sano; cuando sea necesario se usan rutas explícitas:

.\venv\Scripts\python.exe -m uvicorn App.main:app --reload
.\venv\Scripts\python.exe -m pip ...
.\venv\Scripts\alembic.exe ...

Estado actual

Completados: 99 / 112
Restantes:   13


Día 100 — JWT + FastAPI — COMPLETADO

Se incorporaron:

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

security = HTTPBearer()

Conceptos:

HTTPBearer
→ busca/extrae credenciales Bearer

decode_access_token()
→ verifica JWT
→ firma + expiración
→ payload

Práctica /protegido:

sin credenciales → 401
JWT válido        → 200

Se diagnosticó:

jwt.exceptions.DecodeError: Not enough segments

Un token mal formado inicialmente provocó 500 porque la excepción no estaba manejada.

Corrección:

try:
    decode_access_token(token)
except jwt.PyJWTError:
    raise HTTPException(
        status_code=401,
        detail="Token inválido o expirado"
    )

Resultados:

JWT inválido/expirado → 401
JWT válido            → 200

Se protegió el endpoint real GET /usuarios.

Flujo:

GET /usuarios
→ Depends(security)
→ credentials.credentials
→ decode_access_token()
→ inválido: 401
→ válido: consultar PostgreSQL
→ 200

Pruebas finales:

/usuarios sin autorización → 401
/usuarios con JWT válido    → 200

Distinción consolidada:

HTTPBearer se encarga de buscar el header de autorización y obliga a presentar credenciales, mientras que decode_access_token() se encarga de verificar el JWT.

Estado

Completados: 100 / 112
Restantes:    12

Próximos días

101 → get_current_user
102 → roles y permisos admin/user
103 → seguridad Proyecto 1
104 → Docker
105 → Dockerizar FastAPI
106 → Docker Compose
107 → variables de entorno + Docker
108 → Proyecto 1 dockerizado
109 → despliegue
110 → publicar Proyecto 1
111 → Proyecto 2
112 → cierre, GitHub, README, CV e entrevistas

## Día 101 — get_current_user
Se creó una dependencia reutilizable que:
```text
HTTPBearer
→ obtiene JWT
→ decode_access_token()
→ obtiene sub
→ busca Usuario en PostgreSQL
→ devuelve objeto ORM
→ current_user
```

Se incorporó `db: Session = Depends(get_db)` y la búsqueda:
```python
usuario_id = payload["sub"]
usuario = db.query(Usuario).filter(
    Usuario.id == int(usuario_id)
).first()
```

Si el usuario no existe:
```python
if usuario is None:
    raise HTTPException(status_code=401, detail="Usuario no válido")
```

`GET /usuarios` quedó usando:
```python
current_user: Usuario = Depends(get_current_user)
```

Pruebas:
```text
sin autorización → 401
JWT válido        → 200
```

Se creó `GET /mi-perfil`. Con el JWT cuyo `sub` era `"6"`, devolvió `id = 6`, confirmando:
```text
JWT → sub → PostgreSQL → Usuario → current_user
```

Distinción consolidada:
```text
credentials.credentials → JWT completo
payload["sub"]           → ID extraído
current_user             → objeto Usuario
```

## Estado
```text
Completados: 101 / 112
Restantes:    11