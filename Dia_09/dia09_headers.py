#Codigo 1

import requests

r = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

#print(r.headers)
print(type(r.headers))
print(r.headers["Content-Type"])
print(r.headers["Date"])