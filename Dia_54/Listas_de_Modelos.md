# Día 54 - Listas de Modelos (List[Nested Models])

## Objetivo

Aprender a recibir listas de objetos mediante modelos Pydantic, comprendiendo cómo FastAPI valida cada elemento de la colección y por qué este mecanismo representa situaciones reales en una aplicación backend.

---

# ¿Qué es una lista de modelos?

Hasta el momento habíamos trabajado con modelos simples y modelos anidados.

Ahora un modelo puede contener una colección de otros modelos utilizando `List[]`.

Ejemplo:

```python
from typing import List

class Pedido(BaseModel):
    cliente: str
    productos: List[Producto]
```

Esto significa que un pedido puede contener varios productos.

---

# ¿Por qué utilizar listas?

Las listas no existen porque FastAPI las necesite.

Existen porque representan situaciones del mundo real.

Ejemplos:

- Un pedido contiene varios productos.
- Una factura contiene varios artículos.
- Una receta médica contiene varios medicamentos.
- Un estudiante cursa varias materias.
- Un usuario puede tener varias direcciones.

Sin listas sería necesario crear múltiples peticiones para representar un único proceso de negocio.

---

# Ejemplo

## Modelo Producto

```python
class Producto(BaseModel):
    nombre: str
    precio: float = Field(gt=0)
    cantidad: int = Field(gt=0)
```

## Modelo Pedido

```python
from typing import List

class Pedido(BaseModel):
    cliente: str
    productos: List[Producto]
```

---

# JSON esperado

```json
{
    "cliente": "Ricardo",
    "productos": [
        {
            "nombre": "Teclado",
            "precio": 120000,
            "cantidad": 1
        },
        {
            "nombre": "Mouse",
            "precio": 60000,
            "cantidad": 2
        }
    ]
}
```

Observaciones:

- `productos` es una lista (`[]`).
- Cada elemento de la lista es un objeto (`{}`).

---

# ¿Qué hace FastAPI?

Cuando recibe la petición:

1. Recibe el Request Body.
2. Pydantic crea el modelo `Pedido`.
3. Recorre la lista `productos`.
4. Convierte cada elemento en un objeto `Producto`.
5. Valida cada producto.
6. Si todos son válidos, ejecuta la función.
7. Devuelve la respuesta HTTP.

---

# Flujo de funcionamiento

Cliente

↓

Request Body (JSON)

↓

FastAPI recibe la petición

↓

Pydantic crea el modelo Pedido

↓

Recorre la lista de productos

↓

Crea un objeto Producto por cada elemento

↓

Valida todos los productos

↓

Todos válidos

↓

Ejecuta la función

↓

Response

↓

200 OK

---

# Validaciones

Cada objeto de la lista se valida individualmente.

Si un único producto no cumple las reglas, toda la petición será rechazada.

Ejemplo:

```json
{
    "nombre": "Mouse",
    "precio": -5000,
    "cantidad": 2
}
```

Resultado:

```
422 Unprocessable Entity
```

La función no será ejecutada.

---

# Una lista vacía

Durante las pruebas en Swagger observamos un comportamiento importante.

El siguiente JSON:

```json
{
    "cliente": "Ricardo",
    "productos": []
}
```

fue aceptado con:

```
200 OK
```

¿Por qué?

Porque únicamente se indicó que `productos` debía ser una lista.

Una lista vacía sigue siendo una lista válida.

Más adelante aprenderemos cómo exigir que la lista contenga al menos un elemento.

---

# Casos reales

## Tienda virtual

```
Pedido
│
├── Cliente
└── Productos
      ├── Producto 1
      ├── Producto 2
      ├── Producto 3
      └── Producto n
```

---

## Clínica

```
Receta
│
├── Paciente
└── Medicamentos
      ├── Medicamento 1
      ├── Medicamento 2
      └── Medicamento n
```

---

## Universidad

```
Estudiante
│
├── Datos personales
└── Materias
      ├── Matemáticas
      ├── Física
      ├── Programación
      └── Inglés
```

---

# Entidades

Una entidad representa uno de los elementos principales del negocio.

Ejemplos:

Tienda:

- Cliente
- Producto
- Pedido
- Factura

Clínica:

- Paciente
- Médico
- Medicamento
- Receta

Universidad:

- Estudiante
- Profesor
- Materia
- Programa académico

Más adelante, estas entidades se convertirán en tablas de la base de datos.

---

# Buenas prácticas

- Utilizar listas cuando una entidad pueda contener múltiples elementos.
- Validar cada objeto de la colección.
- Mantener modelos pequeños y reutilizables.
- Representar la estructura real del negocio.

---

# Errores comunes

❌ Enviar cadenas cuando se esperan objetos.

❌ Pensar que una lista vacía es inválida.

❌ Creer que FastAPI valida únicamente el primer elemento.

❌ Mezclar diferentes tipos de datos en la misma colección.

---

# Relación con temas anteriores

Este tema integra conocimientos de:

- BaseModel
- Field()
- Optional
- Modelos anidados
- Request Body
- JSON
- Swagger
- Listas de Python

---

# Relación con el Proyecto 1

El proyecto evoluciona desde recibir un único objeto hasta manejar colecciones de objetos.

Esto acerca la API a escenarios reales como pedidos, recetas médicas, facturas o inventarios.

---

# Práctica realizada

Se realizaron pruebas en Swagger.

Resultados:

| Prueba | Resultado |
|---------|-----------|
| Dos productos válidos | 200 OK |
| Falta un campo obligatorio | 422 Unprocessable Entity |
| Lista vacía | 200 OK |
| Lista con cadenas en lugar de objetos | 422 Unprocessable Entity |

---

# Preguntas de repaso

1. ¿Qué representa `List[Producto]`?
2. ¿Por qué las listas son importantes en una API?
3. ¿Qué ocurre si un solo elemento de la lista es inválido?
4. ¿Por qué una lista vacía fue aceptada?
5. ¿Qué es una entidad?
6. ¿Qué relación existe entre listas y situaciones del mundo real?

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
│   ├── BaseModel
│   ├── Field()
│   ├── Optional
│   ├── Modelos anidados
│   ├── Listas de modelos
│   └── Swagger
│
├── Programación Orientada a Objetos
│
└── Git

---

# Resumen

Las listas de modelos permiten representar colecciones de objetos dentro de una API.

FastAPI convierte cada elemento de la lista en un modelo Pydantic, valida todos los objetos y únicamente ejecuta la función cuando toda la colección cumple las reglas establecidas.

Su principal ventaja es representar correctamente situaciones reales del negocio, como pedidos con varios productos, recetas con varios medicamentos o facturas con múltiples artículos.