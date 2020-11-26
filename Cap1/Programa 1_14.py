# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 1.14
"""


def calcula_long(frase):
    """ Genera una lista con la longitud de cada una de las
    palabras que forman la frase.
    Parámetro:
        frase: de tipo str. Las palabras están separadas por espacios en blanco.
    Regresa:
        Una lista de enteros.
    """
    return list(map(len, frase.split()))

# CP1: se proporciona una frase con varias palabras.
frase = 'Mi perro se llama Charrúa y es adorable'
print('\nCP1: frase con varias palabras -->', calcula_long(frase))
# CP2: se proporciona una frase con una sola palabra.
print('CP2: frase con una sola palabra -->', calcula_long('sol'))
# CP3: se proporciona una cadena vacía.
print('CP3: cadena vacía -->', calcula_long(''))