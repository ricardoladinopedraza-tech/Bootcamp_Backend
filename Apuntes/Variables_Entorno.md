# Día 60 – Variables de Entorno (.env)

## Objetivo

Comprender la importancia de separar la configuración de una aplicación del código fuente utilizando variables de entorno.

---

# El problema

En aplicaciones pequeñas es común escribir configuraciones directamente en el código.

Ejemplo:

```python
DATABASE_URL = "postgresql://usuario:password@localhost/clinica"
```

Aunque funciona, presenta varios problemas:

- Expone información sensible.
- Obliga a modificar el código cuando cambia la configuración.
- Aumenta el riesgo de publicar credenciales en GitHub.

---

# ¿Qué es una variable de entorno?

Es un valor de configuración que la aplicación lee al iniciar su ejecución.

Permite modificar el comportamiento de la aplicación sin cambiar el código.

---

# Archivo .env

Normalmente las variables de entorno se almacenan en un archivo llamado:

.env

Ejemplo:

```text
APP_NAME=Proyecto_Backend
APP_VERSION=1.0

DB_HOST=localhost
DB_PORT=5432
DB_NAME=clinica
DB_USER=postgres
DB_PASSWORD=MiPassword

SECRET_KEY=MiClaveSecreta

DEBUG=True
```

---

# ¿Qué información suele almacenarse?

- Dirección de la base de datos.
- Usuario de la base de datos.
- Contraseña.
- Puerto.
- Claves secretas.
- Tokens.
- Configuración del servidor.
- Variables de desarrollo o producción.

---

# Información que NO debe almacenarse

El archivo `.env` contiene **configuración de la aplicación**, no información del negocio.

Por ejemplo, **no** deben almacenarse:

- Usuarios registrados.
- Pacientes.
- Productos.
- Facturas.
- Historias clínicas.

Estos datos pertenecen a la base de datos.

---

# Ventajas

- Mayor seguridad.
- Código más limpio.
- Configuración independiente.
- Facilita el despliegue.
- Permite usar el mismo código en diferentes entornos.

---

# Flujo conceptual

Aplicación

↓

Lee archivo .env

↓

Obtiene configuración

↓

Continúa ejecutándose

---

# Organización del proyecto

Proyecto_1/

├── .env
├── main.py
├── routers/
├── services/
├── models/
├── database/
└── requirements.txt

---

# Relación con los temas anteriores

Hasta el momento conocemos:

- Endpoints
- Path Parameters
- Query Parameters
- Validaciones
- Request Body
- Field()
- Optional
- Modelos anidados
- Listas de modelos
- Response Models
- Routers
- Prefix
- Tags
- Depends()
- Services
- Variables de entorno

Cada tema fortalece la arquitectura de una aplicación backend profesional.

---

# Idea clave

El código define cómo funciona la aplicación.

El archivo `.env` define con qué configuración funciona.

Cambiar la configuración no implica modificar el código.

---

# Conclusión

Las variables de entorno permiten separar la configuración del código fuente, mejorando la seguridad, el mantenimiento y la facilidad de despliegue de una aplicación.