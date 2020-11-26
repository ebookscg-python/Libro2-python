# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 2.1
"""

def contiene_mismos_caract(frase1, frase2):
    """ Determina si dos frases tienen los mismos caracteres, sin
    importar si se repiten o el orden.    
    Parámetros:
        frase1: de tipo str.
        frase2: de tipo str.
    Regresa: 
        True si las frases cumplen con la condición y False en caso contrario.
    """
    conj1 = set(frase1)
    conj2 = set(frase2)
    return conj1 == conj2

# =============================================================================
# Uso de la función contiene_mismos_caract().
# =============================================================================
frase1 = input('Ingrese una frase: ')
frase2 = input('Ingrese otra frase: ')
if contiene_mismos_caract(frase1, frase2):
    print('\nSí tienen los mismos caracteres.')
else:
    print('\nNo tienen los mismos caracteres.')
              

