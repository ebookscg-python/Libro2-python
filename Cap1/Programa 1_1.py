# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 1.1
"""

def primero_y_ultimo(lista):
    """ Obtiene el primero y el último elemento de la lista.    
    Parámetro:
        lista: de tipo list.
    Regresa: 
        Una tupla formada con el primero y el último elemento de la lista.
    Lanza:
        ValueError: cuando el parámetro recibido no es una lista o cuando no 
        tiene, al menos, 2 elementos.
    """
    if lista:
        if len(lista) >= 2:
            return (lista[0], lista[-1])
        raise ValueError('La lista no tiene elementos suficientes.')
    raise ValueError('No es un dato válido.')

# =============================================================================
# Algunas pruebas para la función primero_y_ultimo()
# =============================================================================
# CP1: lista con varios elementos.
lista1 = [1, 2, 3, 4]
print('\nCP1:', primero_y_ultimo(lista1))

# CP2: lista con solo 2 elementos.
lista2 = [1, 2]
print('CP2:', primero_y_ultimo(lista2))
# CP3: lista con 1 solo elemento. 
lista3 = [1]
try: 
    print('CP3:', primero_y_ultimo(lista3))
except Exception as error:
    print('CP3:', error)
# CP4: No se proporciona una lista.
lista4 = None
try:
    print('CP4:', primero_y_ultimo(lista4))
except Exception as error:
    print('CP4:', error)