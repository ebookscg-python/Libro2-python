# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.11
"""

def obtiene_largo_palabras(cadena):
    """ Obtiene y regresa la longitud de cada una de las palabras
    que aparecen en una cadena de caracteres.
    Parámetro:
        cadena: de tipo str.
    Regresa:
        Un diccionario que almacena la longitud de cada una de las
        palabras que forman la cadena.
    """
    longitudes = dict()
    palabras = list(cadena.split())
    for pal in palabras:
      longitudes[pal] = len(pal)
    return longitudes


# Usando diccionarios por comprensión.
# def obtiene_largo_palabras(cadena):      
#     return {pal:len(pal) for pal in list(cadena.split())}

  
# CP1: se proporciona una cadena con varias palabras.
cad1 = 'todos los perros se van al cielo'
print('\nCP1: cadena con varias palabras -->', obtiene_largo_palabras(cad1))
# CP2: se proporciona una cadena con palabras repetidas.
cad2 = 'los bomberos dirigen a los peatones y a los conductores'
print('\nCP2: cadena con palabras repetidas -->', obtiene_largo_palabras(cad2))
# CP3: se proporciona una cadena vacía.
print('\nCP3: cadena vacía -->', obtiene_largo_palabras(''))