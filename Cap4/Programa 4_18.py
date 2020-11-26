# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.21
Prueba las funciones que suman los elementos de las diagonales
principal y secundaria del módulo matrices.
"""

import matrices

filas = int(input('\nIngrese total de filas: '))
columnas = int(input('Ingrese total de columnas: '))
print('\nIngrese los datos del arreglo'.upper())
matriz1 = matrices.forma_matriz_2(filas, columnas)
matrices.lee(matriz1, int)

# Se dan datos correctos. Por razones de espacio no se usa try-except.
suma_principal = matrices.suma_diagonal_principal(matriz1)
print(f'\nCP1 --> Suma de la diagonal principal = {suma_principal}')
suma_secundaria = matrices.suma_diagonal_secundaria(matriz1)
print(f'CP2 --> Suma de la diagonal secundaria = {suma_secundaria}')

# Se utiliza un arreglo que no es cuadrado.
print('\nIngrese los datos del arreglo'.upper())
columnas = filas + 2  # Asegura no ser cuadrada.
matriz2 = matrices.forma_matriz_2(filas, columnas)  
matrices.lee(matriz2, int)
try:
    suma_principal = matrices.suma_diagonal_principal(matriz2)
    print(f'\nCP3 --> Suma de la diagonal principal = {suma_principal}')
except IndexError as error:
    print(f'\nCP3 --> {error}')
try:
    suma_secundaria = matrices.suma_diagonal_secundaria(matriz2)
    print(f'\nCP4 --> Suma de la diagonal secundaria = {suma_secundaria}')    
except IndexError as error:
    print(f'CP4 --> {error}')




