#Ejemplificar lectura de un archivo

#Crear la variable para manipular el archivo
archi1=open("datos.txt","r+", encoding="utf-8")
contenido=archi1.read()
print (contenido)
archi1.write("Otra línea 1\n")
archi1.write("Otra línea 2\n")
archi1.close()
