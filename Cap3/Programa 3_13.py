# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.13
"""

def consulta_clave_par(diccionario):
    """ Obtiene el total de claves que son números pares.
    Parámetro:
        diccionario: de tipo dict. Las claves deben ser numéricas.
    Regresa:
        La cantidad de claves que son números pares.
    """
    contador = 0
    for clave in diccionario:
        if clave % 2 == 0:
            contador += 1
    return contador


# CP1: se ingresa un diccionario con claves pares e impares.
dic1 = {2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
print('\nCP1:', consulta_clave_par(dic1))
# CP2: se ingresa un diccionario con claves impares.
dic2 = {15: 20, 21: 7, 13: 19, 43: 16, 5: 25}
print('CP2:', consulta_clave_par(dic2))
# CP3: se ingresa un diccionario vacío.
dic3 = dict()
print('CP3:', consulta_clave_par(dic3))