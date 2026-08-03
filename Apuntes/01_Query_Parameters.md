# Día 48 — Query Parameters

## Objetivo

Comprender y utilizar query parameters en FastAPI para modificar o filtrar una consulta.

## Relación con el Día 47

Los path parameters identifican un recurso específico:

```text
/usuarios/1
```

Los query parameters filtran o modifican una consulta:

```text
/usuarios?nombre=Ana
```

## Concepto

Un query parameter se escribe después del signo `?` en una URL.

```text
/usuarios?nombre=Ana
```

En este caso:

- La ruta es `/usuarios`.
- `nombre` es el parámetro.
- `Ana` es el valor enviado.

## Parámetro obligatorio y opcional

Un parámetro obligatorio se define así:

```python
nombre: str
```

Si no se envía, FastAPI responde con error 422.

Un parámetro opcional se define así:

```python
nombre: str | None = None
```

Si no se envía, toma el valor `None`.

## Código trabajado

```python
@app.get("/usuarios")
def listar_usuarios(nombre: str | None = None):
    if nombre is None:
        return usuarios

    usuarios_filtrados = [
        usuario
        for usuario in usuarios
        if nombre.lower() in usuario["nombre"].lower()
    ]

    return usuarios_filtrados
```

## Rutas probadas

| Ruta | Resultado |
| --- | --- |
| `/usuarios` | Devuelve todos los usuarios |
| `/usuarios?nombre=Ana` | Devuelve a Ana |
| `/usuarios?nombre=an` | Devuelve a Ana y Andrés |
| `/usuarios?nombre=Pedro` | Devuelve una lista vacía |

## Conclusión

Los query parameters permiten filtrar una colección sin cambiar la ruta principal. Una consulta sin resultados devuelve una lista vacía y estado 200, porque la solicitud fue válida.

## Siguiente paso

En el Día 49 combinaré path parameters y query parameters, y aplicaré validaciones a los datos de entrada.