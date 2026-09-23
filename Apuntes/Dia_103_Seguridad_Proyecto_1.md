Día 103 — Seguridad del Proyecto 1

Objetivo

Integrar y auditar la seguridad del Proyecto 1: autenticación, autorización, protección de datos sensibles, actualización segura de usuarios, creación autenticada de pedidos y verificación mediante tests.

1. Auditoría del registro de usuarios

Se detectó que correo necesitaba protección contra duplicados en dos niveles:

Modelo SQLAlchemy: correo = Column(String, unique=True)

PostgreSQL: restricción UNIQUE real sobre usuarios.correo

Migración Alembic creada y aplicada:

Revisión: 37e09c3bcc17

Restricción resultante: usuarios_correo_key

Además, POST /usuarios realiza una comprobación previa y responde 409 Conflict cuando el correo ya está registrado.

2. Endurecimiento de get_current_user()

La dependencia quedó preparada para manejar JWT inválidos, expirados o con sub incorrecto:

try:
    payload = decode_access_token(token)
    usuario_id = int(payload["sub"])

except (jwt.PyJWTError, KeyError, ValueError, TypeError):
    raise HTTPException(
        status_code=401,
        detail="Token inválido o expirado"
    )

Después se consulta el usuario real en PostgreSQL. Si no existe, se responde 401.

3. Autenticación vs autorización comprobadas

Se verificó el orden:

Sin autenticación válida → 401 Unauthorized

Autenticado pero sin permisos → 403 Forbidden

Autenticado y autorizado, pero recurso inexistente → 404 Not Found

Ejemplo comprobado:

Usuario normal intentando eliminar/modificar otro usuario → 403

Administrador consultando un recurso inexistente después de superar autorización → 404

4. Error real encontrado: PATCH duplicado

Existían dos definiciones:

@app.patch("/usuarios/{usuario_id}")

FastAPI avisaba:

Duplicate Operation ID actualizar_usuario_usuarios__usuario_id__patch

Una versión tenía autorización y otra contenía la actualización real. Esto provocaba que OpenAPI/Swagger no asociara correctamente HTTPBearer al PATCH esperado.

Se fusionaron ambas responsabilidades en un único endpoint.

Lección

Cuando Swagger, OpenAPI y el código parecen contradecirse, revisar rutas duplicadas y los avisos de Uvicorn antes de modificar autenticación.

5. Política del PATCH de usuarios

Regla implementada:

Usuario normal → puede modificar su propia cuenta.

Usuario normal → no puede modificar otra cuenta (403).

Administrador → puede modificar otras cuentas.

Condición:

if current_user.id != usuario_id and current_user.rol != "admin":
    raise HTTPException(
        status_code=403,
        detail="No tienes permisos para modificar este usuario"
    )

Pruebas:

Usuario 6 → PATCH usuario 7 → 403

Usuario 6 → PATCH usuario 6 → 200

6. Protección de la respuesta

El PATCH inicialmente devolvía directamente el objeto ORM y exponía:

password_hash

rol

Se agregó:

response_model=UsuarioResponse

La respuesta quedó limitada a datos públicos:

{
  "id": 6,
  "nombre": "Usuario Seguro",
  "correo": "seguro@test.com",
  "telefono": null,
  "ciudad": null
}

Concepto

Autorización controla quién puede ejecutar una operación.
response_model controla qué información puede salir de la API.

7. Cambio seguro de contraseña

UsuarioActualizar se amplió con:

password: str | None = None

La contraseña requiere tratamiento especial:

for campo, valor in datos_actualizados.items():
    if campo == "password":
        usuario.password_hash = hash_password(valor)
    else:
        setattr(usuario, campo, valor)

Nunca se almacena la contraseña en texto plano.

Pruebas funcionales:

PATCH con nueva contraseña → 200

Login con nueva contraseña → 200

Login con contraseña anterior → 401

Distinción importante

La contraseña no genera el JWT. La contraseña se verifica durante /login; después de un login correcto se genera un JWT independiente con identidad (sub) y expiración.

8. Correo duplicado durante PATCH

