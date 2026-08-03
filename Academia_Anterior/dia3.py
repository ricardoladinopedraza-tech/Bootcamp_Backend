'''
#Condicionales

edad = int(input("Cual es tu edad?   "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

Nota = float(input("Cuanto sacasste en el examen?  "))

if Nota == 5:
    print("Excelente!")
elif Nota >= 4:
    print("Bueno!")
elif Nota >= 3:
    print("Aceptable!")
else:
    print("Reprobado!")


Num = float(input("Digita un numero   "))

if Num >= 1:
    print("El numero es positivo")
elif Num == 0:
    print("El numero es Cero")
else:
    print("El numero es negativo")

    
    # Prueba de solicitar usuario y contrase;a y verificar con datos guardados
usuario = "admin"
contraseña = "NaRa8o29ii"

user = input("Digite usuario     ")
passwd = input("Contraseña    ")

if user == usuario and passwd == contraseña:
    print("Acceso permitido")
else:
    print("Acceso denegado")
    

# Vamos a generar proyecto con datos de carro

Temperatura = int(input("Cual es la temperatura del motor (Grados C)?  "))
Rpm = int(input("Cuales son las RPM del motor?   "))
Emisiones = int(input("Cual es el valor de emisiones de CO?   "))

if Temperatura <= 50:
    print("El motor esta frio")
elif Temperatura >= 100:
    print("Motor Sobrecalentado")
elif Temperatura > 50 and Temperatura < 100:
    print("Temperatura Adecuada")

if Rpm <= 1000:
    print("Motor en ralenti")
elif Rpm >= 2500 and Rpm < 3000:
    print("Motor en valores adecuados de aceleracion")
elif Rpm <= 3500:
    print("El motor esta sobreacelerado")
else:
    print("Motor extraacelerado")

if Emisiones <= 4:
    print("Rango de Emisiones Correcto")
else:
    print("Tomar Correctivos Alto Nivel de Emisiones")
    

edad = int(input("Digite su edad: "))
id = input("Si tiene id digite 1, si no digite 0: ")
if id == 1:
    tiene_id = True
else: 
    tiene_id = False

if edad >= 18 and tiene_id:
    print("Puede entrar")
else:
    print("No puede entrar")


edad = 20

if edad >= 18:
    if edad >= 60:
        print("Adulto mayor")
    else:
        print("Adulto")


#Condicional en linea (ternario)
edad = 17

mensaje = "Mayor" if edad >= 18 else "Menor"
print(mensaje)

#NIVEL 1
#1.

numero = 0

numero = int(input("Digite un numero: "))
if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")

    
#2.

edad = int(input("Digite su edad: "))
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

    
#3.

nota = float(input("Digite una nota de 0 a 5: "))
if nota >= 3:
    print("Aporbado (>= 3)")
else:
    print("Reprobado (< 3)")
    

#4.

numero = 0

numero = int(input("Digita un numero: "))

if numero % 2 == 0:
    print("Par")
else:
    print("Impar")
    

#5.
n = float(input("Digita un numero: "))

if n > 10:
    print("Mayor que 10")
elif n == 10:
    print("Igual a 10")
else:
    print("Menor que 10")
    
    
#6.

nota = 0

nota = float(input("Digite una nota: "))
if nota >= 4.5:
    print("Excelente (≥ 4.5)")
elif 3.5 <= nota < 4.5:
    print("Bueno (≥ 3.5)")
elif 3 <= nota < 3.5:
    print("Regular (≥ 3) ")
else:
    print("Malo (< 3)")
    

#7.

usuario = input("Digite usuario: ")
contraseña = input("Digite contraseña: ")
if usuario == "admin" and contraseña == "1234":
    print("Acceso correcto")
else:
    print("Acceso denegado")


#8

numero = 0

numero = float(input("Digita un numero: "))
if 0 <= numero <= 100:
    print("Entre 0 y 100")
else:
    print("Fuera de rango")


#9.

n1 = n2 = n3 = 0

n1 = float(input("Digita un numero A. "))
n2 = float(input("Digita otro numero B. "))
n3 = float(input("Digita otro numero C. "))
if n1 >= n2 >= n3:
    print("A es el numero mayor ")
elif n2 >= n1 >= n3:
    print("B es el nuemro mayor")
else:
    if n3 >= n2 > n1:
        print("C es el numero mayor")
'''

#10.

año = int(input("Digite un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Año bisiesto")
else:
    print("No es bisiesto")

#11. 
'''
n1 = n2 = 0
n1 = float(input("Digita un numero: "))
n2 = float(input("Digita otro numero: "))
if n1 == n2:
    print("Son iguales")
elif n1 > n2:
    print("El primero es mayor")
else:
    print("El segundo es mayor")
    

#12
color = input("Digita uno de los colores del semaforo, Rojo, Amarillo o Verde: ")
if color == "Rojo":
    print("Detenerse")
elif color == "Amarillo":
    print("Precaucion")
else:
    print("Avanzar")
    

#13.

nombre = input("Digita nombre: ")
edad = int(input("Digita edad: "))
if 0 < edad <= 12:
    print("Niño  (0-12)")
elif 13 <= edad <= 17:
    print("Adolescente (13-17)")
elif 18<= edad <=59:
    print("Adulto (18-59)")
else:
    print("Adulto mayor (60+)")


#14.

salario = años_t = 0
salario = float(input("Digite salario: "))
años_t = float(input("Digite años de trabajo: "))

if salario < 1000 and años_t > 2:
    aumento = salario * 0.2
    salario += aumento
    print("nuevo salario:", salario)
elif salario < 1000 and años_t <= 2:
    aumento = salario * 0.1
    salario += aumento
    print("nuevo salario:", salario)
else:
    if salario >= 1000:
        aumento = salario * 0.05
        salario += aumento
        print("nuevo salario:", salario)


#15.

notas = []

nota1 = float(input("Digita una nota: "))
notas.append(nota1)
nota2 = float(input("Digita otra nota: "))
notas.append(nota2)
nota3 = float(input("Digita otra nota: "))
notas.append(nota3)
promedio = sum(notas) / len(notas)
promedio = sum(notas) / len(notas)

if nota1 < 2 or nota2 < 2 or nota3 < 2:
    print("Riesgo academico")

if promedio >= 3:
    print("Aprobado")
else:
    print("Reprobado")
'''