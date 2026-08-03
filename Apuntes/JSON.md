# JSON

## ¿Qué es JSON?

JSON (JavaScript Object Notation) es un formato estándar para intercambiar datos entre aplicaciones.

Es el lenguaje que utilizan la mayoría de las APIs para comunicarse.

## Tipos de datos

- Objeto → `{ }`
- Lista → `[ ]`
- Cadena → `"texto"`
- Número → `25`
- Booleano → `true` / `false`
- Nulo → `null`

## Regla para analizar un JSON

No intentar leer todo al mismo tiempo.

Analizar por niveles:

1. Identificar el nivel superior.
2. Identificar las claves principales.
3. Identificar el tipo de dato de cada clave.
4. Descender únicamente hasta la información que se necesita.

## Idea clave

Un JSON grande no es complicado; simplemente está organizado en varios niveles.

## Navegación en JSON anidados

Para recorrer un JSON debemos identificar el tipo de dato en cada nivel.

### Regla

- Si el nivel es un objeto (`{}`), se accede mediante una clave:

```python
datos["nombre"]
```

- Si el nivel es una lista (`[]`), se accede mediante un índice:

```python
datos[0]
```

### Estrategia

1. Identificar el nivel superior.
2. Determinar si es objeto o lista.
3. Avanzar un nivel a la vez.
4. Repetir hasta llegar al dato deseado.

### Idea clave

Cada nivel del JSON determina cómo debe accederse al siguiente.

Nivel 1
¿Objeto o lista?

↓

Nivel 2
¿Objeto o lista?

↓

Nivel 3
¿Objeto o lista?

↓

...

↓

Dato buscado

## JSON de APIs reales

Las respuestas de una API suelen contener dos tipos de información:

### Datos principales

Representan el recurso solicitado.

Ejemplos:

- usuarios
- productos
- pedidos

### Metadatos

Describen la respuesta.

Ejemplos:

- page
- total
- total_pages
- per_page

### Estrategia para analizar una respuesta

1. Identificar el nivel superior.
2. Identificar las claves principales.
3. Determinar qué claves contienen datos y cuáles contienen metadatos.
4. Navegar únicamente hasta la información necesaria.

### Idea clave

En una API real, no todo el JSON representa el recurso principal; gran parte de la respuesta puede ser información de contexto.

Actualización del Mapa Conceptual del Backend

Nuestro mapa sigue creciendo:

BACKEND
│
├── Internet
├── HTTP
├── APIs
├── JSON
│   ├── Objetos
│   ├── Listas
│   ├── Valores
│   ├── Niveles
│   ├── JSON anidados
│   ├── Datos
│   └── Metadatos
│
├── Python
│   └── requests
│
└── Git

## Analizando respuestas reales con requests

Después de realizar una petición:

```python
r = requests.get(url)
```

La estrategia recomendada es:

1. Verificar `r.status_code`.
2. Convertir la respuesta con `r.json()`.
3. Identificar el tipo de dato (`type()`).
4. Analizar la estructura (lista, objeto, claves).
5. Acceder únicamente al dato necesario.

### Flujo de trabajo

Response → JSON → Objetos Python → Datos

### Idea clave

Antes de acceder a un dato específico, primero debo comprender la estructura completa de la respuesta.

Nuestro mapa continúa creciendo:

BACKEND
│
├── Internet
├── HTTP
│   ├── Request
│   ├── Response
│   ├── Status Codes
│   └── Headers
│
├── APIs
│
├── JSON
│   ├── Objetos
│   ├── Listas
│   ├── Navegación
│   ├── Datos
│   ├── Metadatos
│   └── Respuestas reales
│
├── Python
│   └── requests
│       ├── get()
│       ├── Response
│       ├── json()
│       ├── type()
│       └── len()
│
└── Git