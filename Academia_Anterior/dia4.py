
'''
#Bucles

contador = 1

while contador <= 5:
    print("Numero:", contador)
    contador = contador + 1

for numero in range(1, 6):
    print("Numero:", numero)
'''
    
'''
contador = 10

while contador >= 0:
    print("Numero:", contador)
    contador = contador - 1


for numero in range(10, 0, -1):
    print(numero)


clave = ""

while clave != "python123":
    clave = input("ingresa la contraseña:")

print("Acceso concedido")


Numero = int(input("Digite un numero:"))
Multiplicador = 1

while Multiplicador <= 10:
    Multiplicacion = Numero * Multiplicador
    print(Numero, "X", Multiplicador, "=", Multiplicacion)
    Multiplicador = Multiplicador + 1


numero = int(input("Digite un numero:"))
suma = 0

for i in range(1, numero + 1):
    suma += i

print("La suma de los numeros de 1 a", numero, "es", suma) 



numero = int(input("Digita un numero:"))
suma = 0
contador = 1

while contador <= numero:
    suma += contador
    contador += 1

print("La suma de los numeros de 1 a", numero, "es", suma)


# Vamos a sumar numeros hasta que el usuario desida salir

total = 0

while True:
    entrada = input("ingresa un numero para sumar (o escribe 'salir'):")

    if entrada == 'salir':
        break

    numero = int(entrada)
    total += numero

print("La suma total es:", total)

palabras = []

while True:
    entradas = input("Ingresa una palabra (o escribe 'Fin'):")

    if entradas == 'Fin':
        break

    palabras.append(entradas)

print("nuemro de palabras ingresadas:", len(palabras))
print("Las palabras digitadas son:", palabras)

resultado = 0
resultado_1 = 0
resultado_2 = 0



while True:
    print("Elija el tipo de operacion a ejecutar")
    print("Digite 1 para Suma")
    print("Digite 2 para Resta")
    print("Digite 3 para multiplicacion")
    print("Digite 4 para Salir")
    entrada = int(input("Ingresa un numero para el tipo de operacion (o escribe 'Salir'):"))
   
    if entrada == 4:
        print("Saliendo del programa. Hasta luego!")
        break

    elif entrada == 1:
        numero_1 = int(input("Digite un numero para sumar: "))
        numero_2 = int(input("Digite otro sumero para suma: "))
        resultado = numero_1 + numero_2
        print("La suma de los dos numeros es: ", resultado)

    elif entrada == 2:
        numero_3 = int(input("Digite un numero para restar: "))
        numero_4 = int(input("Digite otro sumero para restar: "))
        resultado_1 = numero_3 - numero_4
        print("La resta de los dos numeros es: ", resultado_1)

    elif entrada == 3:
        numero_5 = int(input("Digite un numero para multiplicar: "))
        numero_6 = int(input("Digite otro sumero para multiplicar: "))
        resultado_2 = numero_5 * numero_6
        print("La multiplicacion de los dos numeros es: ", resultado_2)

    else:
        print("Opcion no valida. Por favor elige 1, 2, 3 o 4")
'''

