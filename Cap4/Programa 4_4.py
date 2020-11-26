# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.4
"""

import array

def suma_arre1(arreglo):
    """ Suma los elementos de un arreglo numérico.    
    Parámetro:
        arreglo: de tipo array. Almacena datos de tipo int o float.
    Regresa:
        La suma de los números contenidos en el arreglo.
    """
    suma = 0
    for num in arreglo:
        suma += num
    return suma

def suma_arre2(arreglo):
    """...
    """
    suma = 0
    for indice in range(0, len(arreglo)):
        suma += arreglo[indice]
    return suma

arre = array.array('f')
n = int(input('¿Cuántos números va a ingresar? '))
for i in range(0, n):
    arre.append(float(input(f'Ingrese el número {i + 1}: ')))
print(f'\nSuma por medio de la solución 1: {suma_arre1(arre):.2f}')
print(f'Suma por medio de la solución 2: {suma_arre2(arre):.2f}')


