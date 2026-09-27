Día 108 — Proyecto 1 completamente dockerizado
Objetivo
Integrar Docker, Compose, PostgreSQL, Alembic y FastAPI para que el Proyecto 1 pueda reconstruirse y levantarse de forma reproducible.
Progreso al cierre: 108 / 112.
1. Estado inicial verificado
Se comprobó:
- API activa.
- PostgreSQL activo y healthy.
- Alembic en 37e09c3bcc17 (head).
- El usuario Docker Test seguía almacenado.
2. Automatización de migraciones
Antes, el contenedor API iniciaba directamente Uvicorn. En una base nueva había que recordar ejecutar manualmente:
docker compose exec api alembic upgrade head
Se agregó al servicio api de compose.yaml:
command: >
  sh -c "alembic upgrade head &&
         uvicorn App.main:app --host 0.0.0.0 --port 8000"
Flujo:
alembic upgrade head
        ↓
      éxito
        ↓
       &&
        ↓
     Uvicorn
&& ejecuta Uvicorn solamente si Alembic termina correctamente. Si una migración falla, la API no arranca con un esquema posiblemente incompatible.
3. Healthcheck vs Alembic vs Uvicorn
healthcheck → ¿PostgreSQL acepta conexiones?
Alembic     → ¿el esquema está actualizado?
Uvicorn     → ejecuta FastAPI
healthy no significa que las migraciones estén aplicadas.
4. Prueba del arranque automático
Se recreó api con:
docker compose up -d api
docker compose ps
docker compose logs api
Los logs mostraron primero la conexión de Alembic con PostgreSQL y después el inicio correcto de Uvicorn.
Como la base ya estaba en HEAD, no había migraciones pendientes.
5. Recreación de contenedores
Se ejecutó:
docker compose down
docker compose up -d
sin -v.
Compose recreó red y contenedores. PostgreSQL quedó healthy, Alembic se ejecutó automáticamente y Uvicorn arrancó.
Docker Test siguió existiendo porque los datos están en el volumen postgres_data.
docker compose down
→ elimina contenedores y red
→ conserva volumen

docker compose down -v
→ también elimina volúmenes
6. Prueba HTTP
Se ejecutó:
Invoke-RestMethod http://localhost:8000/usuarios/1
y se obtuvo correctamente:
id       : 1
nombre   : Docker Test
correo   : docker@test.com
Además:
docker compose exec api alembic current
confirmó:
37e09c3bcc17 (head)
7. Reconstrucción limpia de la imagen
Se probó reproducibilidad con:
docker compose down
docker compose build --no-cache api
docker compose up -d
--no-cache obligó a reconstruir la imagen API desde Dockerfile, requirements.txt, código y archivos de Alembic.
Después:
- PostgreSQL quedó healthy;
- API quedó activa;
- Alembic se ejecutó antes de Uvicorn;
- /usuarios/1 siguió devolviendo Docker Test.
8. Imagen vs volumen
Corrección conceptual importante:
docker compose build --no-cache api
es una operación de build, no runtime.
No destruyó los datos porque:
Imagen API
├── código
├── dependencias
└── Alembic

Volumen postgres_data
└── datos PostgreSQL
Reconstruir la imagen API no elimina el volumen PostgreSQL.
9. Flujo completo
docker compose up -d
        ↓
Compose crea red/contenedores
        ↓
PostgreSQL inicia
        ↓
healthcheck
        ↓
PostgreSQL healthy
        ↓
depends_on permite iniciar API
        ↓
alembic upgrade head
        ↓
esquema actualizado
        ↓
&&
        ↓
Uvicorn
        ↓
FastAPI :8000
        ↓
GET /usuarios/1
        ↓
endpoint FastAPI
        ↓
SQLAlchemy
        ↓
psycopg
        ↓
db:5432
        ↓
PostgreSQL
        ↓
tabla usuarios / id=1
        ↓
respuesta HTTP
        ↓
Docker Test
10. Conceptos consolidados
- Migraciones automáticas antes del servidor.
- Significado de &&.
- Healthcheck y migraciones tienen responsabilidades diferentes.
- Persistencia mediante volumen.
- Diferencia entre imagen, contenedor y volumen.
- Reconstrucción con --no-cache.
- Comunicación API ↔ PostgreSQL.
- Flujo completo de una petición HTTP.
Arquitectura final
                  Docker Compose
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
        API container        DB container
           FastAPI           PostgreSQL 17
              │                   │
           Alembic                ▼
              │             postgres_data
           SQLAlchemy
              │
            psycopg
              │
              └──── db:5432 ──────┘
Día 108 completado y aprobado.
