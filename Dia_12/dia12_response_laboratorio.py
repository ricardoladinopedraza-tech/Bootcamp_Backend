#Ejemplo

import requests

r = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

print("========== RESPONSE ==========")

print("URL:")
print(r.url)

print("\nSTATUS:")
print(r.status_code)
print(r.reason)

print("\nTIEMPO:")
print(r.elapsed)

print("\nHEADERS:")
print(r.headers)

print("\nTEXT:")
print(r.text[:200])

print("\nCONTENT:")
print(r.content[:100])

print("\nJSON:")
print(r.json()[0])