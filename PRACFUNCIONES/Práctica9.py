# Tabla de multiplicar
print ("")
print ("Programa para imprimir la tabla de multiplicar "
       "de un número dado")

#Se definen las funciones
def tabla(num1,num2):
    return num1 * num2

#Se solicita un número al usuario
n=int(input("Ingrese un número: "))
print (f"Tabla de multiplicar del número {n} es:")

for i in range(1,11): #Ciclo para multiplicar el número dado por i
    result=tabla(n,i)
    print (f"{n} * {i} = {result}")

print ("¡Fin del programa!")
