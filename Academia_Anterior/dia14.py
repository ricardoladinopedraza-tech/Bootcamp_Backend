######### Try\Except      Errores
'''
numero = int(input("Digite un número: ")) #Aparecera ValueError si no se digita un numero. programa se detien


#Solución: try / except

try:  #Python intenta ejecutar el codigo
    numero = int(input("Digite un número: "))
    print(numero)

except:  # si encuentra un erro entra aqui
    print("Error: debes escribir un número")

#Ejemplo

try:
    edad = int(input("Digite su edad: "))
    print("Tu edad es:", edad)

except:
    print("Entrada inválida")

#Error especifico. Es mejor capturar errores especificos

try:
    numero = int(input("Digite un número: "))
    print(numero)

except ValueError:
    print("Eso no es un número válido")

#otro ejemplo

try:
    numero1 = int(input("Número 1: "))
    numero2 = int(input("Número 2: "))

    resultado = numero1 / numero2

    print(resultado)

except ZeroDivisionError:
    print("No se puede dividir entre cero")

except ValueError:
    print("Debes escribir números")

#Múltiples except
#Puedes manejar distintos errores.

try:
    # código

except ValueError:
    # error 1

except ZeroDivisionError:
    # error 2

#else
#else se ejecuta SOLO si NO hubo errores.

try:
    numero = int(input("Digite número: "))

except ValueError:
    print("Error")

else:
    print("Todo salió bien")

#finally
#finally se ejecuta SIEMPRE.

try:
    print("Intentando...")

except:
    print("Error")

finally:
    print("Fin del programa")

#Ejemplo completo

try:
    numero1 = int(input("Digite número 1: "))
    numero2 = int(input("Digite número 2: "))

    resultado = numero1 / numero2

except ValueError:
    print("Debes escribir números")

except ZeroDivisionError:
    print("No puedes dividir entre cero")

else:
    print("Resultado:", resultado)

finally:
    print("Programa finalizado")

#Mini práctica
#Ejercicio 1
#Pedir un número entero.
#Si el usuario escribe texto:    Número inválido

try:
    numero = int(input("Digita un numero entero: "))

except ValueError:
    print("Debes digitar un numero entero")

else:
    print("Correcto, es un numero entero!")

finally:
    print("Programa finalizado!")

#Ejercicio 2
#Pedir dos números y dividirlos.
#Manejar:   ValueError    ZeroDivisionError

try:
    print("***DIVISON***")
    numero_1 = int(input("Digita primer numero para dividor: "))
    nuemro_2 = int(input("Digita segundo numero para dividir: "))

    operacion = numero_1 / nuemro_2

except ValueError:
    print("Error. Debes digitar numeros!")

except ZeroDivisionError:
    print("Error. No se puede dividir por cero!")

else:
    print("Resultado: ", operacion)

finally:
    print("Programa Finalizado")

#Ejercicio 3
#Usar else y finally.

#Ya los use!!!


#Mini reto
#Haz un programa que:
#Pida nombre y edad
#La edad debe ser número entero
#Si hay error, mostrar mensaje
#Si todo sale bien:      Hola Ricardo, tienes 30 años   
#Mostrar siempre:       Fin del sistema

nombre = str(input("Digita su nombre: "))

try:
    edad = int(input("Digita su edad: "))

except ValueError:
    print("Error la edad debe ser un numero entero!")

else: 
    print("Hola ", nombre, " tienes ",  edad, "años")
    #print(f"Hola {nombre}, tienes {edad} años") #Mejor version de print

finally:
    print("Fin del sistema")


#Ejemplo tipo “programa real”

while True:

    try:
        numero = int(input("Digite un número: "))

        print("El doble es:", numero * 2)
        break

    except ValueError:
        print("Error. Debe ingresar un número.")

#Obliga al usario a escribir correctamente


###########################################################################################
#Mini práctica extra (opcional)
#Haz un programa que:
#Pida un número
#Si el usuario escribe texto:  mostrar error
#Si el número es negativo: mostrar: El número debe ser positivo
#Si todo sale bien:  Número válido

try:
    numero = int(input("Digita un numero entero positivo: "))

    if numero <= 0:
        print("El numero debe ser positivo!")

    else:
        print("Numero valido!")

except ValueError:
    print("Error. Debe digitar un numero!")

Debes poner el if dentro del try.

¿Por qué funciona mejor?

Porque:

Primero Python intenta convertir el número
Si falla:
entra al except
Si sale bien:
recién ahí evalúa el if
Esto es MUY importante

Acabas de aprender algo clave:

El flujo del programa

En programación profesional, muchas veces el problema NO es la sintaxis…

sino:

el orden
la lógica
cuándo existe una variable
cuándo no
###################################################################################################
'''