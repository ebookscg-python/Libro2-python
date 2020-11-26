# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.16
Quita de la lista aquellos elementos que no forman parte de
las tuplas que son claves de un diccionario.
"""


equipos = {('pat', 'lara'): 85, ('jorge', 'ines'): 80, ('luis', 'leti'): 103}
nombres = ['jose', 'pat', 'lara', 'alicia', 'ines']

solo_nom = list(equipos.keys())  
nombres = [ele for tupla in solo_nom for ele in tupla if ele in nombres]
print('\nLista modificada:', nombres)