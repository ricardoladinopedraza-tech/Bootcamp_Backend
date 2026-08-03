import requests

respuesta = requests.delete(
    "https://jsonplaceholder.typicode.com/users/5"
)

print(respuesta.status_code)

if respuesta.status_code in (200, 204):
    print("Usuario eliminado.")
else:
    print("Error:", respuesta.status_code)