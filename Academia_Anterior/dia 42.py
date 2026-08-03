#Entornos Virtuales (venv) y Gestión de Dependencias

#Este es uno de los temas que empiezan a acercarte al trabajo real de desarrollador 
# backend. A partir de aquí ya no solo escribes Python: comienzas a trabajar como 
# lo hacen los programadores profesionales.

#1. ¿Qué problema resuelven los entornos virtuales?
#Imagina que tienes dos proyectos:
#Proyecto A:
'''
fastapi==0.95

#Proyecto B:

fastapi==0.120

#Si instalas todo globalmente:

pip install fastapi

#las versiones pueden entrar en conflicto.
#Para evitarlo, cada proyecto tiene su propio entorno virtual.

#2. Crear un entorno virtual
#Dentro de la carpeta del proyecto:

python -m venv venv

#Se crea una carpeta:

#mi_proyecto/
#│
#├── venv/
#├── app.py

#3. Activar el entorno
#Windows

venv\Scripts\activate

#Verás algo parecido a:

(venv) C:\proyecto>

#Linux/Mac

source venv/bin/activate

#4. Instalar paquetes

#Una vez activado:

pip install requests

#Ahora el paquete queda instalado únicamente para este proyecto.

#5. Ver paquetes instalados
pip list

#Ejemplo:

requests
urllib3
certifi

#6. Guardar dependencias o exportar los paquetes
#Cuando termines:

pip freeze > requirements.txt

#Se genera:

requests==2.32.0
urllib3==2.0.0
certifi==2026.1.1

#7. Instalar dependencias desde requirements.txt
#Otro desarrollador puede ejecutar:

pip install -r requirements.txt

#Y tendrá exactamente las mismas librerías.

#8. Desactivar el entorno

deactivate  #Se desactiva el entorno virtual y vuelves a usar la instalación global 
            #de Python.

Vuelves al Python global.

#9. Flujo real de trabajo

#Crear proyecto:

mkdir api_client

#Entrar:

cd api_client

#Crear entorno:

python -m venv venv

#Activar:

venv\Scripts\activate

#Instalar librerías:

pip install requests

#Guardar dependencias:
#Genera un archivo requirements.txt con todas las dependencias instaladas en el 
# entorno virtual y sus versiones.

pip freeze > requirements.txt

#>>>>>>>>>>>> 10. Lo que debes recordar para entrevistas >>>>>>>>>>>>>>

#Pregunta:

#¿Qué es un entorno virtual?

#Respuesta:

#Es un entorno aislado que permite instalar dependencias específicas para un proyecto 
#sin afectar otros proyectos ni la instalación global de Python.

'''

#Ejercicios de análisis (sin ejecutar)
#Ejercicio 1

#python -m venv entorno

#¿Qué hace este comando? >>> Crea un entorno virtual llamado entorno

#Ejercicio 2

#pip install requests

#¿Para qué sirve? >>> Instala la libreria requests

#Ejercicio 3

#pip freeze > requirements.txt

#¿Qué genera?  >>> Guardar las dependencias o exportar los paquetes al archivo
# requirements

#Ejercicio 4

#pip install -r requirements.txt

#¿Qué hace?  >>> Se instalan las dependencias desde requirements

#Ejercicio 5

#deactivate

#¿Qué ocurre después de ejecutarlo?  >>> Regresar a la raiz de la carpeta y salir 
#del entorno virtual

#Mini reto extra (nivel entrevista)
#Sin ejecutar código:
#Tienes un proyecto con esta estructura:

#   mi_app/
#   │
#   ├── venv/
#   ├── main.py
#   ├── requirements.txt

#Un compañero descarga el proyecto desde GitHub.

#¿Qué comandos debe ejecutar para:

#Crear/usar el entorno virtual. >>> Creamos el entorno virtual de la misma manera y 
# con el mismo nombre del entorno del otro desarrollador venv, en la misma carpeta
# y con los mismos comandos. creamos la carpeta mi_app y el entorno python -m venv venv

#Instalar las dependencias. >>> instalamos las depedencias desde el archivo requirements
# del otro desarrollador con el comando pip install -r requirements.txt 

#Ejecutar el proyecto.  >>> Ejecutamos con python .\my_app\main.py
