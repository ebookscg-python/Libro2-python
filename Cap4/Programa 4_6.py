# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.7: algunas pruebas de la función de búsqueda
que se encuentra en el módulo arreglo.
"""

import array
import arreglo

letras = array.array('u', 'tres tristes tigres, tragaban trigo en un trigal')
numeros = array.array('i')

# CP1: se busca en un arreglo con varias ocurrencias del dato.
print('\nCP1: posiciones de la "t":', arreglo.busca_todos(letras, 't'))
# CP2: se busca en un arreglo con una ocurrencia del dato.
print('CP2: posiciones de la "u":', arreglo.busca_todos(letras, 'u'))
# CP3: se busca en un arreglo que no contiene al dato.
print('CP3: posiciones de la "p":', arreglo.busca_todos(letras, 'p'))
# CP4: se busca en un arreglo vacío.
print('CP4: posiciones del "12":', arreglo.busca_todos(numeros, 12))
