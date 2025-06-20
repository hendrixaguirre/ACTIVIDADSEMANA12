# Área de un círculo
print ("Programa que calcula el área de un círculo")
print ("---------------------------------------------------")
#Se definen las funciones 
def area(num1):
    return 3.1416 * (num1**2)

#Se solicita el radio del círculo
radio=float(input("Digite el radio del círculo en centímetros: "))
areac=area(radio)
print (f"El área del círculo es de: {areac:.2f} centímetros")
print ("")
print ("Fin del programa")
