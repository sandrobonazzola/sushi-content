#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
In questo programma giochiamo ad evitare il drago
"""

import random
import time


def descriviLaSituazione():
    """
    Stampa a video l'introduzione al gioco
    """
    # qui sotto usiamo una stringa multilinea
    # invece di scrivere tante print.
    print(
        """
        Sei in un mondo pieno di dragoni.
        Di fronte a te, vedi due caverne.
        In una caverna il dragone è amichevole
        e dividerà con te il suo tesoro.
        Nell'altra caverna il dragone è affamato
        e arrabbiato e ti mangerà in un boccone.
        """
    )


def scegliCaverna():
    """
    Chiede all'utente di scegliere la caverna
    1 o 2.
    Controlla cosa ha risposto l'utente e se la
    risposta è valida la ritorna al chiamante.
    """
    caverna = ''
    while caverna not in ('1', '2'):
        print("In quale caverna vuoi entrare? "
              "(1 o 2)")
        caverna = input()
    # il comando return permette di passare
    # caverna ad una variabile. In questo modo,
    # "c = scegliCaverna()" funziona
    # in modo simile a "caverna = input()"
    return caverna


def controllaCaverna(caverna_scelta):
    """
    Controlla se la caverna_scelta è quella con
    il dragone buono o quella con il dragone
    cattivo e scrive a video cosa succede.
    """
    print('Ti avvicini alla caverna...')
    time.sleep(2)  # attende 2 secondi
    # crea suspense...
    print("E' buio e pauroso...")
    time.sleep(2)
    print("Un grosso dragone salta fuori "
          "di fronte a te! "
          "Apre le sue fauci e...")
    print()
    time.sleep(2)
    caverna_buona = random.randint(1, 2)
    if caverna_scelta == caverna_buona:
        print("Ti dà il suo tesoro!")
    else:
        print("Ti mangia in un boccone!")


giocaAncora = 'si'
while giocaAncora == 'si':
    descriviLaSituazione()
    caverna = scegliCaverna()
    controllaCaverna(caverna)
    print('Vuoi giocare ancora? (si o no)')
    giocaAncora = input()
