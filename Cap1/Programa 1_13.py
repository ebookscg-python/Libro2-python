# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 1.13
"""

def lista_filtrada(lista):
    """ Genera una lista con todos los elementos de la lista 
    recibida que tengan un valor.
    Parámetro:
        lista: de tipo list. Almacena cualquier tipo de datos.
    Regresa:
        Una lista formada solo con elementos no vacíos.
    """
    return list(filter(None, lista))

# CP1: se proporciona una lista de cadenas con algunas cadenas vacías.
lis_cadenas = ['verde', 'azul', '', 'rojo', '', '', 'blanco']
filtrada1 = lista_filtrada(lis_cadenas)
print('\nCP1: lista de cadenas -->', filtrada1)
# CP2: se proporciona una lista de números con algunos 0.
lis_numeros = [23, 0, 17, 15, 0, 0, 56]
filtrada2 = lista_filtrada(lis_numeros)
print('CP2: lista de números -->', filtrada2)
# CP3: se proporciona una lista de tuplas, algunas de las cuales están vacías. 
lis_tuplas = [(2, 4), (), (3, 9), (), (), (), (8, 64)]
filtrada3 = lista_filtrada(lis_tuplas)
print('CP3: lista de tuplas -->', filtrada3)
# CP4: se proporciona una lista de listas, algunas de las cuales están vacías. 
lis_listas = [[], [], ['sol', 'luna'], [35.6], [], [2, 80]]
filtrada4 = lista_filtrada(lis_listas)
print('CP4: lista de listas -->', filtrada4)
# CP5: se proporciona una lista vacía. 
vacia = []
filtrada5 = lista_filtrada(vacia)
print('CP5: lista vacía -->', filtrada5)

