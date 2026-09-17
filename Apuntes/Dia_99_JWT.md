Día 99 — JWT (JSON Web Token)

Objetivo

Implementar JWT en el login para entregar un access token firmado y con expiración. La protección de endpoints queda para el Día 100.

Flujo

correo + password
→ buscar usuario
→ verify_password()
→ create_access_token()
→ JWT
→ access_token + token_type

Conceptos

Un JWT tiene conceptualmente:

HEADER.PAYLOAD.SIGNATURE

Un JWT firmado no equivale a contenido cifrado. Por eso no incluimos password ni password_hash.

Payload:

{"sub": "6"}

sub identifica al usuario.

PyJWT

Instalado dentro del venv:

.\venv\Scripts\python.exe -m pip install PyJWT

Versión comprobada: 2.14.0.

SECRET_KEY y algoritmo

En .env se almacena SECRET_KEY; no se escribe en el código ni se sube a Git.

En App/security.py:

import os
import jwt
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

Durante las pruebas apareció InsecureKeyLengthWarning porque la clave inicial tenía 19 bytes. Se corrigió generando una nueva:

.\venv\Scripts\python.exe -c "import secrets; print(secrets.token_hex(32))"

La comprobación len(SECRET_KEY.encode()) devolvió 64.

Crear token

from datetime import datetime, timedelta, timezone

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

data.copy() evita modificar directamente el diccionario original.

Verificar token

def decode_access_token(token: str) -> dict:
    return jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

Prueba inicial:

{'sub': '6'}

Después de añadir expiración:

{'sub': '6', 'exp': 1789604323}

Token expirado

Se creó deliberadamente un token con exp un minuto en el pasado. PyJWT respondió:

jwt.exceptions.ExpiredSignatureError: Signature has expired

Esto confirmó que jwt.decode() verifica la expiración.

Integración con POST /login

En App/main.py se importó create_access_token.

El login ahora termina:

access_token = create_access_token(
    {"sub": str(usuario.id)}
)

return {
    "access_token": access_token,
    "token_type": "bearer"
}

Swagger devolvió:

{
  "access_token": "xxxxx.yyyyy.zzzzz",
  "token_type": "bearer"
}

Verificación final

El token real generado por /login fue verificado:

{'sub': '6', 'exp': 1789605350}

Esto confirmó:

sub identifica al usuario id 6.

exp establece la expiración.

el JWT está firmado con SECRET_KEY + HS256.

el login ya entrega una credencial reutilizable.

Mapa mental

POST /login
→ correo + password
→ buscar Usuario
→ verify_password()
→ create_access_token()
→ sub = usuario.id
→ exp = +30 minutos
→ JWT firmado
→ access_token

Estado

Día 99 — JWT: COMPLETADO Y CONSOLIDADO.