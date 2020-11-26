# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.18
Obtiene e imprime todos los números primos comprendidos entre 
2 y n inclusive, por medio del método llamado Criba de Eratóstenes. 
"""

import array

def criba_eratostenes(n):
    """ Encuentra los números primos comprendidos entre 2 y n.
    Parámetro:
        n: de tipo int. Límite hasta el que se buscarán números primos.
    Regresa:
        Una lista con los números primos.
    """
    lim = n + 1
    primos = array.array('B')
    primos.append(0)  # Valor 0 para las 2 primeras casillas.
    primos.append(0)    
    for _ in range(2, lim):  # Valor 1 para las otras casillas.  
        primos.append(1)
    for i in range(2, lim):
        if primos[i]:
            for j in range(i + 1, lim):
                if primos[j] and j % i == 0:
                    primos[j] = 0
    res = [i for i in range(2, lim) if primos[i]]
    return res

n = int(input('\n¿Hasta qué valor se buscarán números primos? '))
res = criba_eratostenes(n)
print(f'\nLos números primos <= {n} son:'.upper(), res)