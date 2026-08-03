# Día 53 - Modelos Anidados (Nested Models)

## Objetivo

Comprender cómo construir modelos Pydantic que contengan otros modelos, permitiendo representar estructuras de datos complejas de forma organizada, reutilizable y fácil de mantener.

---

# ¿Qué es un modelo anidado?

Un modelo anidado es un modelo Pydantic que contiene otro modelo Pydantic como uno de sus atributos.

En lugar de almacenar toda la información en una única clase, podemos dividirla en varios modelos relacionados entre sí.

---

# ¿Por qué utilizar modelos anidados?

Cuando una aplicación comienza a crecer, un solo modelo puede contener demasiados atributos.

Por ejemplo, un usuario puede tener:

- Datos personales.
- Dirección.
- Información de contacto.
- Preferencias.

Agrupar toda esta información en una única clase genera código difícil de leer y mantener.

Los modelos anidados permiten organizar la información de forma lógica.

---

# Ejemplo

## Modelo Dirección

```python
from pydantic import BaseModel

class Direccion(BaseModel):
    calle: str
    numero: str
    ciudad: str
```

---

## Modelo Usuario

```python
from typing import Optional
from pydantic import BaseModel, Field

class Usuario(BaseModel):
    nombre: str = Field(min_length=3, max_length=50)
    edad: int = Field(ge=18, le=120)
    telefono: Optional[str] = None
    activo: bool = True
    direccion: Direccion
```

En este caso, el atributo `direccion` no es un dato simple, sino otro modelo Pydantic.

---

# JSON esperado

```json
{
    "nombre": "Ricardo",
    "edad": 45,
    "telefono": "3101234567",
    "activo": true,
    "direccion": {
        "calle": "Carrera 10",
        "numero": "25-18",
        "ciudad": "Paipa"
    }
}
```

---

# ¿Qué hace FastAPI?

Cuando recibe la petición:

1. Recibe el JSON.
2. Pydantic crea el modelo `Direccion`.
3. Valida todos sus campos.
4. Crea el modelo `Usuario`.
5. Asocia el objeto `Direccion` al atributo `direccion`.
6. Si toda la validación es correcta, ejecuta la función.
7. Genera la respuesta HTTP.

---

# Flujo de funcionamiento

Cliente

↓

Request Body (JSON)

↓

FastAPI recibe la petición

↓

Pydantic crea el modelo Dirección

↓

Valida los campos de Dirección

↓

Pydantic crea el modelo Usuario

↓

Valida los campos de Usuario

↓

Modelo completo válido

↓

Se ejecuta la función

↓

Response

↓

200 OK

---

# Validaciones

Las validaciones se realizan tanto en el modelo principal como en los modelos anidados.

Ejemplo:

```python
class Direccion(BaseModel):
    calle: str
    numero: str
    ciudad: str
```

Si falta alguno de estos campos:

- calle
- numero
- ciudad

FastAPI responderá:

```
422 Unprocessable Entity
```

La función no será ejecutada.

---

# Ventajas

- Código más organizado.
- Modelos pequeños y fáciles de mantener.
- Reutilización de modelos.
- Mayor claridad.
- Facilita el crecimiento del proyecto.
- Representa mejor situaciones reales.

---

# Relación con Programación Orientada a Objetos

Este concepto aplica el principio de composición visto en Programación Orientada a Objetos.

Un objeto puede contener otros objetos.

Ejemplo:

```
Automóvil
│
├── Motor
├── Transmisión
└── Llantas
```

De forma similar:

```
Usuario
│
├── nombre
├── edad
└── Dirección
        │
        ├── calle
        ├── numero
        └── ciudad
```

---

# Casos reales

## Universidad

```
Estudiante
│
├── nombre
├── código
└── Programa Académico
        │
        ├── nombre
        ├── facultad
        └── duración
```

---

## Tienda virtual

```
Pedido
│
├── Cliente
├── Dirección de envío
└── Productos
```

---

## Clínica

```
Paciente
│
├── Datos personales
├── Dirección
└── Contacto
```

---

# Errores comunes

❌ Pensar que un modelo anidado recibe una cadena de texto.

❌ Confundir un objeto JSON con un modelo Pydantic.

❌ Olvidar que las validaciones también se aplican a los modelos internos.

❌ Crear modelos demasiado grandes cuando podrían dividirse.

---

# Buenas prácticas

- Crear un modelo para cada entidad del negocio.
- Reutilizar modelos cuando sea posible.
- Mantener cada modelo con una única responsabilidad.
- Agrupar la información relacionada.
- Evitar clases excesivamente grandes.

---

# Relación con conocimientos anteriores

Este tema integra conceptos estudiados previamente:

- Programación Orientada a Objetos.
- BaseModel.
- Field().
- Optional.
- Request Body.
- JSON.
- Validaciones.
- Swagger.

---

# Relación con el Proyecto 1

El modelo evolucionó de:

```python
class Usuario(BaseModel):
    nombre: str
   edad: int
```

A:

```python
class Direccion(BaseModel):
    calle: str
    numero: str
    ciudad: str

class Usuario(BaseModel):
    nombre: str
    edad: int
    telefono: Optional[str] = None
    activo: bool = True
    direccion: Direccion
```

El proyecto comienza a representar relaciones reales entre entidades.

---

# Práctica realizada

Se realizaron pruebas en Swagger.

Resultados:

| Prueba | Resultado |
|---------|-----------|
| Todos los campos enviados | 200 OK |
| Falta `numero` en Dirección | 422 Unprocessable Entity |
| Falta `direccion` | 422 Unprocessable Entity |
| `direccion` enviada como cadena | 422 Unprocessable Entity |

Las pruebas confirmaron que FastAPI valida tanto el modelo principal como los modelos anidados.

---

# Preguntas de repaso

1. ¿Qué es un modelo anidado?
2. ¿Qué ventaja tiene dividir un modelo grande en varios modelos?
3. ¿Qué diferencia existe entre un objeto JSON y un modelo Pydantic?
4. ¿Qué ocurre si falta un campo obligatorio dentro de un modelo anidado?
5. ¿Por qué esta técnica facilita el mantenimiento del código?
6. ¿Qué relación tiene este tema con la Programación Orientada a Objetos?

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
│   ├── Modelos anidados
│   └── Swagger
│
├── Programación Orientada a Objetos
│
└── Git

---

# Resumen

Los modelos anidados permiten construir estructuras de datos complejas utilizando modelos Pydantic dentro de otros modelos.

Esta técnica mejora la organización del código, facilita la reutilización de componentes, reduce el tamaño de las clases y representa de forma más natural las relaciones existentes en aplicaciones reales.

FastAPI valida automáticamente tanto el modelo principal como los modelos internos antes de ejecutar la función, garantizando la consistencia de los datos recibidos.