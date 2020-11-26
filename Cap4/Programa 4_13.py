# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.16
Calcula e imprime la desviación estándard de un grupo de números.
"""

import array
import arreglo

datos = array.array('f')
n = int(input('\nIngrese total de números: '))
arreglo.lectura(datos, n, float, 'Ingrese un número: ')
try:
    ds = arreglo.desviacion_estandar(datos)
    print(f'\nLa desviación estándar es = {ds:.2f}')
except Exception as error:
    print('\nLa desviación estándar no se calculó:', error)

