# Día 65 – CRUD (Create) – Insertar registros con SQLAlchemy

## Objetivo

Aprender a insertar registros en una base de datos utilizando SQLAlchemy ORM desde un endpoint de FastAPI.

---

## Conceptos principales

### Crear un objeto ORM

Un modelo SQLAlchemy representa una tabla y una instancia del modelo representa un registro.

```python
nuevo_usuario = Usuario(
    nombre="Ricardo",
    correo="ricardo@email.com"
)

En este momento el objeto existe solamente en memoria.

db.add()

Agrega el objeto a la Session para que SQLAlchemy lo tenga en cuenta dentro de la transacción.

db.add(nuevo_usuario)
db.commit()

Confirma los cambios y realiza el guardado definitivo en la base de datos.

db.commit()
db.refresh()

Actualiza el objeto en Python con el estado actual de la base de datos.

db.refresh(nuevo_usuario)

Esto permite disponer, entre otros datos, del id generado por la base de datos.

Flujo de creación
Cliente
   ↓
POST /usuarios
   ↓
FastAPI
   ↓
Crear objeto Usuario
   ↓
db.add()
   ↓
db.commit()
   ↓
db.refresh()
   ↓
Base de datos
   ↓
Respuesta
Endpoint para crear usuarios
@app.post("/usuarios")
def crear_usuario(
    nombre: str,
    correo: str,
    db: Session = Depends(get_db)
):
    nuevo_usuario = Usuario(
        nombre=nombre,
        correo=correo
    )

    db.add(nuevo_usuario)

    db.commit()

    db.refresh(nuevo_usuario)

    return nuevo_usuario
Endpoint para consultar usuarios

También se creó un endpoint GET para visualizar los registros almacenados.

@app.get("/usuarios")
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return usuarios

Esto permite consultar los usuarios creados desde Swagger.

CRUD

En este día comenzamos formalmente el CRUD:

C → Create  → POST
R → Read    → GET
U → Update  → PUT/PATCH
D → Delete  → DELETE

En el Día 65 trabajamos:

Create → POST /usuarios
Read → GET /usuarios
ID del registro

El id identifica de manera única un registro.

Ejemplo:

id    nombre
--------------
1     Ricardo
2     Ana
3     Carlos
4     Pedro

Aunque en nuestro ejemplo los IDs coinciden con el orden de creación, conceptualmente el id no representa simplemente la posición de la fila.

Si se elimina el registro id=2, los registros 3 y 4 siguen conservando sus identificadores.

Diferencia entre las operaciones
Usuario(...)
    ↓
Crea un objeto en memoria

db.add(usuario)
    ↓
Prepara/incorpora el objeto a la Session

db.commit()
    ↓
Confirma y guarda el cambio

db.refresh(usuario)
    ↓
Actualiza el objeto con los datos actuales de la BD
Reflexión técnica
add() prepara el objeto para ser guardado.
commit() confirma y ejecuta el cambio.
refresh() actualiza el objeto con los valores actuales de la base de datos.
El id identifica al registro y no debe confundirse con la posición de una fila.
Resultado del día

Se consiguió realizar el primer flujo real de persistencia:

FastAPI
   ↓
SQLAlchemy
   ↓
SQLite
   ↓
Registro persistente

Se verificó mediante Swagger la creación de varios usuarios y el incremento automático de sus IDs.

Conexión con los temas anteriores

Este día integra conceptos estudiados anteriormente:

FastAPI
Routers y endpoints
Depends()
Services
SQLAlchemy
Session
Modelos ORM
SQLite
HTTP POST
HTTP GET
CRUD