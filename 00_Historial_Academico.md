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