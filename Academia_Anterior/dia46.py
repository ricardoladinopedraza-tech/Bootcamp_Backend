#Día 46 — Crear una API con FastAPI
#Hoy empieza una etapa muy importante.
#Hasta ahora has sido cliente de una API.
#Desde hoy comenzarás a crear una.

#Qué es FastAPI?
#FastAPI es un framework de Python para construir APIs REST de forma rápida.
#Con muy poco código puedes crear servidores profesionales.

#Por ejemplo:
'''
Cliente
   │
   │ GET
   ▼
Mi API (FastAPI)
   │
   ▼
Respuesta JSON
'''
#Es uno de los frameworks más usados actualmente para backend moderno.

#Instalar FastAPI
'''
#Dentro del entorno virtual:

pip install fastapi

#También necesitaremos un servidor llamado Uvicorn.

pip install uvicorn

#o ambas:

pip install fastapi uvicorn
'''
#>>>>>>>>>>>> CODIGO DE MAIN <<<<<<<<<<<<<<<

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Hola Mundo"}


@app.get("/saludo")
def saludo():
    return {"mensaje": "Bienvenido"}


#>>>>>>>>>>>>>>>>  Analicemos el codigo   >>>>>>>>>>>>>>>>
'''
Analicemos línea por línea

uvicorn #Uvicorn es un servidor web y de aplicaciones para Python ultrarrápido y 
#asíncrono. Su función principal es tomar tu aplicación construida en un framework 
# moderno y exponerla en internet o red local, gestionando las solicitudes HTTP y 
# WebSockets

Importamos FastAPI

from fastapi import FastAPI

Creamos la aplicación

app = FastAPI()

Todo ocurre sobre el objeto app.

El decorador
@app.get("/")

Aquí aparece algo nuevo.

Se llama decorador.

Por ahora puedes verlo como una instrucción que dice:

"Cuando alguien visite esta ruta, ejecuta esta función."

No necesitas aprender cómo funcionan internamente todavía. Más adelante los 
estudiaremos con detalle.

La función
def inicio():

Se ejecutará cuando alguien entre a:

/
El retorno
return {
    "mensaje": "Hola Mundo"
}

FastAPI convierte automáticamente el diccionario en JSON.

No necesitas usar:

json.dumps()

Eso lo hace FastAPI por ti.
'''

#>>>>>>>>>>>>>>   Ejecutar la API    <<<<<<<<<<<<<<<<

'''
Desde la terminal:

uvicorn main:app --reload

¿Qué significa?

main

Nombre del archivo.

main.py
app

Nombre del objeto:

app = FastAPI()
--reload

Cada vez que guardes el archivo, el servidor se reinicia automáticamente.

Muy útil durante el desarrollo.

Si todo salió bien

Verás algo parecido a:

INFO:
Uvicorn running on

http://127.0.0.1:8000

>>>>>>>>>>>>>>>> Lo mejor de FastAPI  >>>>>>>>>>>>>>>>>>

Tiene documentación automática.

Ve a:

http://127.0.0.1:8000/docs

Verás una página donde puedes probar tu API sin usar otro programa.
'''

#>>>>>>>>>>>>>>>>  Errores frecuentes   <<<<<<<<<<<<<<<<<

'''
1. Ejecutar uvicorn fuera del entorno virtual

Activa primero el entorno virtual:

Windows (PowerShell):

.\venv\Scripts\Activate.ps1

Windows (CMD):

venv\Scripts\activate

Luego ejecuta:

uvicorn main:app --reload
2. El archivo no se llama main.py

Si tu archivo se llama api.py, el comando cambia a:

uvicorn api:app --reload

El primer nombre siempre debe coincidir con el archivo (sin la extensión .py).

3. app tiene otro nombre

Si escribiste:

mi_api = FastAPI()

Entonces debes ejecutar:

uvicorn main:mi_api --reload

El segundo nombre del comando debe coincidir con el objeto que creaste.
'''

#Ejercicios de práctica
#Ejercicio 1

#¿Qué hace esta línea? >>> La linea crea la aplicacion app

app = FastAPI()

#Ejercicio 2
#¿Qué ruta crea este código?  >>> Se crea el sitio con la ruta adicional /usuarios
#http://127.0.0.1:8000/usuarios 

@app.get("/usuarios")
def usuarios():
    return {"total": 5}

#Ejercicio 3
#¿Qué devuelve esta función?  >>> devuelve {"edad": 30}

@app.get("/edad")
def edad():
    return {"edad": 30}

#Ejercicio 4
#¿Qué significa el comando?

uvicorn main:app --reload

#Explica qué representa cada una de sus partes:

uvicorn  #>>> servidor web y de aplicaciones
main  #>>> Nombre del archivo
app   #>>> Nombre del objeto
--reload   #>>> Cada vez que se guarda el archivo, el servidor se reinicia automáticamente

#Mini reto
#Escribe una pequeña API con tres rutas:

/
/nombre
/pais

#Cada una debe devolver un diccionario diferente, por ejemplo:

{"nombre": "Ricardo"}

o

{"pais": "Colombia"}

#No importa el contenido exacto; lo importante es practicar la creación de varias rutas.

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Mi apy"}


@app.get("/nombre")
def nombre():
    return {"nombre": "Ricardo"}

@app.get("/pais")
def pais():
    return {"pais": "Colombia"}


#<<<<<<<<<<<<<<< RESUMEN >>>>>>>>>>>>>>>>>>>>>>

Solo añadiría un pequeño detalle:

uvicorn main:app --reload

se interpreta así:

uvicorn

→ Programa que inicia el servidor.

main

→ Archivo main.py.

app

→ Variable donde está creada la aplicación.

--reload

→ Observa los cambios del código y reinicia el servidor automáticamente.

#<<<<<<<<<<<<<<<<<<<<<<<<<<   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

