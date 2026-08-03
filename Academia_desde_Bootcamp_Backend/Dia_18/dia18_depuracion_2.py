#Error 1, Indice fuera de rango

import requests

r = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

usuarios = r.json()

print(r.status_code)

#Sabemos que hay: 10 Usuarios.

print(len(usuarios))

print(type(usuarios))

print(usuarios[0]["phone"])

#Si hacemos: 

#print(usuarios[15])  #obtenemos error.   >>  IndexError: list index out of range   <<<

#Error 2 — Clave inexistente

#print(usuarios[0]["telefono"]) # obtenemos KeyError: 'telefono', no existe telefono, existe phone

#Error 3 — Tipo incorrecto

#print(usuarios["name"])  #obtenemos TypeError: list indices must be integers or slices, not str
                        # por que usuarios es una lista no un diccionaroio.


#Error 4 — JSON inesperado  

print(usuarios[0])
