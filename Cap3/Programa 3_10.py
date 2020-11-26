# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.10
"""

def cuenta_vocales(cadena):
    """ Cuenta el número de veces que aparece cada una de las
    vocales en una cadena de caracteres.
    Parámetro:
        cadena: de tipo str.
    Regresa:
        Un diccionario que almacena la frecuencia con la que aparece cada 
        vocal en la cadena. 
    """
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}    
    for c in cadena:
        if c in vocales:
            vocales[c] += 1
    return vocales  

# CP1: se proporciona una cadena con algunas de las vocales.
cad1 = 'todos los perros se van al cielo'
print('\nCP1: cadena con algunas de las vocales -->', cuenta_vocales(cad1))
# CP2: se proporciona una cadena con todas las vocales.
cad2 = 'los bomberos se detuvieron junto a los autos'
print('CP2: cadena con todas las vocales -->', cuenta_vocales(cad2))
# CP3: se proporciona una cadena sin vocales.
cad3 = 'xxxxxxxxx'
print('CP3: cadena sin vocales -->', cuenta_vocales(cad3))
# CP4: se proporciona una cadena vacía.
cad4 = ''
print('CP4: cadena vacía -->', cuenta_vocales(cad4))    


