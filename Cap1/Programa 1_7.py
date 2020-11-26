# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 1.7
"""

def busca_copia_ordenada(elemento, lista):
    """ Busca el elemento en la lista, luego de generar una copia de esta con 
    todos sus elementos ordenados crecientemente.    
    Parámetro:
        lista: de tipo list. Formada por elementos del mismo tipo.
        elemento: dato del mismo tipo que los elementos de la lista.
    Regresa: 
        La posición del elemento en la lista o -1 si no lo encuentra.
    """     
    limite = len(lista)
    indice = 0
    copia = sorted(lista)
    while indice < limite and copia[indice] < elemento:
        indice += 1
    # Casos en los que elemento no está en la lista.
    if indice == limite or copia[indice] > elemento:  
        indice = -1
    return indice

# =============================================================================
# Algunas pruebas de la función busca_copia_ordenada()
# =============================================================================
# CP1: se proporciona una lista de nombres y un nombre que está en 
# la lista.
lista1 = ['David', 'Alicia', 'Dolores', 'Manuel', 'Clara']
posicion = busca_copia_ordenada('Manuel', lista1)
if posicion >= 0:
    print('\nCP1: Manuel está en la lista')
# CP2: se proporciona una lista de nombres y un nombre que, una vez 
# ordenada la lista, debería estar al inicio de esta.
posicion = busca_copia_ordenada('Alan', lista1)
if posicion >= 0:
    print('CP2: Alan está en la lista')
else:
    print('CP2: Alan no está en la lista') 
# CP3: se proporciona una lista de nombres y un nombre que, una vez 
# ordenada la lista, debería estar al final de esta.
posicion = busca_copia_ordenada('Samuel', lista1)
if posicion >= 0:
    print('CP3: Samuel está en la lista')
else:
    print('CP3: Samuel no está en la lista') 
# CP4: se proporciona una lista de nombres y un nombre que, una vez 
# ordenada la lista, debería estar en una posición intermedia de esta.
posicion = busca_copia_ordenada('Elena', lista1)
if posicion >= 0:
    print('CP4: Elena está en la lista')
else:
    print('CP4: Elena no está en la lista') 
# CP5: se proporciona una lista vacía y un nombre.
lista2 = []
posicion = busca_copia_ordenada('Jacinto', lista2)
if posicion >= 0:
    print('CP5: Jacinto está en la lista')
else:
    print('CP5: Jacinto no está en la lista') 
