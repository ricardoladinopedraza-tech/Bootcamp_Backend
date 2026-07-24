import requests

r = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

if r.status_code == 200:

    usuarios = r.json()

    if len(usuarios) > 0:

        usuario = usuarios[0]

        print(usuario.get("name"))

        print(usuario.get("phone"))

else:

    print("Error:", r.status_code)