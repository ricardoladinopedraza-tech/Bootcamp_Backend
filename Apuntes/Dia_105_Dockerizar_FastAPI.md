Día 105 — Dockerizar FastAPI
Objetivo
Aplicar Docker al Proyecto 1: construir una imagen FastAPI, ejecutar Uvicorn en un contenedor, publicar el puerto 8000 y conectar temporalmente el contenedor con PostgreSQL ejecutándose en Windows.
Dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY App ./App

CMD ["uvicorn", "App.main:app", "--host", "0.0.0.0", "--port", "8000"]
Conceptos:
- FROM: imagen base.
- WORKDIR: directorio de trabajo dentro de la imagen/contenedor.
- COPY requirements.txt .: copia la lista de dependencias.
- RUN pip install -r requirements.txt: instala dependencias durante docker build.
- COPY App ./App: incorpora el código FastAPI.
- CMD: comando predeterminado al arrancar el contenedor.
- 0.0.0.0: permite a Uvicorn escuchar por las interfaces de red del contenedor.
RUN → durante docker build
CMD → durante docker run, al arrancar el contenedor
El venv de Windows no se copia: la imagen Linux tiene su propio Python e instala sus dependencias desde requirements.txt.
Construcción
Inicialmente Docker Engine no estaba iniciado. Tras abrir Docker Desktop, docker info confirmó cliente y servidor operativos.
Se construyó:
docker build -t bootcamp-fastapi .
Resultado:
bootcamp-fastapi:latest
Primer arranque
docker run -p 8000:8000 bootcamp-fastapi
Falló porque DATABASE_URL era None: .env no estaba dentro de la imagen.
No se copió .env a la imagen. Se inyectaron sus variables al arrancar:
docker run --env-file .env -p 8000:8000 bootcamp-fastapi
Uvicorn arrancó correctamente.
Publicación de puertos
-p 8000:8000
   ↑    ↑
 host  contenedor
docker ps confirmó el contenedor Running y el mapeo del puerto. Swagger cargó desde Windows en localhost:8000/docs.
Problema PostgreSQL
Swagger funcionaba, pero GET /usuarios/1 devolvió 500:
connection to server at "127.0.0.1", port 5432 failed
Connection refused
Causa:
FastAPI dentro del contenedor
        ↓
localhost:5432
        ↓
localhost = el propio contenedor
        ↓
PostgreSQL no está allí
PostgreSQL seguía ejecutándose en Windows.
Concepto clave:
localhost del contenedor ≠ localhost de Windows
Conexión temporal al host
Docker Desktop proporciona:
host.docker.internal
Sin modificar el .env original ni mostrar credenciales, se creó temporalmente en PowerShell una URL sustituyendo localhost por host.docker.internal:
$env:DOCKER_DATABASE_URL = (Get-Content .env | Where-Object { $_ -match '^DATABASE_URL=' }) -replace '^DATABASE_URL=', '' -replace 'localhost', 'host.docker.internal'
Luego:
docker run --env-file .env -e "DATABASE_URL=$env:DOCKER_DATABASE_URL" -p 8000:8000 bootcamp-fastapi
--env-file cargó las variables y -e DATABASE_URL=... sobrescribió solamente la URL de base de datos para ese contenedor.
Arquitectura final del Día 105:
Navegador Windows
       ↓
localhost:8000
       ↓
Contenedor FastAPI
       ↓
SQLAlchemy / psycopg
       ↓
host.docker.internal:5432
       ↓
PostgreSQL en Windows
Prueba final
GET /usuarios/1 devolvió 200 OK con información real almacenada en PostgreSQL.
Se confirmó:
Windows → Docker → Uvicorn → FastAPI
→ SQLAlchemy → psycopg → PostgreSQL → 200 OK
Conceptos consolidados
- El contenedor no utiliza el venv de Windows.
- RUN construye/prepara la imagen; CMD define el proceso al arrancar.
- -p HOST:CONTENEDOR publica puertos.
- Uvicorn escucha en 0.0.0.0 dentro del contenedor.
- .env no fue incorporado a la imagen; sus variables se suministraron en ejecución.
- Swagger puede funcionar aunque falle la conexión a PostgreSQL.
- localhost dentro de Docker representa al propio contenedor.
- host.docker.internal permitió acceder temporalmente al PostgreSQL del host.
Estado
Día 105 de 112 completado. Restan 7 días.