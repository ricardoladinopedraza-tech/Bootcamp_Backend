Día 102 — Roles y permisos (admin vs user)

Objetivo

Pasar de autenticación (¿quién eres?) a autorización (¿qué puedes hacer?).

JWT ausente/inválido → 401
JWT válido + permisos insuficientes → 403

Columna rol

Se agregó al modelo:

rol = Column(String, nullable=False, default="user")

default="user" asigna el rol normal cuando no se especifica; nullable=False impide NULL. El cliente no debe poder autoconcederse admin.

Migración Alembic

Como ya había usuarios, se evitó crear directamente una columna NOT NULL sin valores:

def upgrade() -> None:
    op.add_column('usuarios', sa.Column('rol', sa.String(), nullable=True))
    op.execute("UPDATE usuarios SET rol = 'user' WHERE rol IS NULL")
    op.alter_column('usuarios', 'rol', nullable=False)

downgrade() elimina rol. Migración ejecutada: e76e34cf8d6b → 56acf0546194. PostgreSQL confirmó rol=user para los usuarios existentes.

Registro y seguridad

El usuario 7 se creó sin enviar rol y PostgreSQL guardó rol=user, demostrando que el backend controla el valor por defecto.

Durante la práctica se detectó que GET /usuarios exponía password_hash. Se corrigió con:

@app.get("/usuarios", response_model=list[UsuarioResponse])

Como UsuarioResponse no contiene password_hash, FastAPI lo filtra de la respuesta pública.

Administrador de prueba

Se estableció:

id=6 → user
id=7 → admin

El cambio de rol modifica autorización, no identidad ni contraseña.

require_admin()

def require_admin(
    current_user: Usuario = Depends(get_current_user)
):
    if current_user.rol != "admin":
        raise HTTPException(
            status_code=403,
            detail="No tienes permisos suficientes"
        )
    return current_user

Cadena:

HTTPBearer
→ decode_access_token()
→ get_current_user()
→ Usuario desde PostgreSQL
→ require_admin()
→ endpoint

Casos:

sin JWT           → 401
JWT inválido       → 401
JWT válido + user  → 403
JWT válido + admin → endpoint

DELETE protegido

Se agregó al endpoint:

current_user: Usuario = Depends(require_admin)

Pruebas reales:

id=6, rol=user
DELETE /usuarios/5
→ 403
→ db.delete() no se ejecutó

id=7, rol=admin
DELETE /usuarios/5
→ 200
→ db.delete()
→ db.commit()

PostgreSQL confirmó la eliminación del usuario 5 con (0 rows).

Autorización actual

El JWT identifica al usuario mediante sub; el rol se consulta desde PostgreSQL:

JWT → sub → get_current_user() → PostgreSQL → current_user.rol → require_admin()

Si id=7 cambia de admin a user, un JWT aún válido sigue autenticando la misma identidad, pero la siguiente operación exclusiva de admin devuelve 403.

Mapa mental

Authorization: Bearer JWT
→ HTTPBearer
→ decode_access_token()
→ payload["sub"]
→ get_current_user()
→ objeto Usuario
→ current_user.rol
→ require_admin()
   ├─ user  → 403
   └─ admin → endpoint

Estado

Día 102 COMPLETADO. Progreso: 102/112. Restan 10 días.