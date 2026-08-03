# Día 58 – Depends() e Inyección de Dependencias

## Objetivo

Aprender a reutilizar lógica común mediante `Depends()`, evitando duplicar código y facilitando el mantenimiento de una aplicación FastAPI.

---

# El problema

En aplicaciones reales es frecuente que varios endpoints necesiten realizar exactamente la misma tarea antes de ejecutar su lógica principal.

Ejemplos:

- Verificar autenticación.
- Validar permisos.
- Obtener el usuario autenticado.
- Abrir una conexión a la base de datos.
- Registrar auditoría.

Si esa lógica se escribe en cada endpoint, el código se vuelve repetitivo y difícil de mantener.

---

# ¿Qué es una dependencia?

Una dependencia es una **función reutilizable** que FastAPI ejecuta automáticamente cuando un endpoint la necesita.

Su objetivo es realizar tareas comunes antes (o como parte) de la ejecución del endpoint.

---

# Depends()

FastAPI utiliza `Depends()` para indicar que un endpoint necesita ejecutar una dependencia.

Ejemplo:

```python
from fastapi import FastAPI, Depends

app = FastAPI()

def verificar_usuario():
    return "Ricardo autenticado"

@app.get("/usuarios")
def listar(usuario: str = Depends(verificar_usuario)):
    return {
        "mensaje": usuario
    }
```

---

# Flujo de trabajo

Cliente

↓

Request

↓

FastAPI

↓

Depends()

↓

Función de dependencia

↓

Resultado

↓

Endpoint

↓

Response

↓

Cliente

---

# Ventajas de utilizar Depends()

- Evita repetir código.
- Centraliza la lógica común.
- Facilita el mantenimiento.
- Reduce errores.
- Permite reutilizar funciones en múltiples endpoints.
- Hace la aplicación más modular.

---

# Ejemplos de dependencias

En proyectos reales suelen utilizarse para:

- Autenticación.
- Validación de permisos.
- Obtención del usuario autenticado.
- Conexión a la base de datos.
- Registro de auditoría.
- Validación de tokens.
- Configuración compartida.

---

# Relación con los temas anteriores

Hasta este momento conocemos:

- Path Parameters
- Query Parameters
- Request Body
- Pydantic
- Field()
- Optional
- Modelos anidados
- Listas de modelos
- Response Models
- Routers
- Prefix
- Tags
- Depends()

Cada uno de estos conceptos aporta una pieza a la arquitectura de una API profesional.

---

# Idea clave

No toda función es una dependencia.

Pero toda dependencia es una función reutilizable que FastAPI ejecuta automáticamente cuando un endpoint la necesita.

---

# Conclusión

`Depends()` es una de las herramientas más importantes de FastAPI.

Permite separar responsabilidades, reutilizar lógica y preparar la aplicación para trabajar con autenticación, bases de datos y otros componentes sin duplicar código.