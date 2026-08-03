# Día 47 — FastAPI: Path Parameters

#Hoy aprenderemos a crear rutas dinámicas, una de las características más importantes de 
# cualquier API REST.

#Al finalizar este día podrás crear endpoints como:
'''
/usuarios/1
/productos/25
/libros/100

#y hacer que FastAPI capture automáticamente esos valores para usarlos en tu código.

>>>>>>>>>>>>>   ¿Qué son los Path Parameters?    <<<<<<<<<<<<<<<

#Hasta ahora nuestras rutas eran fijas.

Por ejemplo:

@app.get("/usuarios")

Siempre respondía a la misma URL:

http://127.0.0.1:8000/usuarios

Pero ¿qué pasa si queremos obtener un usuario específico?

En lugar de crear una ruta para cada usuario, usamos un parámetro en la ruta.

@app.get("/usuarios/{id}")

Las llaves ({}) indican que esa parte de la URL es una variable.
'''
#Primer ejemplo

from fastapi import FastAPI

app = FastAPI()

@app.get("/usuarios/{id}")
def obtener_usuario(id: int):
    return {
        "id": id
    }

#Si visitas:   http://127.0.0.1:8000/usuarios/7
#La respuesta será:   {    "id": 7     }
#Si visitas:  http://127.0.0.1:8000/usuarios/25
#Obtendrás:  {    "id": 25   }
#No importa el número; FastAPI lo captura automáticamente.