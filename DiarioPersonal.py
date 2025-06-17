#Programa que funciona como el diario personal del usuario
#Se importa el módulo de fecha y hora
from MODULOFECHA import mostrarfecha

#Se solicita al usuario que ingrese su entrada
entrada=input("Escribe tu entrada del diario: ")

#Se abre el archivo
with open("diario.txt","a", encoding="utf-8") as archivo:
    archivo.write(f"{mostrarfecha()} - {entrada}\n")

#Se confirma que la entrada fue guardada
print ("Su entrada fue guardada con éxito en 'diario.txt'.")