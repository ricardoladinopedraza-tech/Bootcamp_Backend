# Día 50 — Request Body y modelos Pydantic

## Objetivo

Comprender cómo recibir datos estructurados en una API FastAPI mediante Request Body y modelos Pydantic.

## Relación con sesiones anteriores

- Los path parameters identifican recursos mediante la URL.
- Los query parameters filtran o modifican consultas.
- El Request Body permite enviar un objeto completo en formato JSON.

## Request Body

Un Request Body viaja dentro de una petición HTTP.

Ejemplo:

```json
{
  "nombre": "Ricardo",
  "edad": 30,
  "email": "ricardo@email.com"
}
```

Para enviar información destinada a crear un usuario se utiliza el método `POST`.

## Modelo Pydantic

```python
class Usuario(BaseModel):
    nombre: str
    edad: int
    email: str
```

El modelo define el contrato de datos que espera la API:

- `nombre` debe ser texto.
- `edad` debe ser un entero.
- `email` debe ser texto.
- Los tres campos son obligatorios.

## Ruta creada

```python
@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    return {
        "mensaje": "Usuario recibido correctamente",
        "usuario": usuario,
    }
```

FastAPI recibe el JSON, Pydantic lo valida y entrega un objeto `Usuario` a la función.

## Pruebas realizadas

| Request Body | Resultado |
| --- | --- |
| Datos válidos | Respuesta 200 con el usuario recibido |
| `"edad": "treinta"` | Error 422: `edad` debe ser un entero |
| Sin el campo `email` | Error 422: campo requerido |

## Conclusión

Pydantic permite definir y validar la estructura de los datos recibidos. Esto evita procesar solicitudes incompletas o con tipos incorrectos.

## Siguiente paso

En el Día 51 convertiré esta recepción de datos en una operación `POST` real que agregará usuarios a una lista temporal y devolverá el estado HTTP apropiado.

OTROS APUNTES AL RESUMEN  

# Día 50 - Request Body y Pydantic

## ¿Qué aprendimos?

Hasta este momento habíamos recibido información desde la URL mediante Path Parameters y Query Parameters.

En este tema aprendimos una tercera forma de recibir información en una API: el **Request Body**.

El Request Body permite enviar objetos completos en formato JSON, mientras que **Pydantic** se encarga de validar automáticamente que esos datos cumplan con la estructura esperada antes de ejecutar la función.

---

## Conceptos importantes

### Request Body

Es la parte de una petición HTTP donde se envían los datos que necesita la API.

Ejemplo:

```json
{
    "nombre": "Ricardo",
    "edad": 45,
    "ciudad": "Paipa"
}
```

---

### Pydantic

Es una biblioteca utilizada por FastAPI para:

- Definir modelos de datos.
- Validar automáticamente los datos recibidos.
- Detectar errores antes de ejecutar la función.
- Generar documentación automática en Swagger.

---

### BaseModel

Todos los modelos de Pydantic heredan de `BaseModel`.

Ejemplo:

```python
from pydantic import BaseModel

class Usuario(BaseModel):
    nombre: str
    edad: int
    ciudad: str
```

---

### Endpoint POST

Para crear recursos utilizamos normalmente el método HTTP POST.

Ejemplo:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Usuario(BaseModel):
    nombre: str
    edad: int
    ciudad: str

@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    return usuario
```

---

## Ejemplo

Cliente:

```json
{
    "nombre": "Ricardo",
    "edad": 45,
    "ciudad": "Paipa"
}
```

↓

FastAPI recibe el Request Body.

↓

Pydantic valida los datos.

↓

Se crea un objeto `Usuario`.

↓

La función se ejecuta.

↓

La API responde.

---

## Idea clave

**Cuando necesito enviar un objeto completo, utilizo el Request Body.**

**Pydantic garantiza que los datos recibidos tengan la estructura y los tipos correctos antes de ejecutar la función.**

---

## Errores comunes

❌ Enviar muchos datos mediante Query Parameters.

❌ No crear un modelo con `BaseModel`.

❌ Enviar tipos de datos incorrectos.

```json
{
    "edad": "treinta"
}
```

❌ Omitir campos obligatorios.

```json
{
    "nombre": "Ricardo"
}
```

---

## Buenas prácticas

- Crear un modelo para cada recurso importante.
- Utilizar nombres de campos claros y consistentes.
- Aprovechar la validación automática de Pydantic.
- No realizar validaciones manuales que FastAPI ya puede hacer.
- Mantener separados Path Parameters, Query Parameters y Request Body según su propósito.

---

## Flujo de trabajo

Cliente

↓

HTTP Request

↓

Request Body (JSON)

↓

FastAPI

↓

Pydantic

↓

Validación

↓

Objeto Python

↓

Función

↓

Respuesta HTTP

---

## ¿Cuándo usarlo?

### Path Parameters

Cuando necesito identificar un recurso específico.

Ejemplos:

```
GET /usuarios/15
GET /productos/8
```

---

### Query Parameters

Cuando necesito filtrar una colección de recursos.

Ejemplos:

```
GET /usuarios?ciudad=Paipa
GET /productos?categoria=Tecnologia
```

---

### Request Body

Cuando necesito enviar un objeto completo.

Ejemplos:

```
POST /usuarios
PUT /usuarios/15
PATCH /usuarios/15
```

---

## Relación con el Proyecto 1

Antes:

```
GET /usuarios
GET /usuarios/{id}
GET /usuarios?ciudad=Paipa
```

Después:

```
GET /usuarios
GET /usuarios/{id}
GET /usuarios?ciudad=Paipa

POST /usuarios
```

Nuestra API ya puede recibir información enviada por el cliente.

---

## Nuestro mapa continúa creciendo

BACKEND
│
├── Internet
│
├── HTTP
│   ├── Request
│   │   ├── URL
│   │   ├── Headers
│   │   └── Body
│   ├── Response
│   └── Status Codes
│
├── APIs REST
│   ├── Recursos
│   ├── CRUD
│   ├── Path Parameters
│   ├── Query Parameters
│   └── Request Body
│
├── JSON
│
├── FastAPI
│   ├── Rutas
│   ├── Path Parameters
│   ├── Query Parameters
│   ├── Query()
│   ├── Path()
│   ├── POST
│   └── Pydantic
│
├── Python
│   ├── requests
│   └── Programación Orientada a Objetos
│
└── Git

---

## Resumen

En este tema aprendimos que una API puede recibir información desde tres lugares diferentes:

- **Path Parameters** → Identifican un recurso.
- **Query Parameters** → Filtran una consulta.
- **Request Body** → Envía objetos completos.

Además, conocimos Pydantic, la herramienta que utiliza FastAPI para validar automáticamente los datos recibidos, generar modelos y evitar errores antes de ejecutar la lógica de la aplicación.