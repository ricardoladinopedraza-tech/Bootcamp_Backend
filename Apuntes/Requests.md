# Requests

## ¿Qué es requests?

Requests es una librería de Python que permite realizar peticiones HTTP de forma sencilla.

## Métodos HTTP más utilizados

- GET
- POST
- PUT
- PATCH
- DELETE

## Objeto Response

Toda petición realizada con **requests** devuelve un objeto **Response**.

La función `requests.get()` devuelve un objeto `Response`.

## Ejemplo

```python
import requests

r = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

print(r.status_code)
```

¡Y ya habrás creado tu primera documentación técnica!

---

# Lo que usaremos en el Bootcamp

No vamos a aprender Markdown completo. Con estas herramientas cubriremos aproximadamente el **95 %** de la documentación que escribirás:

| Símbolo | Uso |
|---------|-----|
| `#` | Título principal |
| `##` | Subtítulo |
| `-` | Lista |
| `**texto**` | Negrita |
| `` `código` `` | Código en una línea |
| ```python | Bloque de código |

Eso es prácticamente todo lo que necesitaremos durante varios meses.

---

# Mini ejercicio

Crea el archivo `Requests.md` siguiendo la estructura anterior y ábrelo en VS Code.

Si usas VS Code, presiona **Ctrl + Shift + V**. Verás una **vista previa** donde el archivo se renderiza exactamente como aparecerá en GitHub. Es una forma muy agradable de comprobar que tu documentación está bien escrita.

---

# Nuestra nueva metodología

A partir de mañana, cada vez que terminemos un tema importante:

1. 📖 Aprendemos la teoría.
2. 💻 Escribimos el código.
3. 🧠 Resolvemos ejercicios.
4. 🛠️ Hacemos un mini proyecto.
5. 📝 Actualizamos el archivo Markdown correspondiente (`Requests.md`, `HTTP.md`, `JSON.md`, etc.).
6. 🌳 Hacemos el commit en Git cuando corresponda.

Con esto no solo aprenderás a programar, sino también a **documentar como un desarrollador profesional**.

---

## Tarea para hoy

Solo una, muy sencilla:

- Crea `Academia/Apuntes/Requests.md`.
- Escribe el contenido que vimos arriba.
- Ábrelo en la vista previa de VS Code (`Ctrl + Shift + V`) y observa cómo cambia el texto.

Mañana retomaremos el **Bootcamp Backend – Día 09**, y al final de la sesión actualizaremos `Requests.md` con lo nuevo que aprendamos. A partir de ese momento, ese archivo crecerá contigo durante todo el módulo de `requests`.

## Headers HTTP

Los Headers son información adicional que acompaña una petición o una respuesta HTTP.

No contienen los datos principales del recurso, sino metadatos sobre la comunicación.

### Header importante

**Content-Type**

Indica el tipo de contenido que contiene el Body.

Ejemplos:

- `application/json`
- `text/html`
- `image/png`
- `application/pdf`

### En Python

```python
print(r.headers)

