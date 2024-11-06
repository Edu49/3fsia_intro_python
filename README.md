# Divisione tra due numeri

Implementiamo in python il seguente algoritmo, scritto in *pseudocodifica:*

```
scrivi "Inserisci il numeratore: "
leggi a
scrivi "Inserisci il denominatore: "
leggi b
se b != 0:
  divisione a / b
  scrivi "La divisione è: "
  scrivi divisione
altrimenti:
  scrivi "Errore: il denominatore non può essere zero."
```

In python l'algoritmo si scrive così

```
a = int(input("Inserisci il numeratore: "))
b = int(input("Inserisci il denominatore: "))

if b != 0:
    divisione = a / b
    print("La divisione è: ")
    print(divisione)
else:
    print("Errore: il denominatore non può essere zero.")
```
