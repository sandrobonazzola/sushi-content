#!/usr/bin/python3

"""
In questo programma impariamo ad interagire con
l'utente ed aggiungiamo un po' di logica
"""

print('Ciao, come ti chiami?')

nome = input()

print(
    "E` un piacere fare la tua conoscenza, " +
    nome
)

frutta = ('mela', 'pera', 'pesca')
bevande = ('the', 'cappuccino')

print('Cosa vuoi per merenda?')
ciboSceltoPerMerenda = input()
if ciboSceltoPerMerenda in frutta:
    print("Facciamo a meta'?")
elif ciboSceltoPerMerenda in bevande:
    print("Posso averne una tazza?")
else:
    print("Deve essere buono")
print("Premi invio per terminare")
input()
