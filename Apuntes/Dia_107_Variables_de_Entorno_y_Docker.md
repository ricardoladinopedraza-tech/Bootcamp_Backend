Día 107 — Variables de entorno + Docker
Objetivo
Comprender y comprobar cómo pasa la configuración desde .env hasta Docker Compose y finalmente al entorno del contenedor.
.env → Docker Compose → configuración runtime → contenedor → printenv / os.getenv()
1. Código vs configuración
Las credenciales y secretos no deben quedar escritos directamente en el código. Separamos el código (main.py, security.py, database.py) de valores como DATABASE_URL, SECRET_KEY, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB y DEBUG.
Esto permite usar el mismo código con configuraciones distintas en desarrollo, pruebas, Docker y producción.
2. .env no inyecta automáticamente todo al contenedor
Se comprobó:
api: DEBUG       → no disponible inicialmente
api: POSTGRES_DB → no disponible
db:  POSTGRES_DB → bootcamp_backend
Concepto clave:
variable usada POR Compose ≠ variable disponible DENTRO del contenedor
Una variable puede existir en .env y ser usada por Compose para sustitución sin existir como variable independiente dentro de un servicio.
3. Sustitución en Compose
Ejemplo:
POSTGRES_DB: ${POSTGRES_DB}
Compose obtiene el valor y genera la configuración final.
En la API, POSTGRES_USER, POSTGRES_PASSWORD y POSTGRES_DB se utilizan para formar DATABASE_URL, pero no por ello existen individualmente dentro de api.
4. Agregar DEBUG a API
Se añadió:
environment:
  DATABASE_URL: ...
  SECRET_KEY: ${SECRET_KEY}
  DEBUG: ${DEBUG}
Después:
docker compose up -d api
docker compose exec api printenv DEBUG
Resultado:
True
5. Build-time vs Runtime
Agregar DEBUG cambió la configuración de ejecución, no la imagen. Por eso no fue necesario un nuevo build.
Cambio en Dockerfile/dependencias/código copiado
→ build → nueva imagen → contenedor

Cambio en environment/configuración runtime
→ recrear contenedor con nueva configuración
Concepto: BUILD-TIME ≠ RUNTIME.
6. Variables desde Python
Se comprobó:
os.getenv("DEBUG")       → True
os.getenv("POSTGRES_DB") → None
os.getenv() consulta las variables disponibles para el proceso Python dentro del contenedor.
7. No copiar .env a la imagen
Debe evitarse:
COPY .env .
porque incorporaría configuración sensible dentro de la imagen.
La estrategia correcta es:
código + dependencias → imagen
.env → Compose → configuración runtime → contenedor
8. .gitignore vs .dockerignore
Se verificó que .env está ignorado por Git:
git check-ignore -v .env
Resultado: la regla .env de .gitignore lo excluye.
No existía .dockerignore, por lo que se creó con:
# Variables sensibles
.env

# Entornos virtuales
venv/
.venv/

# Python
__pycache__/
*.py[cod]

# Git
.git/
.gitignore

# Cache de pytest
.pytest_cache/
Diferencia:
.gitignore    → qué no debe rastrear Git
.dockerignore → qué se excluye del contexto de build de Docker
9. Estado Git
Se observó:
M  compose.yaml
?? .dockerignore
.env no apareció.
10. environment: vs env_file:
environment:
  DEBUG: ${DEBUG}
permite definir explícitamente qué variables recibe el servicio.
env_file:
  - .env
carga variables del archivo al entorno del contenedor.
En este proyecto se mantiene environment: explícito para controlar qué recibe cada servicio.
11. Cambiar .env y contenedores existentes
Cambiar .env no modifica automáticamente el entorno de un contenedor ya creado. Para aplicar la nueva configuración runtime hay que recrear el servicio, por ejemplo:
docker compose up -d api
No necesariamente se requiere reconstruir la imagen.
12. docker compose config
Se verificó la configuración final resuelta.
API:
DATABASE_URL
DEBUG
SECRET_KEY
DB:
POSTGRES_DB
POSTGRES_PASSWORD
POSTGRES_USER
Precaución: docker compose config puede mostrar secretos ya resueltos; no se debe compartir su salida completa sin ocultarlos.
Evaluación conceptual
Quedaron consolidados:
- .env no implica inyección automática a todos los contenedores.
- sustitución de Compose vs entorno del contenedor;
- .gitignore vs .dockerignore;
- build-time vs runtime;
- environment: vs env_file:;
- printenv y os.getenv();
- secretos fuera de la imagen.
Resultado
Código + Dockerfile → imagen

.env
 ↓
Docker Compose
 ↓
configuración runtime
 ↓
contenedores
Día 107 completado.