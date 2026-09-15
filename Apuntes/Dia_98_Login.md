Día 98 — Login

Objetivo

Implementar el proceso básico de login en FastAPI usando correo, contraseña, SQLAlchemy, PostgreSQL y verify_password().

En este día no se implementa JWT. JWT corresponde al Día 99.

Flujo conceptual

correo + contraseña
        ↓
buscar usuario por correo
        ↓
obtener password_hash
        ↓
verify_password()
        ↓
True / False
        ↓
login correcto / 401

Schema de credenciales

En App/schemas/usuario.py:

class LoginRequest(BaseModel):
    correo: str
    password: str

Distinción clave:

data.password          → contraseña introducida por el usuario
usuario.password_hash  → hash almacenado en PostgreSQL

Buscar usuario

usuario = db.query(Usuario).filter(
    Usuario.correo == data.correo
).first()

.first() devuelve un objeto Usuario o None.

Correo inexistente y seguridad

No se responde "El correo no existe". Se usa un mensaje genérico para no revelar qué cuentas están registradas:

if usuario is None:
    raise HTTPException(
        status_code=401,
        detail="Credenciales incorrectas"
    )

Verificar contraseña

if not verify_password(
    data.password,
    usuario.password_hash
):
    raise HTTPException(
        status_code=401,
        detail="Credenciales incorrectas"
    )

Lógica:

Password correcta   → verify_password() = True  → not True  = False → Login correcto
Password incorrecta → verify_password() = False → not False = True  → 401

Usuarios antiguos con password_hash NULL

Como en el Día 97 password_hash quedó temporalmente nullable=True, los usuarios antiguos pueden tener NULL.

Se protegió el endpoint:

if usuario is None or usuario.password_hash is None:
    raise HTTPException(
        status_code=401,
        detail="Credenciales incorrectas"
    )

Esto evita intentar:

verify_password(data.password, None)

En psql, los NULL aparecían como espacios vacíos. Se pueden localizar con:

SELECT id, nombre, correo, password_hash
FROM usuarios
WHERE password_hash IS NULL;

Endpoint final del Día 98

@app.post("/login")
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
        Usuario.correo == data.correo
    ).first()

    if usuario is None or usuario.password_hash is None:
        raise HTTPException(
            status_code=401,
            detail="Credenciales incorrectas"
        )

    if not verify_password(
        data.password,
        usuario.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Credenciales incorrectas"
        )

    return {"mensaje": "Login correcto"}

Pruebas realizadas

Correo válido + contraseña correcta      → 200, Login correcto
Correo válido + contraseña incorrecta    → 401, Credenciales incorrectas
Usuario antiguo con password_hash = NULL → 401, Credenciales incorrectas
Correo inexistente                       → 401 por diseño

También se comprobó que el password_hash no debe retornarse públicamente.

Mapa mental final

POST /login
     ↓
LoginRequest
correo + password
     ↓
buscar Usuario por correo
     ↓
¿usuario existe y tiene password_hash?
     │
     ├── NO → 401
     │
     └── SÍ
          ↓
verify_password(data.password, usuario.password_hash)
          ↓
     ┌────┴────┐
   False      True
     ↓          ↓
    401    Login correcto

Conceptos consolidados

Login comprueba credenciales.

data.password es la contraseña enviada.

usuario.password_hash es el hash almacenado.

.first() devuelve un usuario o None.

No se debe revelar si un correo específico existe.

Credenciales inválidas responden 401.

verify_password() realiza la comprobación segura.

not False es True y activa el bloque de error.

password_hash = NULL debe controlarse antes de verificar.

El hash no debe devolverse al cliente.

JWT todavía no forma parte del Día 98.

Estado: Día 98 — Login COMPLETADO Y CONSOLIDADO.