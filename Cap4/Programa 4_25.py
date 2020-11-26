# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.28
Prueba la función que multiplica matrices del módulo matrices.
"""

import matrices

# CP1: se proporcionan matrices que pueden multiplicarse (2 x 3 y 3 x 4).
matriz1 = [[4, 2, 5], [6, 3, 1]]
matriz2 = [[7, 1, 2, 4], [3, 4, 6, 1], [2, 5, 3, 2]]
try:
    matriz_multi1 = matrices.multiplica_matrices(matriz1, matriz2)
    print(f'\nCP1: Matriz resultado\n{matrices.a_cadena(matriz_multi1)}')
except Exception as error:
    print(f'\nCP1 --> {error}')
# CP2: se proporcionan matrices que pueden multiplicarse (3 x 3 y 3 x 3).
matriz3 = [[3, 5, 7], [2, 4, 6], [1, 4, 8]]
matriz4 = [[1, 2, 1], [5, 3, 2], [8, 0, 4]]
try:
    matriz_multi2 = matrices.multiplica_matrices(matriz3, matriz4)
    print(f'CP2: Matriz resultado\n{matrices.a_cadena(matriz_multi2)}')
except Exception as error:
    print(f'CP2 --> {error}')
# CP3: se proporcionan matrices que no pueden multiplicarse (3 x 4 y 3 x 3).
try:
    matriz_multi3 = matrices.multiplica_matrices(matriz2, matriz3)
    print(f'CP3: Matriz resultado\n{matrices.a_cadena(matriz_multi3)}')
except Exception as error:
    print(f'CP3 --> {error}')
# CP4: se proporcionan matrices vacías.
matriz4 = matrices.matriz_vacia()
matriz5 = matrices.matriz_vacia()
try:
    matriz_multi4 = matrices.multiplica_matrices(matriz4, matriz5)
    print(f'CP4: Matriz resultado\n {matrices.a_cadena(matriz_multi4)}')
except Exception as error:
    print(f'CP4 --> {error}')