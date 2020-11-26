# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.15
Obtiene e imprime la suma del producto de dos arreglos, recorriendo 
el primero de izquierda a derecha y el segundo de derecha a izquierda. 
"""

import array
import arreglo

def calcula_suma(x, y, n):
    """ Calcula y regresa la suma de los elementos del arreglo x (izq a der) 
    por los elementos del arreglo y (der a izq).
    """
    suma = 0
    for i in range(0, n):
        suma += x[i] * y[n - 1 - i]
    return suma

x = array.array('f')
y = array.array('f')
n = int(input('\nIngrese total de números: '))
print('\nIngrese los valores de x:'.upper())
arreglo.lectura(x, n, float, 'Ingrese un número: ')
print('\nIngrese los valores de y:'.upper())
arreglo.lectura(y, n, float, 'Ingrese un número: ')
suma = calcula_suma(x, y, n)
print(f'\nResultado de la sumatoria = {suma:.2f}')