# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.26
Prueba la función que determina si una matriz es simétrica.
"""

import matrices

# CP1: se proporciona una matriz simétrica.
matriz1 = [[7, 3, 2, 8], [3, 4, 5, 6], [2, 5, 3, 1], [8, 6, 1, 9]]
if matrices.es_simetrica(matriz1):
    print('\nCP1: la matriz es simétrica.')
else:
    print('\nCP1: la matriz no es simétrica.')
# CP2: se proporciona una matriz que no es simétrica.
matriz2 = [[7, 1, 2, 8], [3, 4, 5, 6], [2, 5, 3, 1], [4, 6, 1, 9]]
if matrices.es_simetrica(matriz2):
    print('CP2: la matriz es simétrica.')
else:
    print('CP2: la matriz no es simétrica.')    
# CP3: se proporciona una matriz que no es cuadrada (tampoco simétrica).  
matriz3 = [[6, 1, 7, 6], [1, 3, 5, 6], [3, 1, 9, 8]]
if matrices.es_simetrica(matriz3):
    print('CP3: la matriz es simétrica.')
else:
    print('CP3: la matriz no es simétrica.')
# CP4: se proporciona una matriz vacía.
matriz4 = matrices.matriz_vacia()
if matrices.es_simetrica(matriz4):
    print('CP4: la matriz es simétrica.')
else:
    print('CP4: la matriz no es simétrica.')