#Devolver el número menor
print("Programa que devuelve el menor de los reales")

#Se definen las funciones
def menorTres(a,b,c):
    menor=a
    if b<menor:
        menor=b
    if c<menor:
        menor=c
    return menor

n1=float(input("Digite el primer número: "))
n2=float(input("Digite el segundo número: "))
n3=float(input("Digite el tercer número: "))

result=menorTres(n1,n2,n3)
print(f"El menor de los números reales es: {result:.2f}")