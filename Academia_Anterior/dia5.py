'''
#Funciones

def saludar(nombre):
    print("Hola, bienvenido", nombre)

saludar("Ricardo")


def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)


def calcular_promedio(n1, n2, n3):
    promedio = (n1 + n2 + n3)/3
    return promedio

nota = calcular_promedio(4.0, 3.5, 4.5)
print("El promedio es: ", nota)


#crear una funcion que reciba un numero y defina si es par o impar

def numero():
    numero = int(input("Escriba un numero"))
    resultado = numero % 2
    
    if resultado == 1:
        print("El numero es impar")

    else:
        print("El numero es par")

numero()

#########
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def contar_pares_impares(numeros):
    pares = 0
    impares = 0
    for num in numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    print(f"Pares: {pares}, Impares:{impares}")

contar_pares_impares(numeros)


#funcion que calcule el area de un triangulo

def area(a, h):
    return a * h

resultado = area(5, 10)
print("El area de trinagulo es: ", resultado )



def nombre_edad():
    name = input("Digite su nombre: ")
    edad = int(input("Digite su edad: "))
    
    print("Hola", name, ", tienes", edad, "años")

nombre_edad()


def salario():
    horas = float(input("Digite las horas laboradas: "))
    valor_hora = float(input("Digita el valor por hora: "))
    salario = horas * valor_hora

    print("Su salario es: ", salario)

salario()


def Numero():
    number = float(input("Digite un numero cualquiera: "))

    if number > 0:
        print("El numero es positivo")
    
    elif number == 0:
        print("El numero es cero")
    
    else:
        print("El numero es negativo")

Numero()

########################

resultado = ()

def evaluar_numero(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Cero"
    
resultado = evaluar_numero(0)
print(resultado)


def Numero():
    number = float(input("Digite un numero cualquiera: "))

    if number > 0:
        return "El numero es positivo"
    
    elif number < 0:
        return "El numero es negativo"
    
    else:
        return "El numero es Cero"
    

print(Numero())


# Calculadora Salarial

def salario():
    horas = float(input("Digite las horas laboradas: "))
    valor_hora = float(input("Digita el valor por hora: "))
    salario = horas * valor_hora

    if horas <= 0:
        print("Error horas debe ser mayor que cero")

    elif valor_hora <= 0:
        print("Error valor hora debe ser mayor que cero")

    elif horas <= 44:
        print("Su salario es: ", salario)

    else:
        extras = (horas - 44)
        normales = 44
        valor_extras = valor_hora * 1.5
        salario = (normales * valor_hora) + (extras * valor_extras)
        print("Su salario mas horas extras es:", salario)

salario()


#Registro de  notas de estudiante. funcion que reciba lista de notas, calcula promedio, 
# nota + alta, nota + baja, retorna valores.


def notas():

    estudiante = []
    nota_0 = float(input("Digite nota Geometria: "))
    nota_1 = float(input("Digite nota Matematicas: "))
    nota_2 = float(input("Digite nota Espa;ol: "))
    nota_3 = float(input("Digite nota Religion: "))
    nota_4 = float(input("Digite nota Sociales: "))
    nota_5 = float(input("Digite nota Artistica: "))
    nota_6 = float(input("Digite nota Edufisica: "))
    nota_7 = float(input("Digite nota Estadistica: "))
    nota_8 = float(input("Digite nota Ingles: "))
    nota_9 = float(input("Digite nota Aritmetica: "))
    estudiante.append(nota_0)
    estudiante.append(nota_1)
    estudiante.append(nota_2)
    estudiante.append(nota_3)
    estudiante.append(nota_4)
    estudiante.append(nota_5)
    estudiante.append(nota_6)
    estudiante.append(nota_7)
    estudiante.append(nota_8)
    estudiante.append(nota_9)
    
    print("Las notas del estudiante son:", estudiante)
    promedio = sum(estudiante) / len(estudiante)
    print("El promedio del estudiante es:  ", promedio)
    minimo = min(estudiante)
    print("La nota mas baja es: ", minimo)
    maximo = max(estudiante)
    print("La nota mas alta es: ", maximo)

notas()


def notas():
    estudiante = []

    for i in range(10):
        while True:
            nota = float(input(f"Digite a nota {i+1}:"))
        
            if 0 < nota <= 5:
                estudiante.append(nota)
                break

            else:
                print("La nota debe estar entre 0 y 5")

    promedio = sum(estudiante) / len(estudiante)
    print("El promedio del estudiante es: ", promedio)

    minimo = min(estudiante)
    print("La nota minima es: ", minimo)

    maximo = max(estudiante)
    print("La nota mas alta es: ", maximo)

notas()


# Registrar estudiantes, guardar sus notas, calcular promedio, mostrar resultados.

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def registrar_estudiante():
    nombre = input("Nombre de estudiante: ")

    notas = []
    for i in range(3):
        while True:
            nota = float(input(f"Digite a nota {i+1}:"))
            
            if 0 < nota <= 5:
                notas.append(nota)
                break

            else:
                print("La nota debe estar entre 0 y 5")

        promedio = calcular_promedio(notas)

        return{"nombre": nombre, "notas": notas, "promedio": promedio}

def mostrar_estudiantes(lista):
    print("\n--- LISTA DE ESTUDIANTES ---")
    for est in lista:
        print(f"Nombre: {est['nombre']}")
        print(f"Notas: {est['notas']}")
        print(f"Promedio: {est['promedio']:.2f}")
        print("--------------------------------")

def main():
    estudiantes = []

    while True:
        print("\n1. Registrar estudiante ")
        print("2. Ver estudiantes ")
        print("3. Salir ")

        opcion =input("Selecciona una opcion: ")

        if opcion == "1":
            estudiante = registrar_estudiante()
            estudiantes.append(estudiante)

        elif opcion == "2":
            mostrar_estudiantes(estudiantes)
        
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opcion invalida")

main()


def saludar():
    print("Hola")

saludar()

############
def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Carlos")
############

def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)

def suma(a, b):  # parámetros
    return a + b

suma(5, 3)       # argumentos


def operaciones(a, b):
    return a + b, a - b

suma, resta = operaciones(10, 5)

def saludar(nombre="Invitado"):
    print(f"Hola {nombre}")

saludar()
saludar("Ana")

def principal():
    def interno():
        print("Hola")
    
    interno()

principal()


def evaluar_estudiante(nombre, notas):
    promedio = sum(notas) / len(notas)
    
    if promedio >= 3:
        estado = "Aprobado"
    else:
        estado = "Reprobado"
    
    return nombre, promedio, estado


n, p, e = evaluar_estudiante("Juan", [3.5, 4.0, 2.8])

print(f"Estudiante: {n}")
print(f"Promedio: {p:.2f}")
print(f"Estado: {e}")


def prueba():
    return 10

x = prueba()
print(x)

def datos():
    return "Juan", 20

a, b = datos()

print(a)
print(b)

def valores():
    return 5, 10, 15

x, y, z = valores()

print(z)

def cosas():
    return "A", "B", "C"

x, y, z = cosas()

print(y)

def prueba():
    return 100

resultado = prueba()

print(resultado + 50)


def prueba():
    print(10)

x = prueba()

print(x)

def datos():
    return "Ana", 4.5

x = datos()

print(x)

def prueba():
    return 1, 2

x = prueba()

print(x)

def prueba():
    return 1, 2, 3

a, b, c = prueba()

print(a + b + c)


#Ejercicios

#1.
def saludo():
    print("Hola Mundo")

saludo()


#2.
def doble():
    n = int(input("digita un numero: "))
    return 2 * n

x = doble()
print(x)


#3.
a = 0
b = 0
def suma(a, b):
    a = int(input("Digita un numero: "))
    b = int(input("Digita otro numero: "))
    return a + b

x = suma(a, b)
print(x)


#4.
def Numero():
    number = float(input("Digite un numero cualquiera: "))

    if number > 0:
        return "El numero es positivo"
    
    elif number < 0:
        return "El numero es negativo"
    
    else:
        return "El numero es Cero"
    

print(Numero())

#5.
def numeros():
    lista = []

    for i in range(10):
        n = float(input(f"Digite un numero {i+1}: "))
        lista.append(n)
        
    promedio = sum(lista) / len(lista)
    return promedio
    
x = numeros()
print("El promedio del estudiante es: ", x)


#6.
def Numero():
    n = int(input("Digite un numero cualquiera: "))
    m = n%2
    if m == 0:
        return True
    else:
        return False
    
print(Numero())


#7.
def nota():
    n = int(input("Digita un numero: "))
    if n >= 3:
        return "Aprobado"
    else:
        return "Reprobado"

print(nota())


#8.
def datos():
    nombre = input("Digite nombre: ")
    edad = int(input("Digite edad: "))
    return nombre, edad

print(datos())


#9.
def numeros():
    lista = []

    for i in range(3):
        n = float(input(f"Digite un numero {i+1}: "))
        lista.append(n)  

    mayor = max(lista) 
    return mayor
    
print(numeros())


#10.
def numeros():
    lista = []

    for i in range(10):
        n = float(input(f"Digite un numero {i+1}: "))
        lista.append(n)
        
    mayor = max(lista)
    menor = min(lista)
    return "el mayor", mayor, "el menor", menor
        
print(numeros())


#11.
def primo():
    n = int(input("Digita un numero: "))

    if n <= 1:
        return False
    else:
        es_primo = True

    for i in range(2, n):
        if n % i == 0:
            es_primo = False
            break
    
        if es_primo:
            return True
        else:
            return False
        
print(primo())


#12.
def alumno():
    notas = []
    for i in range(5):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
 
    promedio = sum(notas) / len(notas)

    if promedio >= 3:
        estado = "Aprobado"
    else:
        estado = "Reprobado"

    return promedio, estado

p, e = alumno()

print(f"Promedio: {p:.2f}")
print(f"Estado: {e}")


#13.
def alumno():
    notas = []
    nombre = input("Digite el nombre del estudiante: ")
    
    for i in range(5):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
 
    promedio = sum(notas) / len(notas)

    if promedio >= 3:
        estado = "Aprobado"
    else:
        estado = "Reprobado"
    
    return nombre, promedio, estado

n, p, e = alumno()

print(f"Nombre: {n}"  " | "  f"Promedio: {p:.2f}"  " | "  f"Estado: {e}")


#14.
def numero():
    n = int(input("Digita un numero: "))
    m = n%2
    if m == 0 and n > 10:
        return "Par y mayor que 10"
    
    elif m == 0:
        return "Par"
        
    else:
        return "Impar"
    
print(numero())


#15.
def pares_impares():
    lista = []
        
    for i in range(10):
        n = float(input(f"Digite un numero {i+1}: "))
        lista.append(n)

    pares = [n for n in lista if n % 2 == 0]
    impares = [n for n in lista if n % 2 == 1]
    cantidad_pares = len(pares)
    cantidad_impares = len(impares)
    return cantidad_pares, cantidad_impares

p, i = pares_impares()
print("Numeros pares: ", p)
print("Numeros impares: ", i)
'''