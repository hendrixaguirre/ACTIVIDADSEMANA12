# Ejemplificando creación de archivos en Python

#Declarar un objeto de tipo archivo
archi1=open("datos.txt","a")
archi1.write("Cuarta línea\n")
archi1.write("Quinta línea\n")
archi1.write("Sexta línea\n")
archi1.close()
print("Fin del programa")