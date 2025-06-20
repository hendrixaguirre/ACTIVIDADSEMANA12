# Cálculo de salario por empleado
print ("Programa para determinar el pago del empleado")

#Se definen las funciones
def descuento(num1,num2):
    return num1 * num2

def pagoFinal(num1,num2):
    return num1 - num2

# Se solicita la cantidad de empleados
n=int(input("Ingrese la cantidad de empleados: "))

#Ciclo que permita ingresar los datos de cada empleado
for i in range(n):
    print (f"Empleado {i+1}:")
    salarioBase=float(input("Ingrese el salario base del empleado: "))
    desc=descuento(salarioBase,0.10)
    print(f"El descuento de renta del vendedor es de: {desc:.2f}")
    pago=pagoFinal(salarioBase,desc)
    print(f"El total a pagar al empleado es de: {pago:.2f}")

print("Fin del programa")
