# Día 66 — Consultas con SQLAlchemy

## Objetivo

Realizar consultas a la base de datos utilizando SQLAlchemy y
manejar correctamente el caso en que un registro no exista.

---

## 1. Obtener todos los usuarios

Para obtener todos los registros:

```python
usuarios = db.query(Usuario).all()

.all() devuelve una lista de objetos Usuario.

Ejemplo conceptual:

[
    Usuario(...),
    Usuario(...),
    Usuario(...)
]
2. Obtener un usuario específico

Para buscar un usuario por su ID:

usuario = db.query(Usuario).filter(
    Usuario.id == usuario_id
).first()

usuario_id corresponde al Path Parameter recibido por el endpoint.

Ejemplo:

GET /usuarios/4

FastAPI recibe:

usuario_id = 4

SQLAlchemy busca:

Usuario.id == 4
3. .all() vs .first()
.all()

Devuelve una lista:

usuarios = db.query(Usuario).all()

Resultado conceptual:

[
    Usuario(...),
    Usuario(...),
    Usuario(...)
]
.first()

Devuelve el primer objeto encontrado:

usuario = db.query(Usuario).filter(
    Usuario.id == 4
).first()

Si existe:

Usuario(...)

Si no existe:

None
4. Manejo de usuario inexistente

No es correcto devolver simplemente None cuando el recurso
solicitado no existe.

Se utiliza HTTPException:

from fastapi import HTTPException

Y:

if usuario is None:
    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )

De esta manera:

Usuario existe
    ↓
return usuario
    ↓
200 OK

Mientras que:

Usuario no existe
    ↓
usuario = None
    ↓
HTTPException
    ↓
404 Not Found
5. Endpoint completo
@app.get("/usuarios/{usuario_id}")
def obtener_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return usuario
6. Endpoints trabajados
Crear usuario
POST /usuarios

Crea un nuevo usuario.

Obtener todos
GET /usuarios

Devuelve todos los usuarios.

Obtener uno
GET /usuarios/{usuario_id}

Devuelve un usuario específico.

Si no existe:

404 Not Found
7. Flujo general
Cliente
   ↓
FastAPI
   ↓
Endpoint
   ↓
Depends()
   ↓
Session
   ↓
SQLAlchemy
   ↓
Base de datos
   ↓
Resultado
   ↓
Respuesta HTTP
Conceptos aprendidos
query()
filter()
.all()
.first()
None
HTTPException
404 Not Found
Path Parameters
Consultas a SQLAlchemy
Manejo de recursos inexistentes
Reflexión técnica

El método .all() permite recuperar múltiples registros,
mientras que .first() permite obtener un único resultado.

Cuando .first() no encuentra coincidencias devuelve None.
La aplicación debe detectar esta situación y responder con un
código HTTP apropiado, normalmente 404 Not Found.

Esto permite que nuestra API comunique correctamente al cliente
qué ocurrió con la solicitud.