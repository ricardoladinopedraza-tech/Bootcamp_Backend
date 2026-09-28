Día 109 — Conceptos de despliegue
Objetivo
Comprender servidor, hosting, puertos, variables de entorno, Docker, PostgreSQL y HTTPS antes de publicar el Proyecto 1.
Progreso al cierre: 109 / 112.
Desplegar
Localmente:
TU PC → http://localhost:8000
Desplegado:
CLIENTE → Internet → URL pública → servidor/hosting → FastAPI → PostgreSQL
La aplicación deja de depender del computador de desarrollo.
localhost
localhost significa la misma máquina desde la que se realiza la petición, no el disco local. Normalmente se asocia con loopback (127.0.0.1). Una URL pública permite llegar a una aplicación remota desde Internet.
Servidor y hosting
Un servidor es una computadora que ejecuta software y ofrece servicios.
El hosting proporciona infraestructura donde ejecutar/publicar la aplicación: cómputo, red, acceso público, URL/HTTPS y, según el proveedor, servicios como PostgreSQL administrado.
Hosting no significa específicamente PostgreSQL.
Puertos
Localmente:
localhost:8000 → host:8000 → container:8000 → Uvicorn
En producción, la URL pública no tiene por qué conectarse directamente al puerto 8000 del contenedor. La infraestructura puede recibir HTTPS y dirigir internamente el tráfico hacia la aplicación.
0.0.0.0 permite que Uvicorn escuche en las interfaces disponibles del entorno.
PostgreSQL
El usuario no necesita conectarse directamente a PostgreSQL:
Internet → FastAPI → SQLAlchemy → psycopg → PostgreSQL
La API es el punto de entrada.
Variables de entorno
Configuraciones como DATABASE_URL, SECRET_KEY y DEBUG permanecen separadas del código.
LOCAL:
.env → Docker Compose → contenedor

PRODUCCIÓN:
configuración hosting → variables de entorno → aplicación
El .env real no debe publicarse en Git. Si cambia la dirección de PostgreSQL, se cambia DATABASE_URL, no se hardcodea en database.py.
Desarrollo vs producción
DESARROLLO              PRODUCCIÓN
localhost               URL pública
config local            config servidor
secretos locales        secretos producción
DEBUG=True              normalmente DEBUG=False
El objetivo es utilizar el mismo código con configuraciones distintas.
Docker vs hosting
Docker  → empaquetado y entorno reproducible
Hosting → infraestructura para ejecutar/publicar
Docker facilita que la aplicación se ejecute consistentemente en distintos equipos, pero no hace pública la API por sí mismo.
PostgreSQL administrado
Un proveedor puede ofrecer una base PostgreSQL remota. La aplicación accede mediante una DATABASE_URL. Para SQLAlchemy, lo fundamental es disponer de una URL de conexión válida.
HTTPS
HTTPS cifra el tráfico entre cliente y servidor. Es especialmente importante para login, contraseñas, JWT y datos de usuarios.
Responsabilidades
Docker              → entorno reproducible
Hosting             → infraestructura de publicación
Alembic             → evolución del esquema
PostgreSQL          → persistencia
HTTPS               → protección del tráfico
Variables de entorno→ configuración y secretos
FastAPI             → aplicación/API
Flujo de despliegue
Código
→ Repositorio
→ Hosting / servidor remoto
→ Docker
→ variables de entorno
→ Alembic
→ Uvicorn
→ FastAPI
→ SQLAlchemy
→ PostgreSQL
→ URL pública HTTPS
→ Internet
Respuesta tipo entrevista
Dockerizaría la API para tener un entorno reproducible, subiría el código a un repositorio y desplegaría la aplicación en un servicio de hosting. Configuraría allí las variables de entorno y secretos sin publicarlos en Git. Conectaría la API a PostgreSQL mediante DATABASE_URL, ejecutaría las migraciones de Alembic antes de iniciar Uvicorn y expondría la aplicación mediante una URL pública con HTTPS.

Evaluación
Se consolidó:
- localhost corresponde a la máquina que realiza la petición.
- Un cliente remoto no necesita Python, FastAPI, Docker ni PostgreSQL para consumir la API.
- La API desplegada depende del servidor remoto, no del PC de desarrollo.
- Los secretos son configuración del entorno.
- PostgreSQL no necesita exponerse directamente al usuario.
- Docker aporta portabilidad/reproducibilidad.
- Hosting aporta infraestructura de publicación.
- HTTPS protege el tráfico.
Día 109 completado y aprobado.