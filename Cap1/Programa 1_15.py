# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 1.15
"""

def mezcla(lista1, lista2):
    """ Genera una lista de tuplas formadas por elementos de las listas.
    Parámetros:
        lista1: de tipo list.
        lista2: de tipo list.
    Regresa:
        Una lista de tuplas con elementos de las listas tomados de 
        manera alternada.
    """
    return list((x, y) for x, y in zip(lista1[::2], lista2[1::2]))

# CP1: se proporcionan dos listas de enteros de igual longitud.
l1 = list(range(1, 20, 2))
l2 = list(range(2, 21, 2)) 
print('\nCP1: listas de igual longitud -->', mezcla(l1, l2))
# CP2: se proporcionan dos listas de cadenas de diferentes longitudes.
l3 = list('electroencefalografista')
l4 = list('extraterritorialidad'.upper())
print('CP2: listas de diferentes longitudes -->', mezcla(l3, l4))
# CP3: se proporcionan dos listas vacías.
print('CP3: listas vacías -->', mezcla([], []))
# CP4: se proporcionan dos listas de datos de diferente tipo.
print('CP4: listas de diferente tipo -->', mezcla(l1, l3))