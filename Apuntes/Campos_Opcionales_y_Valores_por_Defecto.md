# Día 52 - Campos Opcionales y Valores por Defecto

## Objetivo

Comprender cómo diseñar modelos más flexibles utilizando campos opcionales (`Optional`) y valores por defecto, permitiendo que una API reciba únicamente la información necesaria sin perder consistencia.

---

# Conceptos fundamentales

## Campo obligatorio

Es un atributo que siempre debe ser enviado por el cliente.

Si no se envía, FastAPI responderá con:

```
422 Unprocessable Entity
```

Ejemplo:

```python
nombre: str
```

---

## Campo opcional

Es un atributo que puede o no enviarse.

Se define utilizando `Optional`.

```python
from typing import Optional

telefono: Optional[str] = None
```

Si el cliente no lo envía, el valor será:

```python
None
```

---

## Valor por defecto

Es un valor que FastAPI asigna automáticamente cuando el cliente no lo envía.

Ejemplo:

```python
activo: bool = True
```

Si el cliente omite el campo:

```json
{
    "nombre":"Ricardo"
}
```

FastAPI crea internamente:

```json
{
    "nombre":"Ricardo",
    "activo":true
}
```

---

# Sintaxis

```python
from typing import Optional
from pydantic import BaseModel, Field

class Usuario(BaseModel):
    nombre: str = Field(min_length=3)
    edad: int = Field(ge=18)
    ciudad: str
    telefono: Optional[str] = None
    activo: bool = True
```

---

# Explicación

El modelo diferencia tres tipos de atributos:

- Obligatorios.
- Opcionales.
- Valores automáticos.

Esto permite construir APIs más flexibles y cercanas a situaciones reales.

---

# Flujo de funcionamiento

Cliente

↓

Request Body

↓

FastAPI

↓

Pydantic

↓

Validación

↓

Si todo es correcto

↓

Se ejecuta la función

↓

Response

---

# Casos de uso

Campos obligatorios:

- Nombre
- Documento de identidad
- Contraseña

Campos opcionales:

- Teléfono
- Dirección
- Fotografía
- Empresa

Valores por defecto:

- Activo = True
- Fecha de creación
- Estado inicial
- Rol por defecto

---

# None vs Cadena vacía

```python
None
```

Significa:

No existe un valor.

Mientras que:

```python
""
```

Significa:

Existe un valor, pero es una cadena vacía.

---

# Errores comunes

❌ Pensar que `Optional` elimina todas las validaciones.

❌ Confundir `None` con `""`.

❌ Hacer todos los campos obligatorios.

❌ Hacer todos los campos opcionales.

---

# Buenas prácticas

- Hacer obligatorios únicamente los datos realmente necesarios.
- Utilizar valores por defecto cuando el sistema pueda decidirlos.
- Utilizar `Optional` cuando el negocio permita completar la información posteriormente.
- Diseñar modelos pensando en la experiencia del usuario.

---

# Relación con conocimientos anteriores

Este tema se relaciona con:

- HTTP → Request Body.
- JSON → Estructura de los datos enviados.
- Pydantic → Modelado y validación.
- Field() → Restricciones adicionales.
- Swagger → Pruebas de los modelos.

---

# Relación con el Proyecto 1

Nuestro modelo evolucionó desde:

```python
class Usuario(BaseModel):
    nombre: str
    edad: int
```

Hasta:

```python
class Usuario(BaseModel):
    nombre: str = Field(min_length=3)
    edad: int = Field(ge=18)
    ciudad: str
    telefono: Optional[str] = None
    activo: bool = True
```

Ahora la API es más flexible y representa mejor situaciones reales.

---

# Práctica realizada

Se realizaron pruebas utilizando Swagger.

Resultados obtenidos:

| Prueba | Resultado |
|----------|-----------|
| Todos los campos enviados | 200 OK |
| Sin teléfono | 200 OK |
| Sin activo | 200 OK |
| Sin teléfono y activo | 200 OK |
| Sin nombre | 422 Unprocessable Entity |

Estas pruebas confirmaron el funcionamiento de los campos obligatorios, opcionales y los valores por defecto.

---

# Preguntas de repaso

1. ¿Qué diferencia existe entre un campo obligatorio y uno opcional?
2. ¿Qué significa `Optional[str] = None`?
3. ¿Qué diferencia existe entre `None` y una cadena vacía?
4. ¿Cuándo conviene utilizar un valor por defecto?
5. ¿Qué ocurre si falta un campo obligatorio?
6. ¿Qué código HTTP responde FastAPI?
7. ¿Qué herramienta utilizamos para probar estas validaciones?
8. ¿Por qué no todos los campos deberían ser obligatorios?

---

# Nuestro mapa continúa creciendo

BACKEND
│
├── Internet
│
├── HTTP
│   ├── Request
│   ├── Response
│   ├── Headers
│   ├── Body
│   └── Status Codes
│
├── JSON
│
├── APIs REST
│   ├── Path Parameters
│   ├── Query Parameters
│   └── Request Body
│
├── FastAPI
│   ├── Rutas
│   ├── GET
│   ├── POST
│   ├── Path Parameters
│   ├── Query Parameters
│   ├── BaseModel
│   ├── Field()
│   ├── Optional
│   ├── Valores por defecto
│   └── Swagger
│
├── Programación Orientada a Objetos
│
└── Git

---

# Resumen

En este tema aprendimos a diferenciar entre campos obligatorios, campos opcionales y valores por defecto.

Utilizando `Optional` y valores predeterminados, FastAPI permite construir modelos más flexibles y adaptados a las necesidades del negocio.

Las pruebas realizadas en Swagger confirmaron que:

- Los campos obligatorios generan un error 422 cuando faltan.
- Los campos opcionales pueden omitirse sin afectar la ejecución.
- Los valores por defecto son asignados automáticamente por FastAPI.