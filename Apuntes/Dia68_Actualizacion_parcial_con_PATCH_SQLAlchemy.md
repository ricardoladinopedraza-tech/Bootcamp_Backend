## Objetivo

Implementar actualización parcial de usuarios utilizando PATCH, FastAPI, Pydantic y SQLAlchemy.

---

## 1. PATCH

PATCH se utiliza para realizar modificaciones parciales sobre un recurso.

Ejemplo:

```json
{
    "correo": "nuevo@correo.com"
}

No es necesario enviar todos los campos del usuario.

2. Modelo para actualización
class UsuarioActualizar(BaseModel):
    nombre: str | None = None
    correo: str | None = None

Los campos son opcionales porque un PATCH puede modificar solamente algunos atributos.

3. Buscar el usuario
usuario = db.query(Usuario).filter(
    Usuario.id == usuario_id
).first()

.first() devuelve:

Un objeto Usuario si existe.
None si no existe.

Si no existe:

if usuario is None:
    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )
4. model_dump()

Convierte el modelo Pydantic en un diccionario.

datos.model_dump()

Puede incluir campos que no fueron enviados y que tienen None como valor por defecto.

5. exclude_unset=True
datos.model_dump(exclude_unset=True)

Permite obtener solamente los campos que realmente fueron enviados por el cliente.

Ejemplo:

Request:

{
    "correo": "nuevo@correo.com"
}

Resultado:

{
    "correo": "nuevo@correo.com"
}

Esto es especialmente útil para PATCH.

6. setattr()

Permite modificar dinámicamente un atributo.

for campo, valor in datos_actualizados.items():
    setattr(usuario, campo, valor)

Por ejemplo:

setattr(usuario, "nombre", "Carlos")

equivale conceptualmente a:

usuario.nombre = "Carlos"
7. Confirmación y actualización

Después de modificar el objeto:

db.commit()

confirma y guarda definitivamente los cambios.

Después:

db.refresh(usuario)

actualiza el objeto Python con el estado actual de la base de datos.

8. Flujo completo
Cliente
   ↓
PATCH /usuarios/{usuario_id}
   ↓
Request Body
   ↓
Pydantic
   ↓
Buscar usuario
   ↓
404 si no existe
   ↓
model_dump(exclude_unset=True)
   ↓
setattr()
   ↓
commit()
   ↓
refresh()
   ↓
Response
9. PATCH vs PUT
PATCH

Actualización parcial.

{
    "correo": "nuevo@correo.com"
}

Solo se modifica el campo enviado.

PUT

Conceptualmente representa una actualización/reemplazo completo del recurso, por lo que normalmente se trabaja con la representación completa.

10. Pruebas realizadas
PATCH — modificar nombre

Request:

{
    "nombre": "Ricardo"
}

Resultado:

{
    "id": 3,
    "nombre": "Ricardo",
    "correo": "nuevo_correo@correo.com"
}

El correo permaneció intacto.

PATCH — modificar correo

Request:

{
    "correo": "ricardo@nuevo.com"
}

Resultado:

{
    "id": 3,
    "nombre": "Ricardo",
    "correo": "ricardo@nuevo.com"
}

El nombre permaneció intacto.

Usuario inexistente
PATCH /usuarios/999

Resultado:

404 Not Found
Conceptos clave aprendidos
PATCH
Actualización parcial
Campos opcionales con Pydantic
model_dump()
exclude_unset=True
setattr()
commit()
refresh()
HTTP 404
Diferencia conceptual entre PATCH y PUT