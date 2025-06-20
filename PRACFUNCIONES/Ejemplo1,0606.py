#Función que permite obtener el producto de 2 #
def producto(num1,num2):
    return num1 * num2 

# Multiplicar 2 #
numero1=int(input("Digite un número: "))
numero2=int(input("Digite otro número: "))
resp=producto(numero1,numero2)
print (numero1, "*", numero2, "=", resp)

#Obtener la tabla de multiplicar de un #
num=int(input("Escriba un número: "))
for i in range(1,13):
    r=producto(num,i)
    print (num, "*", i, "=", r)

#Mostrar el nombre completo de una persona
def NomCom(nombre,apellido):
    return print ("El nombre completo de la persona es:",nombre,"",apellido,"")

#Leer el nombre de la persona
nom=input("Ingrese su nombre: ")
apelli=input("Ingrese su apellido: ")
nomcomple=NomCom(nom,apelli)