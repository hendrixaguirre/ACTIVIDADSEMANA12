# Programa principal

#Importar módulo
import Módulos as md
from Módulos import resta,suma
from Módulos import div,producto,modulo
print ("Programa con las operaciones básicas")
num1=int(input("Ingresa un número: "))
num2=int(input("Ingresa otro número: "))
print(f"La resta es: {md.resta(num1,num2)}")
respuesta=div(num1,num2)
print ("El resultado de la división es:",respuesta)
print(md.texto)
respuesta1=producto(num1,num2)
print ("El producto de la mulltiplicación es:",respuesta1)
respuesta2=modulo(num1,num2)
print ("El módulo de la división es:",respuesta2)
respuesta3=suma(num1,num2)
print ("La suma de los dos números es:",respuesta)