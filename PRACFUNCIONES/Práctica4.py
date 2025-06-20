# Determinar pago mediante horas trabajadas

#Se definen las funciones
def pago(num1,num2):
    return num1 * num2

def horas(num1,num2):
    return num1 - num2

def sumapago(num1,num2):
    return num1 + num2

#Se solicita la cantidad de trabajadores
n=int(input("Ingrese la cantidad de trabajadores: "))

#Ciclo que permita ingresar las horas laboradas
for i in range(n):
    print (f"Trabajador {i+1}:")
    horas_lab=int(input("Ingrese las horas laboradas: "))
    if horas_lab<=160:
        pagot=pago(horas_lab,6.5)
        print (f"El total a pagar al trabajador es de: {pagot:.2f}")
    else:
        if horas_lab>160:
            horasextra=horas(horas_lab,160)
            pagoextra=pago(horasextra,7.5)
            horassinextra=horas(horas_lab,horasextra)
            pagosinextra=pago(horassinextra,6.5)
            pagototal=sumapago(pagoextra,pagosinextra)
            print (f"El total a pagar al trabajador es de: {pagototal:.2f}")

print ("Fin del programa")