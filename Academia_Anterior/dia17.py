#Funciones avanzadas Join()

#¿Qué hace .join()?
#.join() une elementos de una lista en un solo texto.
'''
palabras = ["Hola", "mundo"]

resultado = " ".join(palabras)

print(resultado)

#El separador importa
#El texto antes de .join() es el separador. se puede agregar "-"

palabras = ["Hola", "mundo"]

resultado = "-".join(palabras)

print(resultado)

palabras = ["Hola", "mundo"]

resultado = " * ".join(palabras)

print(resultado)

#Ejemplo real
nombres = ["Ana", "Luis", "Pedro"]

texto = ", ".join(nombres)

print(texto)

nombres = ["Ana", "Luis", "Pedro"]

texto = " - ".join(nombres)

print(texto)

# *******  Importante ⚠️  *********
#join() SOLO funciona con strings.

numeros = [1, 2, 3]

",".join(numeros) #Esto genera error, por que solo trabaja con strings


#Cómo solucionar eso     Usamos map().
numeros = [1, 2, 3]
texto = "-".join(map(str, numeros)) #map() “Convierte cada número en texto usando str()”.
print(texto) #     join() SOLO puede unir texto (str).

#split() — el opuesto de join
#Convierte texto en lista.

texto = "Python es genial"
lista = texto.split()
print(lista)

#Entonces… ¿qué hace map()?
#map() aplica una función a cada elemento.
#La estructura es:

#   map(funcion, lista)
#En este caso
#   map(str, numeros)

#significa:

#“Convierte cada número en texto usando str()”.
#Paso a paso 🔍

#Lista original:

#   [1, 2, 3]

#Python hace esto internamente:

#   str(1)
#   str(2)
#   str(3)

#Resultado:

#     ["1", "2", "3"]

#Ahora sí join() puede trabajar:

#      "-".join(["1", "2", "3"])

#Resultado:

#    1-2-3

#Ejemplo
nombres = ["ana", "juan", "pedro"]

resultado = list(map(str.upper, nombres)) # Aquí map() aplica: str.upper() a cada elemento.

print(resultado)

#.split() — el opuesto de join
#Convierte texto en lista.

texto = "Python es genial"
lista = texto.split()
print(lista)

#split() con separador

texto = "rojo,verde,azul"

lista = texto.split(",")

print(lista)
'''
#Mini práctica 🧠
# Ejercicio 1
#Une esta lista usando espacios: palabras = ["Me", "gusta", "Python"]
#Resultado esperado: Me gusta Python

mensaje = ["Me", "gusta", "Python"]
texto = " ".join(mensaje)
print(texto)

#Ejercicio 2
#Une esta lista usando -

numeros = ["1", "2", "3", "4"]
texto = "-".join(map(str, numeros)) 
print(texto) #  

#Ejercicio 3
#Convierte este texto en lista:

texto = "Colombia Peru Ecuador"

lista = texto.split()

print(lista)

#Ejercicio 4
#Convierte este texto usando coma:

texto = "manzana,pera,uvas"

lista = texto.split(",")

print(lista)