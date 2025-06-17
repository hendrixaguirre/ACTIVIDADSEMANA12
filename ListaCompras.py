# Programa que genera una lista de compras
with open("compras.txt","w",encoding="utf-8") as archivo:
    while True:
        prod=input("Ingrese el nombre del producto (o escribe 'fin' para terminar):")
        if prod.lower() == "fin":
            break
        archivo.write(prod + "\n")
print ("La lista de compras ha sido guardada en 'compras.txt!'1")