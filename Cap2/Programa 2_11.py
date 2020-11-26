# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 2.11
"""

def diferencia_subconjunto(conjunto1, conjunto2):
    """ Le quita al segundo conjunto los elementos del primero,
    solo si el primero es un subconjunto del segundo.
    Parámetros:
        conjunto1: de tipo set.
        conjunto2: de tipo set.
    """
    if conjunto1.issubset(conjunto2):
        conjunto2 -= conjunto1
      
# CP1: se proporcionan un conjunto y un subconjunto de este.
c1 = {1, 3, 5, 7, 9}      
c2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
diferencia_subconjunto(c1, c2)
print('\nCP1: conjunto y subconjunto -->', c2)
# CP2: se proporcionan dos conjuntos iguales.
c3 = {'a', 'e', 'i', 'o', 'u'}
c4 = {'o', 'e', 'i', 'a', 'u'}
diferencia_subconjunto(c3, c4)
print('CP2: dos conjuntos iguales -->', c4)
# CP3: se proporcionan un conjunto y un subconjunto vacío.
vacio = set()
diferencia_subconjunto(vacio, c3)
print('CP3: conjunto y uno vacío -->', c3)
# CP4: se proporcionan dos conjuntos sin relación entre ellos.
diferencia_subconjunto(c1, c3)
print('CP4: dos conjuntos sin relación -->', c3)

