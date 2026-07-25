# Día 47 — Path Parameters

## Objetivo

Comprender y aplicar parámetros de ruta en FastAPI para identificar recursos de forma dinámica.

## Concepto

Un path parameter es la parte variable de una URL.

Ejemplo:

```text
/usuarios/1
```

En esta URL, `1` es el valor de `usuario_id`.

## Código trabajado

```python
@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int):
    ...
```

`usuario_id: int` indica que FastAPI debe recibir un número entero. Si recibe texto, como `/usuarios/abc`, responde con un error de validación 422.

## Rutas probadas

| Ruta | Resultado |
| --- | --- |
| `/usuarios` | Devuelve la lista de usuarios |
| `/usuarios/1` | Devuelve el usuario con ID 1 |
| `/usuarios/99` | Devuelve error 404: usuario no encontrado |
| `/usuarios/abc` | Devuelve error 422 por no ser un entero |

## Conclusión

Los path parameters permiten identificar recursos específicos. Serán fundamentales para las operaciones CRUD de la API de Gestión de Usuarios.

## Siguiente paso

En el Día 48 aprenderé Query Parameters, que permitirán filtrar recursos sin identificarlos directamente.