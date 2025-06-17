#Programa que funciona como el diario personal del usuario

#Se importa el módulo de fecha y hora
from datetime import datetime
def mostrarfecha():
    ahora=datetime.now()
    fecha=ahora.strftime("%d-%m-%Y")
    hora=ahora.strftime("%H:%M")
    return (f"Fecha: {fecha}. Hora: {hora}.")
mostrarfecha()