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