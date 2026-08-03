# Día 55 – Response Models en FastAPI

## Objetivo

Aprender a controlar la información que una API devuelve al cliente utilizando `response_model`, separando los modelos de entrada (Request) y salida (Response) para mejorar la seguridad, organización y mantenimiento de la aplicación.

---

# ¿Qué es un Response Model?

Un **Response Model** es un modelo de Pydantic que define la estructura de los datos que FastAPI enviará como respuesta al cliente.

Se declara mediante el parámetro:

```python
response_model=MiModelo
```

Gracias a este mecanismo, FastAPI filtra automáticamente la información antes de enviarla.

---

# ¿Por qué utilizar Response Models?

En muchas ocasiones una API recibe más información de la que debe devolver.

Por ejemplo, al crear un usuario es necesario recibir la contraseña, pero nunca debería enviarse nuevamente al cliente.

Esto permite:

- Proteger información sensible.
- Separar los modelos de entrada y salida.
- Mantener una API más segura.
- Facilitar el mantenimiento del código.

---

# Modelo de entrada

```python
class Usuario(BaseModel):
    nombre: str
    correo: str
    password: str
```

Este modelo representa la información que el cliente envía para crear un usuario.

---

# Modelo de salida

```python
class UsuarioRespuesta(BaseModel):
    nombre: str
    correo: str
```

Este modelo define únicamente la información que la API devolverá al cliente.

---

# Uso de response_model

```python
@app.post("/usuarios", response_model=UsuarioRespuesta)
def crear_usuario(usuario: Usuario):
    return usuario
```

Aunque la función retorne el objeto completo, FastAPI enviará únicamente los campos definidos en `UsuarioRespuesta`.

---

# Flujo de trabajo

Cliente

↓

Request Body (JSON)

↓

FastAPI recibe la petición

↓

Pydantic crea el modelo de entrada

↓

Valida los datos

↓

Se ejecuta la función

↓

FastAPI aplica `response_model`

↓

Filtra los campos permitidos

↓

Genera la respuesta HTTP

↓

200 OK

---

# Idea clave

Los modelos de entrada y salida pueden ser diferentes.

La información que la API necesita recibir no siempre es la misma que debe mostrar al cliente.

---

# Ejemplo práctico

Request

```json
{
    "nombre":"Ricardo",
    "correo":"ricardo@email.com",
    "password":"123456"
}
```

Response

```json
{
    "nombre":"Ricardo",
    "correo":"ricardo@email.com"
}
```

La contraseña nunca aparece en la respuesta.

---

# Ventajas

- Mayor seguridad.
- Menor exposición de datos sensibles.
- Código más organizado.
- Modelos reutilizables.
- APIs profesionales.
- Documentación automática más clara en Swagger.

---

# Relación con los temas anteriores

Hasta este momento conocemos:

- Path Parameters
- Query Parameters
- Request Body
- BaseModel
- Field
- Optional
- Modelos anidados
- Listas de modelos
- Response Models

Observamos que FastAPI valida tanto la información que entra a la API como la información que sale de ella.

---

# Mapa del proceso

Cliente

↓

Request

↓

Validación de entrada

↓

Función

↓

Validación de salida (Response Model)

↓

Cliente

---

# Conceptos clave

- Request Model
- Response Model
- Seguridad
- Pydantic
- Validación
- Filtrado de datos
- Documentación automática

---

# Conclusión

Un `response_model` permite controlar exactamente qué información recibe el cliente.

Es una práctica fundamental en el desarrollo de APIs profesionales, ya que protege datos sensibles, mejora la organización del código y facilita el mantenimiento de la aplicación.