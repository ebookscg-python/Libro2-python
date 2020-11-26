# -*- coding: utf-8 -*-
"""
Problema 4.30
@author: guardati
Prueba las funciones que determinan si una matriz es triangular inferior y la 
que determina si una matriz es triangular superior. 
"""

import matrices

matriz1 = [[1, 2, 3, 4], [0, 5, 6, 7], [0, 0, 8, 9], [0, 0, 0, 10]]
matriz2 = [[1, 0, 0, 0], [2, 3, 0, 0], [4, 5, 6, 0], [7, 8, 9, 10]]
matriz3 = [[0, 8, 0, 1], [2, 3, 7, 0], [4, 5, 0, 6], [0, 0, 9, 10]]
matriz4 = [[0, 8, 0, 1], [2, 3, 7, 0], [4, 5, 0, 6]]

# CP1: se proporciona una matriz triangular superior.
print(matrices.a_cadena(matriz1))
if matrices.es_triangular_superior(matriz1):
    print('CP1: La matriz es una matriz triangular superior.\n')

# CP2: se proporciona una matriz triangular inferior.
print(matrices.a_cadena(matriz2))
if matrices.es_triangular_inferior(matriz2):
    print('CP2: La matriz es una matriz triangular inferior.\n')

# CP3: se proporciona una matriz cuadrada que no es triangular.
print(matrices.a_cadena(matriz3))
if matrices.es_triangular_inferior(matriz3) or matrices.es_triangular_superior(matriz3):
    print('\nCP3: Es una matriz triangular inferior o superior.')
else:
    print('CP3: No es una matriz triangular.\n')
    
# CP4: se proporciona una matriz que no es cuadrada.
print(matrices.a_cadena(matriz4))
try:
    matrices.es_triangular_superior(matriz4)
except ValueError as error:
    print('CP4:', error)

