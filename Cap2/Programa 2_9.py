# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 2.9
"""


def aparece_dos_veces(palabra):
    """ Determina si todas las letras de la palabra están exactamente 2 veces.
    Parámetro:
        palabra: de tipo str.
    Regresa:
        True si la palabra cumple la condición y False en caso contrario.
    """        
    n = len(palabra)
    # Debe tener, por lo menos, dos caracteres y un número par de
    # caracteres para poder cumplir con la propiedad que se pide.
    if n > 1 and n % 2 == 0:  
        primera = set()
        segunda = set()
        indice = 0
        resp = True
        while indice < n and resp:
            letra = palabra[indice]
            if letra not in primera:
                primera.add(letra)
            else:
                if letra not in segunda:
                    segunda.add(letra)
                else:
                    resp = False  # Está más de 2 veces.
            indice += 1
        resp = resp and len(primera) == len(segunda)
    else:
        resp = False
    return resp
    
# Algunas pruebas de la función.
print('\nCP1: la palabra "papa" -->', aparece_dos_veces('papa'))
print('CP2: la palabra "nenes" -->', aparece_dos_veces('nenes'))
print('CP3: la palabra "detergente" -->', aparece_dos_veces('detergente'))
print('CP4: la palabra "tratar" -->', aparece_dos_veces('tratar'))
# Se quitó el acento a termómetro.
print('CP5: la palabra "termometro" -->', aparece_dos_veces('termometro'))  
print('CP6: una cadena vacía -->', aparece_dos_veces(''))  
