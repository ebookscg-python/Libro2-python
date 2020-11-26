# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 1.6
"""

def busca(elemento, lista):
    """ Busca el elemento en la lista.    
    Parámetro:
        lista: de tipo list. Formada por elementos del mismo tipo.
        elemento: dato del mismo tipo que los elementos de la lista.
    Regresa: 
        La posición (índice) del elemento en la lista o -1 si no lo encuentra.
    """ 
    indice = 0
    limite = len(lista)
    while indice < limite and lista[indice] != elemento:
        indice += 1
    if indice == limite:  # elemento no está en la lista
        indice = -1
    return indice

# =============================================================================
# Algunas pruebas de la función busca()
# =============================================================================
# CP1: se da una lista de nombres y un nombre que está en la lista.
lista1 = ['David', 'Alicia', 'Dolores', 'Manuel', 'Clara']
print('\nCP1 - ¿Manuel está en la lista? Posición =', busca('Manuel', lista1))
# CP2: se da una lista de nombres y un nombre que no está en la lista.
print('CP2 - ¿Pedro está en la lista? Posición =', busca('Pedro', lista1))
# CP3: se da una lista vacía y un nombre.
lista2 = []
print('CP3 - ¿Juan está en la lista? Posición =', busca('Juan', lista2))
