# Compañia de seguros

#Primero se establecen las funciones
def calComision(num1,num2,num3):
    totalVentas=num1+num2+num3
    comision=totalVentas*0.10
    return comision

def Totsemana(num1,num2):
    return num1 + num2

n=int(input("Ingrese la cantidad de vendedores: ")) #Se solicita la cantidad de vendedores

for i in range(n):
    print (f"Vendedor {i+1}:")
    sueldoBase=float(input("Ingrese el sueldo base del vendedor: "))
    venta1=float(input("Ingrese el valor de la primera venta: "))
    venta2=float(input("Ingrese el valor de la segunda venta: "))
    venta3=float(input("Ingrese el valor de la tercera venta: "))
    
    comi=calComision(venta1,venta2,venta3)
    totalSemana=Totsemana(sueldoBase,comi)

    print (f"El total de comisión por ventas es de: {comi:.2f}")
    print (f"El total de la semana es: {totalSemana:.2f}")

print ("Fin de programa")
