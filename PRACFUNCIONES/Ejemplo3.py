# Ejemplo 3
#Promedio de tres notas
def prom():
    nota1=int(input("Ingrese la primera nota:"))
    nota2=int(input("Ingrese la segunda nota:"))
    nota3=int(input("Ingrese la tercera nota:"))
    resultado=(nota1+nota2+nota3)/3
    return resultado
promedio=prom()
print ("El promedio de las notas es:",promedio)
