#Archivos
#Crear archivo.txt
#archivo = open("E:\Python 2026 RLP\mensaje.txt", "w")
#archivo.write("Hola Ricardo Ladino Pedraza")
#archivo.close()

#Leer archivo
#archivo = open("E:\Python 2026 RLP\mensaje.txt", "r")
#contenido = archivo.read()
#print(contenido)
#archivo.close()

#agregar informacion
#archivo = open("E:\Python 2026 RLP\mensaje.txt", "a")
#archivo.write("\nNueva linea")
#archivo.close()
'''
#Ejercicio1

archivo = open("E:\Python 2026 RLP\mensaje1.txt", "w")
archivo.write("Hola mundo, estoy aprendiendo Python")
archivo.close()

#Ejercicio2
archivo = open("E:\Python 2026 RLP\prueba1.txt", "w")
nombre = input(str("Digita nombre: "))

archivo = open("E:\Python 2026 RLP\prueba1.txt", "a")
archivo.write(nombre)
archivo.close()

#Ejercicio3
archivo = open("E:\Python 2026 RLP\inventario.txt", "w")

producto = input(str("Escribir producto: "))
precio = input(str("Escribir precio de producto: "))

archivo = open("E:\Python 2026 RLP\inventario.txt", "a")
#archivo.write(producto + " - " + precio) #dos manera de imprimir 1
#archivo.write(precio)
archivo.write(f"{producto} - {precio}\n") # y 2
archivo.close()

#Mini reto
archivo = open("E:\Python 2026 RLP\mnotas.txt", "a")

nota = input(str("Escribir nota: "))
archivo.write("\nnota agregada: ")
archivo.write(nota)
archivo.close()
'''

#Mini reto extra
archivo = open("E:/Python 2026 RLP/inventario_1.txt", "a") 
#ojo con cambiar \ por / en ruta de archivo. evitar problemas de sintaxis

while True:
    producto = input(str("Escribir producto (o escribe 'salir'): "))
            
    if producto == 'salir':
       break

    precio = input(str("Escribir precio de producto: "))
    archivo.write(f"{producto} - {precio}\n") 

archivo.close() #se debe cerrar el archivo de escritura o adicion, depues abrir y volver a cerrar
archivo = open("E:/Python 2026 RLP/inventario_1.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()



