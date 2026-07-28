# Día 51 - Field() y Validaciones con Pydantic

## ¿Qué aprendimos?

Aprendimos que validar únicamente el tipo de dato no siempre es suficiente.

Pydantic permite utilizar `Field()` para agregar reglas adicionales que garanticen que la información recibida también cumpla las reglas del negocio antes de ejecutar la función.

Además, realizamos nuestras primeras pruebas reales utilizando **Swagger**, enviando peticiones POST y observando las respuestas automáticas de FastAPI.

---

## Conceptos importantes

### Field()

`Field()` permite agregar restricciones adicionales a los atributos de un modelo.

Ejemplo:

```python
edad: int = Field(ge=18)
```

Esto significa:

- el valor debe ser un entero;
- además debe ser mayor o igual a 18.

---

### Validaciones numéricas

```python
Field(gt=0)
```

Mayor que.

```python
Field(ge=0)
```

Mayor o igual que.

```python
Field(lt=100)
```

Menor que.

```python
Field(le=100)
```

Menor o igual que.

---

### Validaciones de texto

```python
Field(min_length=3)
```

Longitud mínima.

```python
Field(max_length=50)
```

Longitud máxima.

---

### Swagger

Swagger es una interfaz web generada automáticamente por FastAPI que permite:

- visualizar los endpoints;
- probar peticiones;
- enviar Request Body;
- ver respuestas;
- analizar errores;
- validar el funcionamiento de la API.

Se encuentra en:

```text
http://127.0.0.1:8000/docs
```

---

## Ejemplo

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Usuario(BaseModel):
    nombre: str = Field(min_length=3, max_length=50)
    edad: int = Field(ge=18, le=120)
    ciudad: str = Field(min_length=2, max_length=50)


@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    return usuario
```

---

## Flujo de trabajo

Cliente

↓

Request Body (JSON)

↓

FastAPI recibe la petición

↓

Pydantic valida tipos

↓

Field() valida restricciones

↓

Si todo es válido:

↓

Se ejecuta la función

↓

Response

---

## Idea clave

Los tipos de datos validan la estructura.

`Field()` valida las reglas del negocio.

---

## Errores comunes

❌ Pensar que `str` garantiza datos válidos.

❌ Pensar que `int` evita valores negativos.

❌ No validar longitudes mínimas.

❌ No validar rangos numéricos.

❌ Guardar datos sin validarlos.

---

## Buenas prácticas

- Validar los datos antes de almacenarlos.
- Crear reglas claras para cada atributo.
- Utilizar `Field()` siempre que exista una restricción del negocio.
- Aprovechar la validación automática de FastAPI.
- Probar los endpoints desde Swagger.

---

## ¿Cuándo usarlo?

Usaremos `Field()` cuando:

- exista una edad mínima;
- exista una longitud mínima;
- exista una longitud máxima;
- un número no pueda ser negativo;
- necesitemos proteger la integridad de la información.

---

## Conexión con conocimientos anteriores

Este tema se relaciona con:

- HTTP → El Request Body forma parte de la petición HTTP.
- JSON → Los datos enviados viajan normalmente en formato JSON.
- Programación Orientada a Objetos → Pydantic utiliza clases para representar modelos.
- FastAPI → Utiliza Pydantic para validar automáticamente las peticiones.
- Día 50 → Request Body y modelos BaseModel.

---

## Relación con el Proyecto 1

Antes:

```python
class Usuario(BaseModel):
    nombre: str
    edad: int
    ciudad: str
```

Ahora:

```python
class Usuario(BaseModel):
    nombre: str = Field(min_length=3, max_length=50)
    edad: int = Field(ge=18, le=120)
    ciudad: str = Field(min_length=2, max_length=50)
```

Nuestra API ya no solo recibe información.

Ahora también protege la calidad de la información.

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
├── JSON
│
├── APIs REST
│   ├── Path Parameters
│   ├── Query Parameters
│   └── Request Body
│
├── FastAPI
│   ├── Rutas
│   ├── GET
│   ├── POST
│   ├── Path Parameters
│   ├── Query Parameters
│   ├── Pydantic
│   ├── BaseModel
│   ├── Field()
│   └── Swagger
│
├── Programación Orientada a Objetos
│
└── Git

---

## Resumen

En este tema aprendimos que una API profesional no solo valida tipos de datos.

También debe validar reglas del negocio.

Pydantic y `Field()` permiten realizar estas validaciones automáticamente antes de ejecutar la función.

Además, conocimos Swagger, la herramienta que utilizaremos constantemente para probar nuestras APIs durante todo el desarrollo de nuestros proyectos.