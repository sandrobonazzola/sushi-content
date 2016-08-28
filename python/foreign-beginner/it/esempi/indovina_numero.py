#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
In questo programma giochiamo ad indovinare
un numero
"""

import random
numero_da_indovinare = random.randint(1, 20)

print('Ciao, come ti chiami?')
nome = input()
print("Bene, " + nome +
      ", sto pensando a un numero tra 1 e 20.")
print("Prova a indovinare! Hai 6 tentativi.")

tentativi = 0
while tentativi < 6:
    # Il rientro deve essere sempre fatto nello
    # stesso modo.
    # Puoi usare il tasto tab o 4 spazi a tua
    # scelta ma non puoi mescolare spazi e tab
    print('Dimmi un numero!')
    risposta = input()
    numero = int(risposta)  # input ritorna
    # una stringa, a noi serve un numero
    if numero < numero_da_indovinare:
        print("Sbagliato! Il numero è "
              "più grande!")
    elif numero > numero_da_indovinare:
        print("Sbagliato! Il numero è "
              "più piccolo!")
    else:
        print("Congratulazioni " + nome +
              ", hai indovinato!")
        break
    tentativi = tentativi + 1
else:
    print(
        'Mi dispiace, il numero che stavo '
        'pensando era ' +
        str(numero_da_indovinare)
    )
print('premi invio per chiudere')
input()
