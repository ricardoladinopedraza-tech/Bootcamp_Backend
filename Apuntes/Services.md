# Día 59 – Services (Separación de la lógica del negocio)

## Objetivo

Aprender a separar la lógica del negocio de los endpoints utilizando Services, construyendo aplicaciones más organizadas, reutilizables y fáciles de mantener.

---

# El problema

En aplicaciones pequeñas es común escribir toda la lógica dentro del endpoint.

Ejemplo:

```python
@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    # Validar información
    # Buscar usuario
    # Guardar en la base de datos
    # Registrar auditoría
    # Enviar correo

    return usuario
```

Aunque funciona, el endpoint termina realizando demasiadas tareas.

Esto dificulta:

- La lectura del código.
- El mantenimiento.
- Las pruebas.
- La reutilización.

---

# La solución: Services

Los Services contienen la lógica del negocio.

El endpoint únicamente recibe la petición y delega el trabajo al Service correspondiente.

Ejemplo:

## services/usuarios.py

```python
def crear_usuario(nombre: str):
    return {
        "mensaje": f"Usuario {nombre} creado correctamente"
    }
```

## main.py

```python
from fastapi import FastAPI
from services.usuarios import crear_usuario

app = FastAPI()

@app.get("/usuarios/{nombre}")
def crear(nombre: str):
    return crear_usuario(nombre)
```

---

# Flujo de trabajo

Cliente

↓

Request

↓

main.py

↓

Router

↓

Endpoint

↓

Service

↓

Response

↓

Cliente

---

# Responsabilidades

## Endpoint

- Recibir la petición.
- Obtener parámetros.
- Validar mediante Pydantic.
- Llamar al Service.
- Retornar la respuesta.

No debe contener la lógica del negocio.

---

## Service

Contiene la lógica del negocio.

Ejemplos:

- Crear usuarios.
- Buscar pacientes.
- Calcular descuentos.
- Generar facturas.
- Actualizar inventario.
- Registrar auditorías.

Puede ser utilizado por varios endpoints.

---

# Ventajas

- Código más limpio.
- Reutilización.
- Mantenimiento sencillo.
- Pruebas más fáciles.
- Separación de responsabilidades.
- Escalabilidad.

---

# Organización del proyecto

Proyecto_1/

├── main.py

├── routers/
│   ├── usuarios.py
│   └── productos.py

├── services/
│   ├── usuarios.py
│   ├── productos.py
│   └── ...

├── models/

├── database/

└── requirements.txt

---

# Relación con los temas anteriores

Hasta el momento conocemos:

- Path Parameters
- Query Parameters
- Validaciones
- Request Body
- Field()
- Optional
- Modelos anidados
- Listas de modelos
- Response Models
- Routers
- Prefix
- Tags
- Depends()
- Services

Cada tema incorpora una nueva capa a la arquitectura de la aplicación.

---

# Idea clave

El endpoint no realiza el trabajo.

El endpoint sabe a quién pedirle el trabajo.

El Service contiene la lógica del negocio.

---

# Conclusión

La separación mediante Services permite construir aplicaciones backend profesionales, organizadas y fáciles de mantener.

Este patrón será fundamental cuando integremos PostgreSQL, SQLAlchemy y otras tecnologías en los siguientes módulos.