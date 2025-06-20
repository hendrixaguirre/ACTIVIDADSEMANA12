# Factorial de número capturado por el teclado

#Se definen las funciones
def calFac(num):
    factorial=1
    for i in range(1,num+1):
        factorial *=i
    return factorial
    
n=int(input("Ingrese un número para calcular su factorial: "))

if n>0:
    result=calFac(n)
    print(f"El factorial de {n} es: {result}")
else: 
    print ("El número no es válido")

print ("")
print ("Fin del programa")