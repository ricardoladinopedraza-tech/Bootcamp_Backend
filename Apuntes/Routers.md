# Día 56 – Routers en FastAPI

## Objetivo

Aprender a organizar una aplicación FastAPI mediante el uso de `APIRouter`, separando los endpoints en diferentes archivos para mejorar la organización, el mantenimiento y la escalabilidad del proyecto.

---

# ¿Qué es un Router?

Un **Router** (`APIRouter`) es un componente de FastAPI que permite agrupar endpoints relacionados.

En lugar de colocar todas las rutas en `main.py`, podemos distribuirlas en diferentes archivos según su funcionalidad.

Ejemplo:

- usuarios.py
- pacientes.py
- medicos.py
- citas.py

Cada archivo administra únicamente los endpoints relacionados con ese módulo.

---

# ¿Por qué utilizar Routers?

A medida que una API crece, aumenta el número de endpoints.

Mantener todas las rutas en un único archivo hace que:

- El código sea difícil de leer.
- Sea más complejo realizar mantenimiento.
- Aumenten los conflictos cuando varias personas trabajan sobre el mismo archivo.
- Sea más difícil localizar un endpoint específico.

Los Routers solucionan este problema permitiendo dividir la aplicación en módulos independientes.

---

# Creación de un Router

```python
from fastapi import APIRouter

router = APIRouter()
```

A partir de este momento las rutas pertenecen al router.

```python
@router.get("/usuarios")
def listar_usuarios():
    return {
        "mensaje": "Lista de usuarios"
    }
```

---

# Integración con FastAPI

En el archivo principal:

```python
from fastapi import FastAPI
from usuarios import router

app = FastAPI()

app.include_router(router)
```

El método:

```python
app.include_router(router)
```

incorpora todas las rutas definidas en ese archivo a la aplicación principal.

---

# Flujo de trabajo

Cliente

↓

FastAPI recibe la petición

↓

main.py

↓

include_router()

↓

Router correspondiente

↓

Endpoint

↓

Validación (Pydantic)

↓

Función

↓

Response

↓

Cliente

---

# Organización profesional

Un proyecto FastAPI suele organizarse de la siguiente manera:

Proyecto/

│

├── main.py

│

├── routers/
│   ├── usuarios.py
│   ├── pacientes.py
│   ├── medicos.py
│   └── citas.py

│

├── models/
│   ├── usuario.py
│   ├── paciente.py
│   └── cita.py

│

├── database/

│

├── services/

│

└── requirements.txt

Esta estructura facilita el crecimiento de la aplicación y el trabajo en equipo.

---

# Ventajas de utilizar Routers

- Organización del código.
- Separación de responsabilidades.
- Facilita el mantenimiento.
- Reduce conflictos en Git.
- Permite que varios desarrolladores trabajen simultáneamente.
- Hace más sencilla la búsqueda de funcionalidades.

---

# Diferencia entre app.get() y router.get()

app.get()

- Registra la ruta directamente en la aplicación principal.

router.get()

- Registra la ruta dentro de un Router.
- Posteriormente el Router es incorporado mediante `include_router()`.

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
- Listas de modelos
- Response Models
- Routers

Ya podemos crear APIs organizadas y preparadas para seguir creciendo.

---

# Idea clave

Los Routers no cambian el funcionamiento de una API.

Su objetivo es organizar el código para que sea más fácil mantenerlo, ampliarlo y trabajar en equipo.

---

# Conclusión

El uso de `APIRouter` representa una práctica estándar en el desarrollo profesional con FastAPI.

Separar la aplicación por módulos mejora la organización del proyecto y prepara la estructura para integrar bases de datos, autenticación y nuevas funcionalidades sin convertir el código en un archivo difícil de mantener.