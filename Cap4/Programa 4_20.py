# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.23
Prueba la función que suma matrices del módulo matrices.
"""

import matrices

# CP1: se proporcionan matrices del mismo tamaño.
matriz1 = [[3, 5, 7], [2, 4, 6], [1, 1, 1]]
matriz2 = [[1, 2, 1], [5, 3, 2], [8, 0, 4]]
try:
    matriz_suma = matrices.suma_matrices(matriz1, matriz2)
    print(f'\nCP1 --> Matriz resultado\n{matrices.a_cadena(matriz_suma)}')
except IndexError as error:
    print(f'\nCP1 --> {error}')
# CP2: se proporcionan matrices de diferente tamaño.
matriz3 = [[6, 1, 7, 6], [1, 3, 5, 6], [3, 1, 9, 8]]
try:
    matriz_suma = matrices.suma_matrices(matriz1, matriz3)
    print(f'CP2: Matriz resultado\n {matrices.a_cadena(matriz_suma)}')
except IndexError as error:
    print(f'CP2 --> {error}')
# CP3: se proporcionan matrices vacías.
matriz4 = matrices.matriz_vacia()
matriz5 = matrices.matriz_vacia()
try:
    matriz_suma = matrices.suma_matrices(matriz4, matriz5)
    print(f'\nCP3 --> Matriz resultado\n {matrices.a_cadena(matriz_suma)}')
except IndexError as error:
    print(f'CP3 --> {error}')