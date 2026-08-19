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