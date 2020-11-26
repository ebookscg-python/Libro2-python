# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.27
Prueba la función que genera la traspuesta de una matriz.
"""

import matrices

# CP1: se proporciona una matriz de 4 x 4.
matriz1 = [[7, 4, 2, 8], [3, 4, 7, 6], [1, 1, 1, 1], [4, 6, 0, 9]]
trasp1 = matrices.traspuesta(matriz1)
cadm1 = matrices.a_cadena(matriz1)
cadt1 = matrices.a_cadena(trasp1)
print(f'\nCP1 --> Matriz:\n{cadm1}\nMatriz traspuesta:\n{cadt1}')
# CP2: se proporciona una matriz 3 x 4. 
matriz2 = [[6, 1, 7, 6], [1, 3, 5, 6], [3, 1, 9, 8]]
trasp2 = matrices.traspuesta(matriz2)
cadm2 = matrices.a_cadena(matriz2)
cadt2 = matrices.a_cadena(trasp2)
print(f'CP2 --> Matriz:\n{cadm2}\nMatriz traspuesta:\n{cadt2}')
# CP3: se proporciona una matriz vacía.
matriz3 = matrices.matriz_vacia()
trasp3 = matrices.traspuesta(matriz3)
cadm3 = matrices.a_cadena(matriz3)
cadt3 = matrices.a_cadena(trasp3)
print(f'CP3 --> Matriz:\n{cadm3}\nMatriz traspuesta:\n{cadt3}')
# CP4: se proporciona una matriz de 2 x 3 de tipo str.
matriz4 = [['d', 'g', 'p'], ['b', 'x', 't']]
trasp4 = matrices.traspuesta(matriz4)
cadm4 = matrices.a_cadena(matriz4)
cadt4 = matrices.a_cadena(trasp4)
print(f'CP4 --> Matriz:\n{cadm4}\nMatriz traspuesta:\n{cadt4}')