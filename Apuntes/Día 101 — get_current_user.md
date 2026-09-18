Día 101 — get_current_user

## Objetivo
Centralizar la validación JWT e identificar en PostgreSQL al usuario autenticado.

## Problema inicial
En el Día 100 cada endpoint protegido repetía la extracción y validación del token. El Día 101 lo resolvió con una dependencia reutilizable.

## Dependencia
```python
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    try:
        payload = decode_access_token(token)
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=401,
            detail="Token inválido o expirado"
        )

    usuario_id = payload["sub"]

    usuario = db.query(Usuario).filter(
        Usuario.id == int(usuario_id)
    ).first()

    if usuario is None:
        raise HTTPException(
            status_code=401,
            detail="Usuario no válido"
        )

    return usuario
```

## Dependencias encadenadas
```text
endpoint
→ Depends(get_current_user)
→ Depends(security)
→ HTTPBearer
→ credentials.credentials
→ decode_access_token()
→ payload["sub"]
→ PostgreSQL
→ objeto Usuario
→ current_user
```

Sin Bearer token, `HTTPBearer` responde 401 antes de ejecutar `decode_access_token()`. Si existe token pero es inválido/expirado, la validación JWT produce el 401 correspondiente.

## Del sub al usuario
Para un token con:
```text
sub = "6"
```
el flujo es:
```text
"6" → int("6") → 6 → Usuario.id == 6 → PostgreSQL → objeto Usuario
```

Recordatorio: `.first()` devuelve un objeto ORM si encuentra registro y `None` si no lo encuentra.

## Refactor de GET /usuarios
La seguridad repetida se sustituyó por:
```python
current_user: Usuario = Depends(get_current_user)
```

Pruebas:
```text
sin autorización → 401
JWT válido        → 200
```

## Endpoint /mi-perfil
```python
@app.get("/mi-perfil")
def mi_perfil(
    current_user: Usuario = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "nombre": current_user.nombre,
        "correo": current_user.correo
    }
```

Con el JWT cuyo `sub` era `"6"`, la prueba devolvió efectivamente:
```text
id = 6
```

Esto demuestra que cada petición identifica al usuario por el JWT enviado en esa petición.

## Distinción final
```text
credentials.credentials → JWT completo
payload["sub"]           → ID del usuario extraído del JWT
current_user             → objeto Usuario recuperado desde PostgreSQL
```

## Estado
**Día 101 — get_current_user: COMPLETADO Y CONSOLIDADO.**
