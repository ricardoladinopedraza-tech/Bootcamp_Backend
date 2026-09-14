Día 96 — Autenticación vs. Autorización

Objetivo

Comprender la diferencia entre autenticación y autorización como base del bloque de seguridad.

Autenticación

Responde ¿Quién eres? y está relacionada con la identidad.

credenciales / token → verificación → identidad confirmada

Autorización

Responde ¿Qué puedes hacer? y está relacionada con permisos y roles.

Un usuario puede estar autenticado y no estar autorizado para una operación.

401 y 403

401 Unauthorized → autenticación ausente o inválida
403 Forbidden    → autenticado, pero sin permiso

Mapa mental:

AUTENTICACIÓN → ¿Quién eres?       → identidad
AUTORIZACIÓN  → ¿Qué puedes hacer? → permisos / roles

Reto consolidado

Ana
JWT válido
rol = usuario
DELETE /usuarios/5 requiere admin

Autenticada: sí.

Autorizada para DELETE: no.

Respuesta: 403.

Si cambia su rol a admin, no cambia su identidad; cambia su autorización.

Bloque

Día 96  → Autenticación vs. autorización
Día 97  → Hashing
Día 98  → Login
Día 99  → JWT
Día 100 → Protección de endpoints
Día 101 → get_current_user
Día 102 → Roles/permisos
Día 103 → Seguridad Proyecto 1

Estado: Día 96 completado y consolidado.