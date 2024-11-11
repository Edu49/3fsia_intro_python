#Programma che chiede in input due numeri e calcola il quoziente

a = float(input("Inserisci il numeratore: "))
b = float(input("Inserisci il denominatore: "))

if b != 0:
    divisione = a / b
    print(f"La divisione è: {divisione} ")
else:
    print("Errore: il denominatore non può essere zero.")
