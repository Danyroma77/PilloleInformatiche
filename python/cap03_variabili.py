# Assegnazione base
eta = 25
nome = "Carlo"
# Regole di denominazione
# Valido
_nome_utente = "Giovanni"
nome2 = "Marco"
# Non valido (genererebbe errore)
# 2nome = "Errore"
# nome-utente = "Errore"
# Tipizzazione dinamica
variabile = 10  # Intero
variabile = "Ora sono una stringa"  # Ora è una stringa
# Variabili mutabili e immutabili
# Mutabile (lista)
lista_numeri = [1, 2, 3]
lista_numeri.append(4)  # Modificabile
# Immutabile (tupla)
coordinate = (10, 20)
# coordinate[0] = 15  # Genererebbe un errore
# Scope delle variabili
x = 10  # Variabile globale
def esempio_funzione():
    x = 20  # Variabile locale
    print("Dentro la funzione:", x)
esempio_funzione()
print("Fuori dalla funzione:", x)
