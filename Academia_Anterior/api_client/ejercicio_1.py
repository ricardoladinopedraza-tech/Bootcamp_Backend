import requests

params = {
    "userId": 1,
    "id": 5
}

r = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)

print(r.json())