Al intentar actualizar un usuario con un correo ya utilizado, PostgreSQL protegió la integridad mediante UNIQUE, pero inicialmente la API devolvió 500.

Se agregó manejo de IntegrityError:

try:
    db.commit()

except IntegrityError:
    db.rollback()
    raise HTTPException(
        status_code=409,
        detail="Correo ya registrado"
    )

Resultado comprobado:

409 Conflict
"Correo ya registrado"

rollback() restaura el estado transaccional de la sesión después del commit() fallido.

9. Response models auditados

Se corrigieron endpoints que podían exponer password_hash o rol.

Se utilizaron:

UsuarioResponse

PedidoResponse

UsuarioConPedidosResponse

UsuarioPedidoResponse

PedidoDetalleResponse

En /usuarios/con-pedidos se comprobó además:

selectinload() decide cómo cargar las relaciones.

response_model decide qué exponer en la respuesta.

10. Seguridad de POST /pedidos

Antes:

cliente → producto + usuario_id

El cliente podía elegir arbitrariamente el propietario del pedido.

Después:

@app.post("/pedidos")
def crear_pedido(
    producto: str,
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    nuevo_pedido = Pedido(
        producto=producto,
        usuario_id=current_user.id
    )

Ahora el propietario se obtiene del JWT.

Prueba:

JWT usuario 6

Producto: Monitor

Resultado: 200

Pedido creado con usuario_id = 6

11. Recuperación de GET /usuarios/{usuario_id}

Los tests detectaron que durante la refactorización había desaparecido:

GET /usuarios/{usuario_id}

Esto producía 405 Method Not Allowed, porque la misma ruta existía para PATCH/DELETE pero no para GET.

Se restauró con:

@app.get(
    "/usuarios/{usuario_id}",
    response_model=UsuarioResponse
)

Así se recuperaron:

Usuario existente → 200

Usuario inexistente → 404

12. Testing después de integrar seguridad

Primera ejecución:

3 failed, 3 passed

La base bootcamp_backend_test conservaba una tabla antigua sin password_hash. Se confirmó nuevamente:

create_all() crea tablas faltantes, pero no migra automáticamente tablas existentes.

Se reconstruyó exclusivamente la base de testing con los modelos actuales.

Después quedaron fallos por UniqueViolation: los tests insertaban siempre:

test@correo.com

endpoint@test.com

y los datos permanecían entre ejecuciones.

Tras limpiar/reconstruir la base de testing:

6 passed

Deuda técnica consciente

Los tests pasan con una base limpia, pero todavía no están completamente aislados/repetibles porque dejan registros persistidos. El aislamiento mediante fixtures queda pendiente para una mejora posterior; no se profundizó para evitar desviarse del plan.

Resultado final del Día 103

Se integraron y comprobaron:

Hashing Argon2.

Login seguro.

JWT.

HTTPBearer.

get_current_user().

Roles user/admin.

401, 403, 404 y 409.

Restricción UNIQUE de correo.

rollback() ante conflicto.

Cambio seguro de contraseña.

response_model para evitar fugas.

PATCH con autorización propia/admin.

POST de pedidos ligado al usuario autenticado.

Depuración de endpoint duplicado.

Recuperación de endpoint perdido mediante tests.

Suite final: 6 tests aprobados con base de testing limpia.

Conceptos para entrevista

¿401 vs 403?
401: no se pudo autenticar correctamente al usuario.
403: está autenticado, pero no tiene permiso para esa acción.

¿Por qué no confiar en usuario_id enviado por el cliente al crear un pedido?
Porque permitiría intentar crear recursos a nombre de otro usuario. La identidad debe derivarse del usuario autenticado.

¿Por qué usar response_model aunque el endpoint esté protegido?
Porque autenticación/autorización y exposición de datos son problemas diferentes.

¿Por qué hacer rollback después de IntegrityError?
Porque una transacción fallida deja la sesión en estado de error hasta revertirla.

¿Por qué create_all() no sustituyó a Alembic?
Porque crea estructuras que faltan, pero no administra de forma segura la evolución de tablas existentes.

Estado

Día 103 completado.