Día 97 — Hashing de contraseñas

Objetivo

Evitar contraseñas en texto plano e implementar hashing seguro con pwdlib + Argon2.

Conceptos

La contraseña original no se guarda:

password → hashing → password_hash → PostgreSQL

Hashing no es cifrado: no necesitamos recuperar la contraseña original. Durante el login verificaremos una contraseña candidata contra el hash almacenado.

Salt

Con algoritmos modernos, la misma contraseña puede producir hashes diferentes debido al salt. Por eso no generamos dos hashes y los comparamos directamente.

Implementación

Se instaló pwdlib[argon2] dentro del venv.

App/security.py:

from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)

Comprobación:

verify_password("Python2026", hash)        → True
verify_password("claveIncorrecta", hash)   → False

SQLAlchemy

En Usuario:

password_hash = Column(String, nullable=True)

Se eligió temporalmente nullable=True porque existen usuarios antiguos sin contraseña.

Alembic

Migración:

Revision: e76e34cf8d6b
Revises: 47e20a3d7e7f

op.add_column(
    "usuarios",
    sa.Column("password_hash", sa.String(), nullable=True)
)

PostgreSQL confirmó la columna password_hash.

Creación de usuario

El endpoint transforma:

password recibida
      ↓
hash_password()
      ↓
password_hash
      ↓
PostgreSQL

Ejemplo:

nuevo_usuario = Usuario(
    nombre=nombre,
    correo=correo,
    password_hash=hash_password(password)
)

No exponer el hash

Al principio el objeto SQLAlchemy devolvía password_hash. Se creó UsuarioResponse:

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    correo: str
    telefono: str | None = None
    ciudad: str | None = None

    model_config = {"from_attributes": True}

y:

@app.post("/usuarios", response_model=UsuarioResponse)

Resultado comprobado:

Contraseña original en PostgreSQL → NO
Hash Argon2 almacenado             → SÍ
Hash expuesto por la API           → NO

PostgreSQL mostró para el usuario de prueba un valor $argon2id$....

Entorno virtual

Se descubrió que PowerShell mostraba (venv) pero algunos comandos resolvían el Python global. El venv está sano; por ahora se usan rutas explícitas:

.\venv\Scripts\python.exe -m uvicorn App.main:app --reload
.\venv\Scripts\alembic.exe ...
.\venv\Scripts\python.exe -m pip ...

requirements.txt fue regenerado desde el Python del venv.

Mapa final

REGISTRO:
password → hash_password() → Argon2 → password_hash → PostgreSQL

LOGIN (Día 98):
password introducida + password_hash → verify_password() → True / False

Estado: Día 97 completado y consolidado.