# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 2.10
"""

def quita_repetidos_y_ordena(lista):
    """ Genera una lista sin elementos repetidos y ordenada crecientemente.
    Parámetro:
        lista: de tipo list.
    Regresa:
        Una lista ordenada y sin elementos repetidos.
    """
    sin_repetidos = set(lista)
    ordenada = sorted(list(sin_repetidos))
    return ordenada

# CP1: se proporciona una lista con elementos repetidos y desordenados.
lis1 = [1, 5, 8, 1, 5, 7, 8, 7, 7, 9, 1]
res1 = quita_repetidos_y_ordena(lis1)
print('\nCP1: quita repetidos y ordena -->', res1)
# CP2: se proporciona una lista sin repetidos y ordenada.
lis2 = ['a', 'e', 'i', 'o', 'u']
res2 = quita_repetidos_y_ordena(lis2)
print('CP2: sin cambios -->', res2)
# CP3: se proporciona una con todos sus elementos iguales.
lis3 = [23, 23, 23, 23, 23, 23, 23]
res3 = quita_repetidos_y_ordena(lis3)
print('CP3: queda un elemento -->', res3)
# CP4: se proporciona una lista vacía.
lis4 = []
res4 = quita_repetidos_y_ordena(lis4)
print('CP4: lista vacía -->', res4)



