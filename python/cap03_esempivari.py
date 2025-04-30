
##################################################################################################

# Calcolo area del cerchio
import math
def calcola_area_cerchio(raggio):
    return math.pi * (raggio ** 2)
raggio = 5
area = calcola_area_cerchio(raggio)
print(f"Area del cerchio con raggio {raggio}: {area:.2f}")

##################################################################################################

# Conversione temperatura
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
temperatura_celsius = 25
temperatura_fahrenheit = celsius_to_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C corrisponde a {temperatura_fahrenheit}°F")

##################################################################################################

# Programma semplice di input/output
def saluta_utente():
    nome = input("Inserisci il tuo nome: ")
    eta = input("Quanti anni hai? ")
    print(f"Ciao {nome}, hai {eta} anni!")

saluta_utente()
