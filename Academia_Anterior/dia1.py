'''
#Primer programa

Nombre = input("Como te llamas?  ")
Edad = input("Cuantos años tienes?  ")
Estatura = input("Cuanto mides?  ")

print("Buenos dias", Nombre)
print("Tienes", Edad, "Años")
print("Mides", Estatura, "centimetros")


print("A", "B", "C", sep=" # ")

print("Hola ", end='')
print("Hola", end=" ")
print("Mundo")
print("Hola", end='... ')


for i in range(5):
    print(i, end='\"')


nombre = "Ana"
print(f"Hola {nombre}")

a = 5
b = 3
print(f"La suma es {a + b}")

print(f"{'Hola':<10}")  # izquierda
print(f"{'Hola':>10}")  # derecha
print(f"{'Hola':^10}")  # centro

print("Hola " + nombre)


lista = [1, 2, 3]
print(lista)

for x in lista:
    print(x)

for i in range(5):
    print(i, end="\n")

lista = [1, 2, 3]
print(*lista)


with open("archivo.txt", "w") as f:
    print("Hola archivo", " ", "Ricardo Ladino Pedraza esta probando Python 2026", file=f)
    print("Hola pelota", file=f)
    

print("Cargando...", flush=True)


import time

# Sin flush=True, los puntos podrían salir todos juntos al final
for i in range(5):
    print(".", end="", flush=True)                
    time.sleep(1)
    
#EVALUACION
#Nivel 1
print("Hola estoy aprendiendo Python")

nombre = "Luis"
edad = 20

print("Nombre:", nombre, "Edad:", edad)


print("A", "B", "C", "D", sep="-")

print("Hola", end=' ')
print("Mundo")

# Nivel 2
numero = 3.14159
print("El valor es: ", end='')
print(f"pi= {numero:.2f}")

a = 5
b = 7
print(f"La suma de a y b es: {a+b}")

for i in range(6):
    print(i, end='\n')

lista = [10, 20, 30]
print(*lista, end='')

#Nivel 3
nombre = "Ana"
promedio = 4.5678
print(f"Nombre: {nombre}  | Promedio: {promedio:.2f}")

print(f"{'Hola':>10}")

estudiantes = [{"nombre": "Juan", "nota": 3.5}, {"nombre": "Maria", "nota": 4.2}]

for est in estudiantes:
    print(f"Nombre: {est['nombre']} - Nota: {est['nota']:.2f} ")

lista = [1, 2, 3, 4, 5]
print(*lista)

for i in range(1, 6):
    print(i, end=" ")
 
    
def calcular_promedio(notas):
    return sum(notas) / len(notas)

def registrar_estudiante():
    nombre = input("Nombre de estudiante: ")

    notas = []
    for i in range(2):
        while True:
            nota = float(input(f"Digite a nota: {i+1}:"))
            
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
'''
'''
productos = ["pan", "leche", "huevos"]
print("Lista de compras: ", end='')
for i in productos:
    print(i, end=', ')


print(f"{'Nombre':>10} {'Nota':>10}")
print(f"{'Juan':>10} {'3.50':>10}")
print(f"{'Maria':>10} {'4.20':>10}")
'''

numero = 3.14159
print(f"El valor es {numero:.2f}")