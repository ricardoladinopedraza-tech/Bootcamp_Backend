'''
#Variables y operaciones

a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)

num1 = 20
num2 = 4

print("Los numeros son:", num1, "y", num2)

resultado = num1 * num2

print("La multiplicacion es:", resultado)

num1 = 20
num2 = 4

resultado = num1 + num2

print("La suma es:", resultado)

nombre = input("Cual es tu nombre y Apellido?   ")
edad = input("Cual es tu edad?   ")
print("Hola!", nombre)
print("Tienes!", edad, "años")

numero_1 = input("Ingresa un numero:   ")
numero_2 = input("Ingresa otro numero:   ")

suma = int(numero_1) + int(numero_2)

print("la suma de los dos numeros es: ", suma)


####### VARIABLES Y OPERACIONES


#ver tipo de dato

nombre = "Ana"
edad = 20
precio = 10.5
activo = True

print(type(nombre))
print(type(edad))
print(type(precio))
print(type(activo))


#Cambiar tipo de variable
numero = "10"
print(type(numero))
numero = int(numero)
print(type(numero))

#Operaciones matematicas
a = 10
b = 3

print(a + b)  # suma
print(a - b)  # resta
print(a * b)  # multiplicación
print(a / b)  # división
print(a // b) # división entera
print(a % b)  # residuo
print(a ** b) # potencia


#prioridad en operaciones
resultado = 2 + 3 * 4  # 14
print(resultado)
resultado = (2 + 3) * 4  # 20
print(resultado)

#operaciones con strings

nombre = "Juan"
apellido = "Perez"

print(nombre + " " + apellido)

#Repeticion

print("Hola " * 3)

#Comparaciones
a = 5
b = 10

print(a == b)  # igual
print(a != b)  # diferente
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#operaciones logicas
print(True and False)
print(True or False)
print(not True)
print(not False)
print(True + False)
print(True * False)

#Asignaciones abreviadas

x = 5

x += 2  # x = x + 2
x -= 1
x *= 3
x /= 2


#Evaluacion

#Nivel 1
#1.
a = 5
b = 7
print("la suma es:", (a + b))

#2.
nombre = input("Digite su nombre: ")
edad = input("Digite su edad: ")
print("Hola", nombre, "Tienes", edad, "a;os")

#3.
precio = 100
incremento = precio + (precio * 0.15)
print(incremento)

#4.
numero = "25"
print(int(numero) + 10)


#Nivel 2

#5.
numero = input("Digita un numero")
x = numero
print("la suma es: ", (x += numero))

#6.
a = 17
b = 3
print("Division entera: ", (a // b))
print("El residuo es: ", (a % b))

#7. 
numero = float(input("Digita un numero: "))
if numero > 10:
    print("El numero es mayor que 10")
else:
    print("El numero es menor o igual a 10")

#8.
nombre = "Ana"
nota = 4.5
print("Estudiante: ", nombre, "-", "Nota: ", nota)

#9.
a = float(input("Digita un numero: "))
b = float(input("Digita otro numero: "))
c = float(input("Digita otro numero: "))

promedio = ((a + b + c) / 3)
print(f"Promedio:  {promedio:.2f}")


#10.
x = 5

x *= 4
print("Resultado final: ", x)

#11
numero = float(input("Digita un numero: "))
verificacion = (numero % 2)
if verificacion == 1:
    print("El numero es impar")
else:
    print("El numero es par")

#12
nombre = input("Digita Nombre: ")
salario = float(input("Digita salario: "))
incremento = (salario * 0.1)

salario += incremento
print("Empleado: ", nombre)
print(f"Nuevo salario:  {salario}")


#13

nombre = input("Digite nombre: ")

def notas():
    estudiante = []

    for i in range(3):
        while True:
            nota = float(input(f"Digite a nota {i+1}:"))
            
            if 0 < nota <= 5:
                estudiante.append(nota)
                break
            else:
                print("La nota debe estar entre 0 y 5")


    promedio = sum(estudiante) / len(estudiante)
    if promedio >= 3:
        print("Estudiante: ", nombre, end='\n')
        print(f"Promedio:  {promedio:.2f}")
        print("Estado: Aprobado")
    else:
        print("Estudiante: ", nombre, end='\n')
        print(f"Promedio:  {promedio:.2f}")
        print("Estado: Reprobado")

notas()
'''