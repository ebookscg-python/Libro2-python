# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.22
Prueba las funciones del módulo matrices que buscan y regresan la posición del: 
    - elemento más grande de una fila 
    - elemento más grande una columna 
"""

import matrices

filas = int(input('\nIngrese total de filas: '))
columnas = int(input('Ingrese total de columnas: '))
print('\nIngrese los datos del arreglo'.upper())
matriz1 = matrices.forma_matriz_3(filas, columnas)
matrices.lee(matriz1, int)

# Se dan datos correctos. Por razones de espacio no se usa try-except.
max_f = matrices.max_fila(matriz1, filas - 1)
print(f'\nCP1 --> El máximo de la última fila está en la posición {max_f}')
max_c = matrices.max_columna(matriz1, 0)
print(f'CP2 --> El máximo de la primera columna está en la posición {max_c}')

# Se utiliza un arreglo vacío.
matriz2 = matrices.matriz_vacia()  
try:
    max_f = matrices.max_fila(matriz2, filas - 1)
    print(f'\nCP3 --> El máximo de la última fila está en la posición {max_f}')
except IndexError as error:
    print(f'\nCP3 --> {error}')  
try:
    max_c = matrices.max_columna(matriz2, 0)
    print(f'\nCP4 --> El máximo de la primera columna está en la posición {max_c}')   
except IndexError as error:
    print(f'CP4 --> {error}')

    