print(r.headers["Content-Type"])
```

### Idea clave

Antes de procesar el Body, el cliente consulta el `Content-Type` para saber cómo interpretar los datos.

## URL y Reason

### r.url

Devuelve la URL final utilizada para obtener la respuesta. Es útil para identificar redirecciones o cambios en la petición.

```python
print(r.url)
```

### r.reason

Devuelve una descripción breve del código de estado HTTP.

Ejemplos:

- `200 → OK`
- `404 → Not Found`
- `500 → Internal Server Error`

```python
print(r.reason)
```

### Idea clave

`status_code` indica **el número** del resultado de la petición, mientras que `reason` proporciona una **descripción textual**. Ambos ayudan a interpretar rápidamente la respuesta del servidor.

## Enviar información con requests

### params=

Se utiliza para enviar Query Parameters en la URL.

```python
requests.get(url, params={"categoria": "teclados"})
```

### headers=

Permite enviar información adicional en la petición.

```python
headers = {"User-Agent": "MiAplicacion"}
```

### json=

Convierte automáticamente un diccionario de Python en JSON y lo envía en el Body.

```python
requests.post(url, json={"nombre": "Ricardo"})
```

### data=

Se utiliza principalmente para enviar datos de formularios.

### Idea clave

- `params=` → URL.
- `headers=` → Metadatos de la petición.
- `json=` → Body en formato JSON.
- `data=` → Body para formularios.

## Laboratorio del objeto Response

Cuando recibimos una respuesta HTTP, es recomendable inspeccionarla en este orden:

1. `status_code` → ¿La petición fue exitosa?
2. `reason` → ¿Qué significa el código?
3. `url` → ¿Qué URL respondió finalmente?
4. `elapsed` → ¿Cuánto tardó?
5. `headers` → ¿Qué tipo de contenido recibimos?
6. Elegir cómo leer el Body:
   - `json()` para `application/json`
   - `text` para contenido de texto
   - `content` para archivos o datos binarios

### Idea clave

No debemos intentar interpretar el contenido del Body antes de conocer el resultado de la petición y el tipo de contenido recibido.

## Depuración de APIs (Parte 1)

Cuando una petición falla, no debo asumir la causa del problema.

### Protocolo de diagnóstico

1. Revisar `status_code`.
2. Revisar `reason`.
3. Revisar `url`.
4. Revisar `headers`.
5. Analizar `text` o `json()`.

### Errores del cliente (4xx)

Indican que la solicitud realizada por el cliente tiene algún problema.

Ejemplos:

- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found

### Errores del servidor (5xx)

Indican que el servidor encontró un problema al procesar la solicitud.

Ejemplos:

- 500 Internal Server Error
- 502 Bad Gateway
- 503 Service Unavailable

### Idea clave

Antes de modificar el código, debo recopilar información sobre la respuesta recibida.

Actualización del Mapa Conceptual del Backend
BACKEND
│
├── Internet
├── HTTP
│   ├── Request
│   ├── Response
│   ├── Status Codes
│   ├── Errores 4xx
│   └── Errores 5xx
│
├── APIs
├── JSON
├── Python
│   └── requests
│       ├── get()
│       ├── Response
│       ├── Depuración
│       └── Diagnóstico
│
└── Git

## Depuración de APIs (Parte 2)

Los errores pueden provenir de dos lugares:

### Errores HTTP

Son respuestas enviadas por el servidor.

Ejemplos:

- 404 Not Found
- 500 Internal Server Error

### Errores de Python

Se producen cuando procesamos la respuesta.

Ejemplos:

- IndexError
- KeyError
- TypeError

### Protocolo de análisis

1. Leer el tipo de error.
2. Leer el mensaje completo.
3. Verificar la estructura de los datos.
4. Identificar la causa.
5. Corregir el código.

### Idea clave

No debo corregir un error antes de comprender exactamente qué lo produjo.

Actualización del Mapa Conceptual del Backend
BACKEND
│
├── Internet
├── HTTP
│   ├── Request
│   ├── Response
│   ├── Status Codes
│   ├── Errores 4xx
│   └── Errores 5xx
│
├── APIs
│
├── JSON
│
├── Python
│   └── requests
│       ├── Response
│       ├── Diagnóstico
│       ├── Depuración
│       ├── KeyError
│       ├── IndexError
│       └── TypeError
│
└── Git

## Depuración de APIs (Parte 3)

### Programación defensiva

Es escribir código preparado para manejar situaciones inesperadas.

### Buenas prácticas

1. Verificar `status_code` antes de procesar la respuesta.
2. Convertir con `json()`.
3. Verificar el tipo de dato (`type()`).
4. Comprobar la estructura (`len()`, claves).
5. Utilizar `get()` cuando sea apropiado.

### Método get()

```python
usuario.get("phone")
usuario.get("phone", "No disponible")
```

Evita producir un `KeyError` cuando la clave no existe.

### Idea clave

Antes de acceder a un dato, debo comprobar que realmente existe.

BACKEND
│
├── Internet
├── HTTP
│   ├── Request
│   ├── Response
│   ├── Status Codes
│   ├── Errores 4xx
│   └── Errores 5xx
│
├── APIs
│
├── JSON
│
├── Python
│   └── requests
│       ├── Response
│       ├── JSON
│       ├── Depuración
│       ├── Programación defensiva
│       ├── get()
│       ├── len()
│       └── type()
│
└── Git

## APIs REST (Parte 2)

### Método POST

El método POST se utiliza para crear nuevos recursos en una API REST.

### Envío de datos

Con la librería `requests` se recomienda usar:

```python
requests.post(url, json=datos)
```

Esto convierte automáticamente el diccionario a JSON y agrega el encabezado `Content-Type: application/json`.

### Código HTTP esperado

- 201 Created → El recurso fue creado correctamente.

### Buenas prácticas

1. Verificar `status_code`.
2. Obtener la respuesta con `json()`.
3. Procesar los datos devueltos por la API.

### Idea clave

Con `GET` solicitamos información; con `POST` enviamos información para crear un nuevo recurso.

## APIs REST (Parte 2)

### Método POST

El método POST se utiliza para crear nuevos recursos en una API REST.

### Envío de datos

Con la librería `requests` se recomienda usar:

```python
requests.post(url, json=datos)
```

Esto convierte automáticamente el diccionario a JSON y agrega el encabezado `Content-Type: application/json`.

### Código HTTP esperado

- 201 Created → El recurso fue creado correctamente.

### Buenas prácticas

1. Verificar `status_code`.
2. Obtener la respuesta con `json()`.
3. Procesar los datos devueltos por la API.

### Idea clave

Con `GET` solicitamos información; con `POST` enviamos información para crear un nuevo recurso.

BACKEND
│
├── Internet
├── HTTP
│   ├── GET
│   ├── POST
│   ├── PUT
│   ├── PATCH
│   └── DELETE
│
├── APIs REST
│   ├── Recursos
│   ├── URLs
│   ├── GET → Consultar
│   └── POST → Crear
│
├── JSON
│
├── Python
│   └── requests
│       ├── get()
│       ├── post()
│       ├── json=
│       └── status_code
│
└── Git

## APIs REST (Parte 3)

### Método PUT

Se utiliza para reemplazar completamente un recurso existente.

Ejemplo:

```python
requests.put(url, json=datos)
```

### Método PATCH

Se utiliza para modificar parcialmente un recurso existente.

Ejemplo:

```python
requests.patch(url, json=datos)
```

### Diferencia principal

- PUT → Reemplaza todo el recurso.
- PATCH → Modifica solo algunos campos.

### Buenas prácticas

Después de realizar un PUT o PATCH:

1. Verificar `status_code`.
2. Obtener la respuesta con `json()`.
3. Revisar los datos devueltos por la API.

### Idea clave

Si cambia todo el recurso, usar PUT. Si solo cambia una parte, usar PATCH.

BACKEND
│
├── Internet
├── HTTP
│   ├── GET
│   ├── POST
│   ├── PUT
│   ├── PATCH
│   └── DELETE
│
├── APIs REST
│   ├── Recursos
│   ├── GET → Consultar
│   ├── POST → Crear
│   ├── PUT → Reemplazar
│   └── PATCH → Modificar parcialmente
│
├── JSON
│
├── Python
│   └── requests
│       ├── get()
│       ├── post()
│       ├── put()
│       ├── patch()
│       └── delete()
│
└── Git

## APIs REST (Parte 4)

### Método DELETE

Se utiliza para eliminar un recurso existente.

Ejemplo:

```python
requests.delete(url)
```

### Códigos HTTP frecuentes

- 200 OK → Eliminación correcta con respuesta.
- 204 No Content → Eliminación correcta sin contenido.

### Buenas prácticas

1. Verificar `status_code`.
2. Aceptar como éxito los códigos 200 o 204.
3. Manejar correctamente un posible 404.

### CRUD completo

- POST → Crear.
- GET → Consultar.
- PUT / PATCH → Actualizar.
- DELETE → Eliminar.

BACKEND
│
├── Internet
├── HTTP
│   ├── GET
│   ├── POST
│   ├── PUT
│   ├── PATCH
│   └── DELETE
│
├── APIs REST
│   ├── CRUD
│   │   ├── Create → POST
│   │   ├── Read → GET
│   │   ├── Update → PUT / PATCH
│   │   └── Delete → DELETE
│   ├── Recursos
│   └── URLs
│
├── JSON
│
├── Python
│   └── requests
│       ├── get()
│       ├── post()
│       ├── put()
│       ├── patch()
│       └── delete()
│
└── Git

## APIs REST (Parte 5)

### CRUD

CRUD representa las cuatro operaciones básicas sobre un recurso:

- Create → POST
- Read → GET
- Update → PUT / PATCH
- Delete → DELETE

### Filosofía REST

- La URL representa el recurso.
- El método HTTP representa la acción.

### Flujo de trabajo

1. Identificar el recurso.
2. Elegir el método HTTP adecuado.
3. Enviar la petición.
4. Verificar `status_code`.
5. Procesar la respuesta.

### Idea clave

Antes de pensar en el código, un desarrollador backend piensa en el recurso y en la operación REST que debe realizar.