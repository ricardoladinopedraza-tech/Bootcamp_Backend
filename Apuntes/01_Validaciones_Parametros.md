# Día 49 — Validaciones y múltiples parámetros

## Objetivo

Aplicar validaciones a query parameters y combinar varios parámetros en una misma consulta.

## Relación con sesiones anteriores

- Día 47: los path parameters identifican recursos.
- Día 48: los query parameters filtran colecciones.
- Día 49: los query parameters pueden tener reglas de validación.

## Validación con Query

```python
limite: int = Query(
    default=10,
    ge=1,
    le=10,
)
```

Significado:

- `int`: el valor debe ser entero.
- `default=10`: valor usado si no se envía el parámetro.
- `ge=1`: valor mínimo permitido.
- `le=10`: valor máximo permitido.

Si el valor no cumple una regla, FastAPI responde con estado 422 antes de ejecutar la función.

## Múltiples parámetros

La API puede recibir varios query parameters separados por `&`.

```text
/usuarios?nombre=an&limite=1
```

En esta consulta:

- `nombre=an` filtra los usuarios.
- `limite=1` limita la cantidad de resultados.

## Código trabajado

```python
@app.get("/usuarios")
def listar_usuarios(
    nombre: str | None = Query(
        default=None,
        min_length=2,
        max_length=20,
    ),
    limite: int = Query(
        default=10,
        ge=1,
        le=10,
    ),
):
    usuarios_filtrados = usuarios

    if nombre is not None:
        usuarios_filtrados = [
            usuario
            for usuario in usuarios
            if nombre.lower() in usuario["nombre"].lower()
        ]

    return usuarios_filtrados[:limite]
```

## Pruebas realizadas

| Ruta | Resultado |
| --- | --- |
| `/usuarios` | Devuelve todos los usuarios |
| `/usuarios?limite=1` | Devuelve un usuario |
| `/usuarios?nombre=an` | Devuelve Ana y Andrés |
| `/usuarios?nombre=an&limite=1` | Devuelve únicamente a Ana |
| `/usuarios?nombre=a` | Devuelve error 422 por longitud mínima |

## Conclusión

Las validaciones protegen la API contra datos inválidos. Al combinar filtros y límites, primero se filtran los recursos y después se limita el resultado.

## Siguiente paso

En el Día 50 crearé modelos Pydantic y aprenderé a recibir información mediante Request Body.

Nuestro mapa va asi:

BACKEND
│
├── Internet
│
├── HTTP
│   ├── Request
│   ├── Response
│   ├── Status Codes
│   └── Headers
│
├── APIs REST
│   ├── Recursos
│   ├── CRUD
│   ├── Path Parameters
│   └── Query Parameters
│
├── FastAPI
│   ├── Rutas
│   ├── Path Parameters
│   ├── Query Parameters
│   ├── Query()
│   └── Path()
│
├── JSON
│
├── Python
│   ├── requests
│   └── FastAPI
│
└── Git