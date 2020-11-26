# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.20
Prueba las funciones que suman filas y columnas del módulo matrices.
"""

import matrices

filas = int(input('\nIngrese total de filas: '))
columnas = int(input('Ingrese total de columnas: '))
matriz = matrices.forma_matriz_1(filas, columnas)
matrices.lee(matriz, int)

# Se dan datos correctos. Por razones de espacio no se usa try-except
suma_fila = matrices.suma_fila(matriz, 1)
print(f'\nCP1 --> Suma de la segunda fila = {suma_fila}')
suma_columna = matrices.suma_columna(matriz, columnas - 1)
print(f'CP2 --> Suma de la última columna = {suma_columna}')

# Se dan datos fuera del rango del arreglo.
try:
    suma_fila = matrices.suma_fila(matriz, 11)
except IndexError as error:
    print(f'\nCP3 --> {error}')
except TypeError as error:
    print(f'\nCP3 --> {error}')
else:
    print(f'\nCP3 --> Suma de la segunda fila = {suma_fila}')
try:
    suma_columna = matrices.suma_columna(matriz, columnas + 1)
except IndexError as error:
    print(f'CP4 --> {error}')
except TypeError as error:
    print(f'CP4 --> {error}')
else:
    print(f'CP4 --> Suma de la última columna = {suma_columna}')    
    

