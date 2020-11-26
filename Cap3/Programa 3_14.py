# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.14
"""

def busca_maximo_suma(diccionario):
    """ Obtiene el mayor valor luego de sumar los elementos
    clave y valor de un diccionario.
    Parámetro:
        diccionario: de tipo dict. Sus ítems deben estar formados
        por números.
    Regresa:
        El número más grande obtenido al sumar cada pareja: clave+valor.
    Lanza:
        ValueError: si el diccionario está vacío.    
    """
    if len(diccionario) >= 1:
        claves = list(diccionario.keys())
        valores = list(diccionario.values())
        suma = [c + v for c, v in zip(claves, valores)]
        return max(suma)
    raise ValueError('El diccionario está vacío.')
    
# CP1: se ingresa un diccionario con 4 ítems diferentes.
dic1 = {2: 4, 3: 9, 4: 16, 5: 25}
print('\nCP1:', busca_maximo_suma(dic1))
# CP2: se ingresa un diccionario con 3 ítems cuyas sumas dan el mismo valor.
dic2 = {15: 20, 5: 30, 13: 22}
print('CP2:', busca_maximo_suma(dic2))
# CP3: se ingresa un diccionario vacío.
dic3 = dict()
try:
    print('CP3:', busca_maximo_suma(dic3))
except ValueError as error:
    print('CP3:', error)

