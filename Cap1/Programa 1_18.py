# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 1.18
"""

def uno_y_uno(lista1, lista2, separador):
    """ Genera una nueva lista mezclando los elementos
    de las listas dadas y separador por los caracteres almacenados en separador.
    Parámetros:
        lista1: de tipo list.
        lista2: de tipo list.
        separador: de tipo str. Se utiliza para separar pares de elementos.
    Regresa:
        Una lista de cadenas.
    """
    return list(str(el1) + separador + str(el2) for el1, el2 in zip(lista1, lista2))

  

def todos_con_todos(lista1, lista2, separador):
    """ Genera una nueva lista mezclando cada elemento de lista1
    con cada uno de los elementos de lista2. A cada par los 
    separa con los caracteres almacenados en separador.
    Parámetros:
        lista1: de tipo list.
        lista2: de tipo list.
        separador: de tipo str. Se utiliza para separar pares de elementos.
    Regresa:
        Una lista de cadenas.
    """
    return [str(el1) + separador + str(el2) for el1 in lista1 for el2 in lista2]

print('\nPruebas de la función uno_y_uno()'.upper())
# CP1: se proporcionan dos listas de cadenas que representan sílabas.
lis1 = ['ver', 'ro', 'a', 'blan']
lis2 = ['de', 'jo', 'zul', 'co']
print('\nCP1 (listas de igual longitud):', uno_y_uno(lis1, lis2, ''))
# CP2: se proporcionan dos listas de cadenas de diferente longitud.
lis3 = ['so', 'ma', 'la']
print('CP2 (diferente longitud):', uno_y_uno(lis1, lis3, ''))
# CP3: se proporcionan dos listas de números.
num = [1, 2, 3, 4]
cubo = [1, 8, 27, 64]
print('CP3 (listas de números):', uno_y_uno(num, cubo, ' --> '))

print('\nPruebas de la función todos_con_todos()'.upper())
# CP4: se proporcionan dos listas de cadenas de diferente longitud.
saludos = ['Buenos días', 'Buenas tardes', 'Buenas noches', 'Hola']
titulo = ['Sra.', 'Sr.', 'Srta.']
print('\nCP4 (diferente longitud):', todos_con_todos(saludos, titulo, ' '))
# CP5: se proporcionan dos listas una de las cuales está vacía.
print('CP5 (con una vacía):', todos_con_todos(saludos, [], ' '))



