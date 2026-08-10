# Día 69 — DELETE con SQLAlchemy

## Objetivo

Implementar la eliminación de registros utilizando FastAPI y SQLAlchemy.

---

## 1. DELETE

DELETE se utiliza para eliminar un recurso.

Endpoint:

DELETE /usuarios/{usuario_id}

---

## 2. Buscar antes de eliminar

Primero buscamos el usuario:

```python
usuario = db.query(Usuario).filter(
    Usuario.id == usuario_id
).first()

.first() devuelve:

El objeto Usuario si existe.
None si no existe.
3. Manejo de usuario inexistente
if usuario is None:
    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )

Si el usuario no existe, se responde:

404 Not Found

No se intenta ejecutar delete() sobre un objeto inexistente.

4. Eliminar
db.delete(usuario)

delete() prepara la eliminación del objeto dentro de la sesión.

La eliminación todavía no queda confirmada definitivamente.

5. Confirmar la eliminación
db.commit()

commit() confirma y persiste la eliminación en la base de datos.

6. ¿Por qué no usamos refresh()?

Después de:

db.delete(usuario)
db.commit()

el registro ya no existe en la base de datos.

Por esta razón no tiene sentido utilizar refresh() sobre el usuario eliminado.

7. Endpoint completo
@app.delete("/usuarios/{usuario_id}")
def eliminar_usuario(
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

    db.delete(usuario)
    db.commit()

    return {
        "mensaje": "Usuario eliminado correctamente"
    }
8. Pruebas realizadas
Eliminar usuario existente

Se eliminó:

ID 4 → Johana

La respuesta fue exitosa y posteriormente GET /usuarios confirmó que el usuario ya no aparecía.

Eliminar usuario inexistente

Se probó:

DELETE /usuarios/999

Resultado:

404 Not Found

9. Flujo completo

DELETE
↓
query()
↓
filter()
↓
first()
↓
¿Existe?
↓
NO → 404 Not Found
↓
SÍ → delete()
↓
commit()
↓
respuesta

10. CRUD aprendido hasta el momento
Operación	HTTP	SQLAlchemy
Crear	POST	add() + commit()
Leer todos	GET	query().all()
Leer uno	GET	query().first()
Actualizar parcialmente	PATCH	modificar + commit()
Eliminar	DELETE	delete() + commit()
Conceptos clave
DELETE
db.delete()
commit()
first()
None
HTTPException
404 Not Found
Eliminación persistente
Diferencia entre preparar y confirmar una operación