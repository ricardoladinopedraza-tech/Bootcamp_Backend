Día 106 — Docker Compose: FastAPI + PostgreSQL
Objetivo
Integrar el Proyecto 1 con Docker Compose, ejecutando FastAPI y PostgreSQL en contenedores separados, conectados por la red interna de Compose y con persistencia mediante un volumen Docker.
Arquitectura final
Windows / Navegador
        |
        | localhost:8000
        v
+------------------------+
| API container          |
| FastAPI + SQLAlchemy   |
| psycopg + Alembic      |
+-----------+------------+
            |
            | db:5432
            v
+------------------------+
| DB container           |
| PostgreSQL 17          |
+-----------+------------+
            |
            v
      postgres_data
       (persistente)
Docker Compose
Se verificó docker compose version y se trabajó con Docker Compose v5.5.1.
Se definieron dos servicios: db y api.
Servicio PostgreSQL
db:
  image: postgres:17
db es el nombre del servicio y funciona también como hostname dentro de la red de Compose. postgres:17 es una imagen existente.
Las variables POSTGRES_USER, POSTGRES_PASSWORD y POSTGRES_DB se toman de .env, evitando escribir secretos directamente en compose.yaml.
Persistencia
Se configuró el volumen:
volumes:
  - postgres_data:/var/lib/postgresql/data
y el volumen nombrado:
volumes:
  postgres_data:
Concepto clave: contenedor PostgreSQL ≠ almacenamiento persistente.
Puertos
Se utilizó:
ports:
  - "5433:5432"
porque PostgreSQL de Windows ya usa 5432.
Windows → PostgreSQL Docker: localhost:5433
API container → PostgreSQL container: db:5432
Windows → PostgreSQL Windows: localhost:5432
Servicio FastAPI
api:
  build: .
Diferencia:
- image: postgres:17: usa una imagen existente.
- build: .: construye nuestra imagen usando el Dockerfile y el directorio actual como contexto.
build: . no significa /app; /app es el WORKDIR dentro de la imagen.
Conexión API → DB
La API utiliza una DATABASE_URL cuyo host es db y cuyo puerto interno es 5432.
Flujo:
FastAPI → SQLAlchemy → psycopg → db:5432 → PostgreSQL
Healthcheck y depends_on
Se configuró pg_isready como healthcheck y:
depends_on:
  db:
    condition: service_healthy
Esto evita confundir “contenedor iniciado” con “PostgreSQL listo para aceptar conexiones”.
Primer arranque
Con:
docker compose up -d --build
se construyó/inició la API, PostgreSQL quedó healthy y se creó la red de Compose.
Error detectado: tablas inexistentes
La nueva base Docker estaba vacía. Una consulta produjo:
psycopg.errors.UndefinedTable: relation "usuarios" does not exist
Esto demostró que API → SQLAlchemy → psycopg → PostgreSQL sí funcionaba, pero faltaba el esquema.
Alembic dentro de Docker
El Dockerfile se amplió con:
COPY App ./App
COPY alembic ./alembic
COPY alembic.ini .
Así el contenedor API dispone del historial de migraciones.
Deuda técnica descubierta
La migración inicial 3965e7b974fd_estado_inicial.py tenía upgrade() y downgrade() vacíos. Alembic se había introducido cuando las tablas ya existían en PostgreSQL Windows, por lo que podía evolucionar esa base pero no reconstruir una base vacía.
Reparación de la migración inicial
Se reconstruyó únicamente el esquema histórico original:
usuarios:
  id
  nombre
  correo

pedidos:
  id
  producto
  usuario_id → usuarios.id
No se incluyeron telefono, ciudad, password_hash, rol ni UNIQUE(correo) porque corresponden a migraciones posteriores.
Cadena:
3965e7b974fd → esquema inicial
d8848d64e7cc → telefono
47e20a3d7e7f → ciudad
e76e34cf8d6b → password_hash
56acf0546194 → rol
37e09c3bcc17 → correo UNIQUE
Transactional DDL
Después de un intento fallido se comprobó:
alembic current → ninguna revisión aplicada
\dt             → ninguna relación
El intento se había revertido, evitando un esquema parcialmente migrado.
Migración completa desde cero
Se ejecutó:
docker compose exec api alembic upgrade head
Toda la cadena llegó correctamente a:
37e09c3bcc17 (head)
La base contiene:
alembic_version
pedidos
usuarios
Esquema vs datos
La tabla usuarios apareció con 0 registros.
Concepto fundamental:
Alembic migra ESQUEMA
        ≠
migrar DATOS
PostgreSQL Windows y PostgreSQL Docker son instancias independientes. Alembic no copia automáticamente los registros de una a otra.
Validación mediante FastAPI
Antes de migrar:
GET /usuarios/1 → 500 UndefinedTable
Después:
GET /usuarios/1 → 404
El 404 demuestra que la consulta ya funciona y simplemente no existe el registro solicitado.
Se creó después un usuario de prueba mediante la API y quedó almacenado en PostgreSQL Docker.
Prueba de persistencia
Se ejecutó:
docker compose down
docker compose up -d
Los contenedores y la red fueron eliminados y recreados. El usuario de prueba continuó existiendo.
contenedor anterior → eliminado
postgres_data       → permanece
contenedor nuevo    → reutiliza postgres_data
datos               → permanecen
No se utilizó docker compose down -v, porque -v eliminaría también el volumen.
Conceptos consolidados
- Servicio, imagen y contenedor son conceptos diferentes.
- image usa una imagen existente; build construye una propia.
- Dentro de Compose se usa db:5432; desde Windows se usa localhost:5433.
- healthcheck comprueba que PostgreSQL esté realmente preparado.
- depends_on con service_healthy hace esperar a la API.
- Los volúmenes permiten persistencia independiente de los contenedores.
- Alembic debe poder reconstruir el esquema completo desde una base vacía.
- Alembic administra principalmente el esquema; no copia automáticamente datos entre bases.
Resultado
Proyecto funcionando como:
FastAPI container
       ↓
Docker network
       ↓
PostgreSQL container
       ↓
Docker volume
Día 106 completado.