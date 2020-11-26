# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.15
Elimina los elementos de una lista que no aparecen como valores
en un diccionario.
"""

lista = [103, 87, 105, 98, 80, 104, 85, 54, 60]
equipos = {('pat', 'lara'): 85, ('jorge', 'ines'): 80, ('luis', 'leti'): 103}

lista = [item for item in lista if item in equipos.values()]
print('\nLista luego de eliminar los valores:', lista)


