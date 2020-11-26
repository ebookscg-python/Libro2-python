# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.1
"""

def obtiene_elemento(dic, clave):
    """ Regresa una tupla con el elemento del diccionario correspondiente
    a clave.    
    Parámetro:
        dic: de tipo dict.
        clave: representa una de las posibles claves del diccionario.
    Regresa:
        Una tupla formada por un ítem del diccionario (clave, valor).
    Lanza: 
        ValueError: si la clave no está en el diccionario.
    """
    valor = dic.get(clave)
    if valor == None:
        raise ValueError(f'La clave "{clave}" no está en el diccionario.')
    return clave, valor

# =============================================================================
# Algunas pruebas de la función obtiene_elemento()
# =============================================================================
num_meses = {'ene': 1, 'feb': 2, 'mar': 3, 'abr': 4, 'may': 5, 'jun': 6}
# CP1: se da una clave que está en el diccionario.
print('\nCP1:', obtiene_elemento(num_meses, 'abr'))
# CP2: se da una clave que no está en el diccionario.
try:
    print('CP2:', obtiene_elemento(num_meses, 'ago'))
except ValueError as error:
    print('CP2:', error)
# CP3: se da un diccionario vacío.
dic = {}
try:
    print('CP3:', obtiene_elemento(dic, 25))
except ValueError as error:
    print('CP3:', error)

