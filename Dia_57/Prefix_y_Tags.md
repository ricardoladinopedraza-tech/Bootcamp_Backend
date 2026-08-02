# Día 57 – Prefix y Tags en FastAPI

## Objetivo

Aprender a utilizar `prefix` y `tags` en `APIRouter` para organizar mejor una API, evitando la repetición de rutas y mejorando la documentación automática generada por Swagger.

---

# ¿Qué es un prefix?

El **prefix** es una ruta base que se asigna a un Router.

En lugar de repetir la misma ruta en cada endpoint, se define una sola vez al crear el Router.

Ejemplo:

```python
router = APIRouter(
    prefix="/usuarios"
)
```

Ahora todos los endpoints utilizarán automáticamente ese prefijo.

---

# Sin prefix

```python
@router.get("/usuarios")

@router.post("/usuarios")

@router.put("/usuarios/{id}")

@router.delete("/usuarios/{id}")
```

Existe repetición de código.

---

# Con prefix

```python
router = APIRouter(
    prefix="/usuarios"
)

@router.get("/")

@router.post("/")

@router.put("/{id}")

@router.delete("/{id}")
```

FastAPI construye automáticamente las rutas completas.

---

# ¿Qué son los tags?

Los **tags** permiten organizar los endpoints dentro de Swagger.

Ejemplo:

```python
router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)
```

Swagger mostrará una sección llamada:

Usuarios

y dentro de ella aparecerán todos los endpoints relacionados.

---

# Ejemplo completo

```python
from fastapi import APIRouter

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

@router.get("/")
def listar():
    return {"mensaje": "Lista de usuarios"}

@router.post("/")
def crear():
    return {"mensaje": "Usuario creado"}
```

---

# Resultado

FastAPI genera automáticamente:

GET      /usuarios

POST     /usuarios

---

# Flujo de trabajo

Cliente

↓

main.py

↓

include_router()

↓

Router correspondiente

↓

Endpoint

↓

Validación

↓

Función

↓

Respuesta

↓

Cliente

---

# Ventajas del prefix

- Evita repetir rutas.
- Reduce errores de escritura.
- Hace el código más limpio.
- Facilita el mantenimiento.

---

# Ventajas de los tags

- Organizan Swagger.
- Agrupan endpoints relacionados.
- Facilitan la navegación.
- Mejoran la documentación.

---

# Organización de una API clínica

Tags sugeridos:

- Usuarios
- Pacientes
- Médicos
- Especialidades
- Citas
- Medicamentos
- Historias Clínicas
- Laboratorios
- EPS
- Facturación

---

# Relación con los temas anteriores

Hasta este momento conocemos:

- Path Parameters
- Query Parameters
- Request Body
- Pydantic
- Field
- Optional
- Modelos anidados
- Listas
- Response Models
- Routers
- Prefix
- Tags

Cada nuevo tema complementa la arquitectura de una API profesional.

---

# Idea clave

`prefix` y `tags` no modifican el funcionamiento de una API.

Su propósito es mejorar la organización del código y de la documentación.

---

# Conclusión

El uso de `prefix` y `tags` representa una buena práctica en FastAPI.

Permiten construir aplicaciones más limpias, fáciles de mantener y preparadas para crecer sin perder organización.