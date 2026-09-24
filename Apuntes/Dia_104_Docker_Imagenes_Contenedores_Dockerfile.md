Día 104 — Docker: imágenes, contenedores y Dockerfile

Objetivo

Comprender los fundamentos de Docker antes de dockerizar el Proyecto 1: imagen, contenedor, Dockerfile y el ciclo Dockerfile → build → imagen → run → contenedor.

Preparación del entorno

Se configuró y verificó:

WSL 2.

Ubuntu sobre WSL 2.

Docker Desktop.

Docker CLI.

Docker Engine.

Comandos de comprobación:

docker --version
docker info

Conceptos fundamentales

Imagen

Una imagen Docker es una plantilla preparada para crear contenedores. No es un programa en ejecución.

Contenedor

Un contenedor es una instancia creada a partir de una imagen. Una misma imagen puede originar múltiples contenedores.

Dockerfile

Archivo de instrucciones que describe cómo construir una imagen.

Dockerfile
    ↓
docker build
    ↓
Imagen
    ↓
docker run
    ↓
Contenedor

Práctica con hello-world

Se ejecutó:

docker run hello-world

Docker obtuvo la imagen, creó un contenedor, ejecutó /hello, mostró Hello from Docker! y el proceso terminó correctamente.

Comandos estudiados:

docker images
docker ps
docker ps -a

docker images: imágenes locales.

docker ps: contenedores actualmente en ejecución.

docker ps -a: todos los contenedores, incluidos los detenidos.

Exited (0): el proceso terminó correctamente.

Primera imagen propia

Estructura:

practica_docker_104/
├── Dockerfile
└── saludo.py

saludo.py:

print("Hola desde mi primer contenedor Docker")

Dockerfile:

FROM python:3.13-slim

WORKDIR /app

COPY saludo.py .

CMD ["python", "saludo.py"]

Instrucciones

FROM python:3.13-slim: define la imagen base.

WORKDIR /app: establece /app como directorio de trabajo dentro de la imagen/contenedor.

COPY saludo.py .: copia el archivo al directorio de trabajo de la imagen.

CMD ["python", "saludo.py"]: define el comando predeterminado al arrancar el contenedor.

CMD queda definido durante el build, pero se ejecuta al iniciar el contenedor.

Construcción

docker build -t saludo-docker .

docker build: construye una imagen.

-t saludo-docker: asigna nombre/tag.

.: utiliza la carpeta actual como contexto de construcción.

Imagen obtenida:

saludo-docker:latest

Ejecución

docker run saludo-docker

Resultado:

Hola desde mi primer contenedor Docker

Después el contenedor quedó en Exited (0) porque python saludo.py terminó.

Experimento clave

Se modificó saludo.py en Windows después del build. Al ejecutar nuevamente docker run saludo-docker sin reconstruir, apareció el mensaje antiguo.

Después de ejecutar un nuevo:

docker build -t saludo-docker .
docker run saludo-docker

apareció el código actualizado.

Conclusión:

Modificar el código fuente
        ≠
Modificar una imagen ya construida

docker run no reconstruye la imagen. Para incorporar cambios copiados durante el build es necesario construir nuevamente la imagen.

Diferencias clave

docker build → construye una imagen
docker run   → crea y ejecuta un contenedor a partir de una imagen

El contenedor permanece activo mientras su proceso principal siga ejecutándose. saludo.py termina; Uvicorn permanecerá escuchando solicitudes, por lo que el futuro contenedor FastAPI podrá permanecer Running.

Comprobación final

Se consolidó:

Imagen = plantilla para crear contenedores.

Contenedor = instancia creada a partir de una imagen.

Dockerfile = instrucciones para construir una imagen.

FROM = imagen base.

WORKDIR = directorio de trabajo.

COPY = incorpora archivos a la imagen.

CMD = comando predeterminado al arrancar.

Una imagen ya construida no cambia automáticamente al modificar el código fuente.

Estado

Día 104 de 112 completado.