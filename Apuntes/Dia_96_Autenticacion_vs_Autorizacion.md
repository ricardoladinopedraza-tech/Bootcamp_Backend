Día 96 — Autenticación vs. Autorización

Objetivo

Comprender la diferencia entre autenticación y autorización antes de implementar contraseñas, login, JWT, protección de endpoints y roles en FastAPI.

Autenticación

Responde: ¿Quién eres?

correo + contraseña
        ↓
verificación
        ↓
identidad confirmada
        ↓
usuario autenticado

El login es un mecanismo de autenticación. En peticiones posteriores, un JWT válido también permitirá identificar al usuario.

Autorización

Responde: ¿Qué puedes hacer?

Usuario autenticado: Ana
Rol: usuario
DELETE /usuarios/5 requiere admin
        ↓
operación denegada

Estar autenticado no significa estar autorizado para hacer todo.

Mapa mental

AUTENTICACIÓN → ¿Quién eres?       → identidad
AUTORIZACIÓN  → ¿Qué puedes hacer? → permisos / roles

HTTP 401 y 403

401 Unauthorized

En el contexto estudiado, indica que no existe una autenticación válida.

Sin token / token inválido
        ↓
401
        ↓
"No puedo confirmar quién eres"

403 Forbidden

El sistema conoce al usuario, pero este no tiene permiso para realizar la operación.

JWT válido
   ↓
usuario autenticado
   ↓
rol = usuario
   ↓
DELETE requiere admin
   ↓
403

Asociación:

Autenticación → 401 si no es válida
Autorización  → 403 si falta permiso

Ejercicio consolidado

Para DELETE /usuarios/10:

Situación

Resultado

No envía token

401

Token inválido

401

Token válido + rol usuario, pero requiere admin

403

Token válido + rol admin

Puede continuar

Reto final

Caso:

Ana
JWT válido
rol = usuario
DELETE /usuarios/5 requiere admin

Conclusiones:

Ana está autenticada.

Ana no está autorizada para ese endpoint.

La respuesta corresponde a 403 Forbidden.

Si únicamente cambia rol = usuario por rol = admin, la identidad sigue siendo Ana.

Por tanto, no cambia la autenticación; cambia la autorización.

Conexión con el bloque de seguridad

Día 96  → Autenticación vs. autorización
Día 97  → Hashing de contraseñas
Día 98  → Login
Día 99  → JWT
Día 100 → JWT + FastAPI
Día 101 → get_current_user
Día 102 → Roles y permisos
Día 103 → Seguridad del Proyecto 1

Conclusión

Conceptos consolidados:

Autenticación = identidad.

Autorización = permisos.

Un usuario puede estar autenticado y no autorizado para una operación.

401 se relaciona con autenticación ausente o inválida.

403 se relaciona con falta de autorización.

Cambiar un rol no cambia quién es el usuario; cambia lo que puede hacer.

Estado: Día 96 completado.