# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 2.3
"""

def cuenta_comunes(conj1, conj2):
    """ Obtiene el total de elementos comunes entre los 2 conjuntos.    
    Parámetros:
        conj1: de tipo set o frozenset.
        conj2: de tipo set o frozenset.
    Regresa:
        La cantidad (tipo int) de elementos comunes a ambos conjuntos.
    """
    comunes = 0
    if len(conj1) < len(conj2):
        arecorrer = conj1
        otro = conj2
    else:
        arecorrer = conj2
        otro = conj1            
    for ele in arecorrer:
        if ele in otro:
            comunes += 1
    return comunes

# =============================================================================
# Algunas pruebas de la función cuenta_comunes()
# =============================================================================
vocales = {'a', 'e', 'i', 'o', 'u'}
letras = {'g', 'o', 'm', 'b', 'e', 'a', 'u', 'i'}
vacio = {}
consonantes = {'g', 'r', 'd', 's'}
vocales_completas = frozenset('áéíóúüaeiou')
# CP1: se proporcionan conjuntos que tienen elementos en común. 
print('\nCP1:', cuenta_comunes(vocales, letras))
# CP2: se proporcionan conjuntos que no tienen elementos en común. 
print('CP2:', cuenta_comunes(vocales, consonantes))
# CP3: se proporcionan un conjunto vacío y otro con elementos. 
print('CP3:', cuenta_comunes(consonantes, vacio))
# CP4: se proporcionan un set y un frozenset que tienen elementos en común. 
print('CP4:', cuenta_comunes(vocales, vocales_completas))