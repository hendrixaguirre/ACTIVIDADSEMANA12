# Programa que abre un archivo y cuenta las líneas que posee

#Se solicita el nombre del archivo al usuario
nombre=input("Ingrese el nombre del archivo con terminación .txt: ")

try:
    with open(nombre,"r",encoding="utf-8") as archivo:
        lineas=archivo.readlines()
        cantidadLineas=len(lineas)
        print(f"El archivo contiene {cantidadLineas} líneas.")

except FileNotFoundError:
    print ("Error: el archivo no fue encontrado. "
           "Verifica el nombre del archivo e intenta de nueveichon!")