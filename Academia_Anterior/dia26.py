#Día 26 – Manejo de Excepciones (Try / Except)
#Las excepciones permiten que un programa continúe funcionando cuando ocurre un error inesperado.

#En Python, la instrucción try sirve para probar y ejecutar código que puede causar un error 
# en tiempo de ejecución. Su función principal es evitar que tu programa se detenga abruptamente (crash) 
# si algo falla. En su lugar, permite controlar cómo responder ante el problema.Generalmente, 
# try se usa en conjunto con la palabra clave except.¿Cómo funciona?
# #try (intentar): Ejecuta el bloque de código principal.
# except (excepto): Si ocurre cualquier error dentro del bloque try





'''
numero = int(input("Ingresa un número: "))
print(10 / numero)

#2. Uso de try y except

try:
    numero = int(input("Ingresa un número: "))
    print(10 / numero)

except ZeroDivisionError:
    print("No puedes dividir entre cero.")

#Ahora el programa no se rompe.

#3. Capturar varios errores
try:
    numero = int(input("Ingresa un número: "))
    print(10 / numero)



except ZeroDivisionError:
    print("No puedes dividir entre cero.")

#4. Uso de else

#   else se ejecuta solo si no hubo errores.

try:
    numero = int(input("Número: "))
    resultado = 10 / numero

except ZeroDivisionError:
    print("Error: división por cero.")

except ValueError:
    print("Debes escribir un número.")

else:
    print("Resultado:", resultado)

#5. Uso de finally
# finally se ejecuta siempre.

try:
    numero = int(input("Número: "))
    print(10 / numero)

except ZeroDivisionError:
    print("Error.")

#except ValueError:
 #   print("Debes escribir un número.")

#else:
 #   print("Resultado:", resultado)

finally:
    print("Programa finalizado.")

#Ejercicio 1
#Solicita un número al usuario.   
#Si escribe texto, mostrar: "Debes ingresar un número."
#Si escribe un número válido, mostrar:  "Número correcto."

try:

    numero = int(input("Digita un numero: "))

except ValueError:
    print("Debes ingresar un numero! ")

else:
    print("Numero correcto! ")

#Ejercicio 2
#Pide dos números.  Realiza una división.  
#Controla:    ValueError    ZeroDivisionError

division = 0

try:

    numero1 = int(input("Digita un numero: "))
    numero2 = int(input("Digita otro numero: "))
    division = numero1 / numero2

except ValueError:
    print("Debes digitar un numero! ")

except ZeroDivisionError:
    print("No se puede dividir por cero! ")

else: 
    print("Resultado: ", division)

#Ejercicio 3
#Crea una lista:    nombres = ["Ana", "Luis", "Pedro"]
#Pide una posición al usuario e intenta mostrar el elemento.
#Controla el error cuando la posición no exista.   Pista:   IndexError

nombres = ["Ana", "Luis", "Pedro"]

try:

    i = int(input("Digita posicion de la lista: "))
    print(nombres[i])

except ValueError:  #Evita que se digite letras y de error
    print("Debes ingresar un número.")

except IndexError:
    print("Estas intentando acceder a una posicion de la lista que no existe! ")

#Mini Reto (Nivel Entrevista Junior)
# Crea una calculadora simple:  1. Sumar   2. Restar   3. Multiplicar   4. Dividir
#Debe:   Pedir dos números.  Capturar errores de texto.  Capturar división por cero. 
#Mostrar el resultado correcto.
sumar = 0
restar = 0
multiplicar = 0
dividir = 0

try:

    print("Digita un numero para la operacion que desea realizar!")
    operacion = int(input("Digita 1. Suma - 2. Resta - 3. Multiplicacion - 4. Division: " ))
    numero1 = int(input("Digita u numero para operaciones: "))
    numero2 = int(input("Digita otro numero para operaciones: "))

    if operacion == 1:
        sumar = numero1 + numero2
        print("La suma es: ", sumar)

    elif operacion == 2:
        restar = numero1 - numero2
        print("La resta es: ", restar)

    elif operacion == 3:
        multiplicar = numero1 * numero2
        print("La multiplicacion es: ", multiplicar)

    else: 
        dividir = numero1 / numero2
        print("La division es: ", dividir)

    else: #evita que se digite un numero mayor de 4 para la operacion!!!! Error
    print("Operacion no valida")

except ValueError:
    print("Por favor digita un numero!")

except ZeroDivisionError:
    print("No se puede dividir por cero!")
'''

