'''
#Codigo 1

import requests

r = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

#print(r.status_code)
#print(r.json())
r = requests.get(url)


# Codigo 2

import requests

r = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

print(type(r))
'''

#Codigo 3

import requests

r = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

print(r.status_code)
print(r.url)
print(r.reason)
print(r.elapsed)


'''
import requests

r = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

print("Tipo:", type(r))
print("Status:", r.status_code)
print("URL:", r.url)
print("Reason:", r.reason)
print("Tiempo:", r.elapsed)

datos = r.json()

print("Tipo del JSON:", type(datos))
print("Cantidad de usuarios:", len(datos))
print("Primer usuario:", datos[0]["name"])
'''