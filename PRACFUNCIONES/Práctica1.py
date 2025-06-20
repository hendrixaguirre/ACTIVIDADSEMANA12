#Función que determina el porcentaje
def porcentaje(porcen,presu):
    return porcen * presu

#Programa que determina el porcentaje que le corresponde a cada departamento
print ("Programa para determinar el porcentaje de dinero "
       "que le corresponde a cada departamento en una fábrica")
print("Porcentajes por departamentos:")
print ("Recursos Humanos: 50%. "
       "Manufactura: 25%. "
       "Empaquetado: 15%. "
       "Publicidad: 10%. ")

recur=0.50
manu=0.25
empa=0.15
publi=0.10
presu=float(input("Digite el presupuesto anual de la fábrica en dólares:"))

#Se realiza el cálculo
porcentaje1=porcentaje(recur,presu)
print ("El porcentaje de dinero que le corresponde a "
       "Recursos Humanos es de: ", porcentaje1)

porcentaje2=porcentaje(manu,presu)
print ("El porcentaje de dinero que le corresponde a "
       "Manufactura es de: ",porcentaje2)

porcentaje3=porcentaje(empa,presu)
print ("El porcentaje de dinero que le corresponde a "
       "Empaquetado es de: ",porcentaje3)

porcentaje4=porcentaje(publi,presu)
print ("El porcentaje de dinero que le corresponde a "
       "Publicidad es de: ",porcentaje4)

