# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 2.8
"""

def conjunto_tuplas(lista1, lista2):
    """ Genera un conjunto de tuplas con pares de elementos de las listas.
    Parámetros:
        lista1: de tipo list.
        lista2: de tipo list.
    Regresa:
        Un conjunto formado por tuplas de pares de elementos de las listas.
    Lanza:
        ValueError: si las listas tienen distinta longitud.
    """        
    if len(lista1) != len(lista2):
        raise ValueError('Listas de diferente longitud.')
    mezcla = zip(lista1, lista2)
    return set(mezcla)

# CP1: se proporcionan dos listas de igual longitud.
l1 = list('aeiou')
l2 = list('AEIOU')
print('\nCP1:', conjunto_tuplas(l1, l2))
# CP2: se proporcionan dos listas vacías.
l3 = []
l4 = []
print('CP2:', conjunto_tuplas(l3, l4))
# CP3: se proporcionan dos listas de distinto tamaño.
l5 = [12, 35, 78]
try:
    print('CP3:', conjunto_tuplas(l1, l5))
except ValueError as error:
    print('CP3:', error)

