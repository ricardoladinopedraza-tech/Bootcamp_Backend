Día 100 — JWT + FastAPI: Protección de Endpoints

Objetivo

Usar el JWT del Día 99 para proteger endpoints mediante Authorization: Bearer <JWT>.

HTTPBearer

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
security = HTTPBearer()

Si llega:

Authorization: Bearer eyJ123.xyz456.abc789

entonces:

credentials.scheme       → Bearer
credentials.credentials  → eyJ123.xyz456.abc789

HTTPBearer busca y extrae las credenciales Bearer; no valida por sí solo la firma y expiración de nuestro JWT.

Endpoint de práctica

Se creó /protegido con:

credentials: HTTPAuthorizationCredentials = Depends(security)

Pruebas:

Sin credenciales → 401 {"detail": "Not authenticated"}
Con Bearer        → 200

Verificación del JWT

Se conectó:

token = credentials.credentials
payload = decode_access_token(token)

Con un JWT válido:

{
  "mensaje": "Acceso permitido",
  "sub": "6"
}

Error encontrado

Una prueba con un valor que no era un JWT completo produjo:

jwt.exceptions.DecodeError: Not enough segments

Como no se estaba capturando la excepción, inicialmente terminó en 500 Internal Server Error.

Se corrigió:

try:
    payload = decode_access_token(token)
except jwt.PyJWTError:
    raise HTTPException(
        status_code=401,
        detail="Token inválido o expirado"
    )

Resultados:

JWT inválido/expirado → 401
JWT válido            → 200

Protección real de GET /usuarios

El endpoint quedó:

@app.get("/usuarios")
def listar_usuarios(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    try:
        decode_access_token(token)
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=401,
            detail="Token inválido o expirado"
        )

    usuarios = db.query(Usuario).all()
    return usuarios

Pruebas:

GET /usuarios sin autorización → 401
GET /usuarios con JWT válido    → 200

Distinción fundamental

En palabras consolidadas durante la sesión:

HTTPBearer se encarga de buscar el header de autorización y obliga a presentar credenciales, mientras que decode_access_token() se encarga de verificar el JWT.

Mapa mental:

Authorization: Bearer <JWT>
→ HTTPBearer
→ credentials.credentials
→ decode_access_token()
→ firma + exp válidos?
   NO → 401
   SÍ → ejecutar endpoint
→ PostgreSQL
→ 200

Problema pendiente

La validación se repetiría en cada endpoint:

token = credentials.credentials
try:
    decode_access_token(token)
except jwt.PyJWTError:
    ...

El Día 101 resolverá esta duplicación mediante una dependencia reutilizable get_current_user.

Estado

Día 100 — JWT + FastAPI: COMPLETADO.