################################################################## for
'''
lista = [1, 2, 3]

for num in lista:
    print(num)
    

for i in range(5):
    print(i)

############################################ while
i = 0

while i < 5:
    print(i)
    i += 1

for i in range(10):
    if i == 5:
        break
    print(i)


for i in range(5):
    if i == 2:
        continue
    print(i)

    
for i in range(3):
    print(i)
else:
    print("Fin del ciclo")

for i in range(3):
    for j in range(2):
        print(i, j)

#Tabla de multiplcar

n = int(input("Numero: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")


suma = 0

for i in range(1, 6):
    suma += i

print(suma)


while True:
    n = int(input("Numero positivo: "))
    
    if n > 0:
        print("Correcto, numero positivo")
        break
        
    else:
        print("Error, intenta de nuevo")
        

########### Ejercicios

#1.

for i in range (1, 11):
    print(i)


#2

for i in range(-10, 0):
    i = i * -1
    print(i)


#3.

for i in range(2, 21 , 2):
    print(i)


#4.

i = 0

while i < 5:
    print(i)
    i += 1


#5.
multiplicacion = 0

n = int(input("Digite un numero para tabla de multiplicar: "))

for i in range(1, 11):
    multiplicacion = i * n
    print(f"{n} x {i} = {n*i}")


#6.
suma = 0
for i in range(1, 101):
    suma += i

print(suma)

#7.

numeros = []
suma = 0

while True:
    numero = int(input("Digita uno o varios numeros para sumar, digita 0 para sumar: "))
    if numero == 0:
        suma = sum(numeros)
        print("La suma de los numeros digitados es: ", suma)
        break
        
    else:
        numeros.append(numero) 


suma = 0

while True:
    numero = int(input("Numero (0 para salir): "))
    
    if numero == 0:
        break
    
    suma += numero

print("Suma:", suma)

#8.
n = 0
for i in range(1, 21):
    n = i % 2
    if n == 1:
        print("Fizz")
    else:
        print(i)

for i in range(1, 21):
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)


#9.
i = 1
fact = 1
n = int(input("Digita un numero para factorial: "))
while i <= n:
    fact *= i
    i += 1

print(fact)

#10

cant_digitos = 0
numero = int(input("Digita un numero: "))
cant_digitos = len(str(numero))
print(f"El número {numero} tiene {cant_digitos} dígitos.")

cantidad_digitos = 0
numer = int(input("Digita un numero: "))
for digito in str(abs(numero)):
    cantidad_digitos += 1

print(f"El número {numer} tiene {cantidad_digitos} dígitos.")


#11.

numeros = []
suma = 0

while True:
    numero = int(input("Digita uno o varios numeros, digita numero negativo para salir: "))
    if numero < 0:
        print("Los numeros digitados son: ", *numeros)
        break
        
    else:
        numeros.append(numero) 

contador = 0

while True:
    numero = int(input("Numero (negativo para salir): "))
    
    if numero < 0:
        break
    
    contador += 1

print("Cantidad:", contador)

#12.

for i in range(1, 6):
    print("*" * i)

#13.

usuario = "admin"
contraseña = "1234"
i = 0

while True:
    user = input("Digita usuario: ")
    passwd = input("Digita contraseña: ")
    i += 1
    if i == 3:
        print("Cuenta bloqueada")
        break
            
    if usuario == user and contraseña == passwd:
        print("Acceso Permitido")
        break
    
    else:
        print("Acceso denegado. Usuario y/o contraseña incorrectas")

intentos = 0

while intentos < 3:
    user = input("Usuario: ")
    passwd = input("Contraseña: ")
    
    if user == "admin" and passwd == "1234":
        print("Acceso permitido")
        break
    
    intentos += 1

if intentos == 3:
    print("Cuenta bloqueada")

#14.

n = 7


while True:
    numero = int(input("Digita un numero de 1 a 10: "))
    if numero == n:
        print("Correcto")
        break

    else:
        if numero > n:
            print("Muy alto")
                
        else:
            print("Muy bajo")
           

#15.

n = int(input("Numero: "))

if n <= 1:
    print("No es primo")
else:
    es_primo = True
    
    for i in range(2, n):
        if n % i == 0:
            es_primo = False
            break
    
    if es_primo:
        print("Es primo")
    else:
        print("No es primo")

#Traducción humana:

#“Supongo que el número es primo (True)”

#“Si encuentro divisor, dejo de pensar eso (False)”


#print(5 < 3)   # True
#print(5 < 3)   # False

nota = 4.5
if nota >= 3 or recuperacion == True:
    print("Aprobado")
 

#mas ejercicios de loca booleana (True, False, and, or, not).

#1. 

print(5 > 3) #imprime True

#2.

print(10 == 5) #imprime False

#3.

print(7 != 7) #imprime False

#4. 

#print(8 ___ 4)   # debe dar True
print(8 > 4)
print(8 != 4)

#5.
print(True and False) #imprime False

#6. 
print(True or False) #imprime True

#7. 
print(not True) #imprime False

#8.
print(5 > 3 and 2 < 1) #imprime False

#9.
print(10 > 5 or 3 > 8) #imprime True

#10.
print(not (4 == 4)) #imprime False

#11.
edad = 20
tiene_id = True

if edad == 20 and tiene_id == True:
    print("Acceso permitido")

#12. 
nota = 2.5
recuperacion = True

if nota >= 2.5 and recuperacion == True:
    print("Aprobado")

#13.
x = 5
print(x > 3 and x < 10) #imprime True

#14.
x = 5
print(x > 10 or x == 5) #inprime True

#15.
x = 5
print(not (x > 3)) #imprime False

#16.
#Pide un número e imprime:
#"Dentro del rango" si está entre 10 y 20
#"Fuera del rango" si no

n = int(input("Digita un numero: "))
if (n >= 10) and (n <= 20):
    print("Dentro del rango")
else:
    print("Fuera de rango")

#17.

#Pide:
#usuario
#contraseña
#Permite acceso si:
#usuario es "admin" o
#contraseña es "1234"
usuario = "admin"
contraseña = "1234"

user = input("Usuario: ")
passwd = input("Contraseña: ")
if (user == usuario) or (passwd == contraseña):
    print("Acceso permitido")

#18
#Pide un número e imprime:
#"No válido" si es negativo
#"Válido" si no

m = int(input("Digita un numero: "))
if not(m >= 0):
    print("No valido")
else:
    print("Valido")
    '''