#Importe a pagar
print("Programa para determinar el total a pagar en una compra")

#Se definen las funciones
def importe(num):
    if num>=300 and num<=499:
        print ("Usted tiene un descuento del 5%")
        descuento=num*0.05
    
    if num>=500 and num<=699:
        print ("Usted tiene un descuento del 10%")
        descuento=num*0.10
        
    if num>=700:
        print ("Usted tiene un descuento del 12%")
        descuento=num*0.12
    
    importefin=num - descuento
    return importefin

#Se solicita el importe de la compra
n=float(input("Ingrese el importe inicial de su compra: "))
totalpago=importe(n)
print (f"El importe final con descuento es de: {totalpago:.2f}")

print("")
print ("Fin del programa")