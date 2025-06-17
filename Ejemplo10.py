#Programa que pide al usuario un nombre de archivo de texto
# y permite almacenar frases como el usuario desee

nombrearchi=input("Ingrese el nombre del archivo: ")
archi1=open(nombrearchi,"a")
cantlin=int(input("Ingrese la cantidad de frases que desea agregar: "))
lista=[]
for i in range(1,cantlin+1):
    elementos=input(f"Ingrese el elemento {i}: ")
    lista.append(elementos)

with open(nombrearchi,"w", encoding="utf-8") as archivo:
    archivo.writelines(lista)