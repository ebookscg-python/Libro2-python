# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 2.6
"""

def es_panvocalica(palabra):
    """ Determina si la palabra es panvocálica.
    Parámetro:
        palabra: de tipo str.
    Regresa:
        True si la palabra es panvocálica y False en caso contrario.
    """
    n = len(palabra)    
    if n >= 5:
        vocales = {'a', 'e', 'i', 'o', 'u'}
        panvo = set()
        indice = 0
        resp = True
        while indice < n and resp:
            letra = palabra[indice]
            if letra in vocales:
                if letra not in panvo:
                    panvo.add(letra)
                else:
                    resp = False  # Porque se repite.
            indice += 1
        resp = resp and len(panvo) == 5  # Están las 5 vocales sin repetir.
    else:
        resp = False
    return resp  

# =============================================================================
# Algunas pruebas de la función es_panvocálica
# =============================================================================
# CP1: se da una palabra panvocálica.
if es_panvocalica('enunciado'):
    print('\nCP1: la palabra "enunciado" es panvocálica.')
else:
    print('\nCP1: la palabra "enunciado" no es panvocálica.')
# CP2: se da una palabra con las 5 vocales, pero hay repetidas.
if es_panvocalica('ayuntamiento'):
    print('CP2: la palabra "ayuntamiento" es panvocálica.')
else:
    print('CP2: la palabra "ayuntamiento" no es panvocálica.')
# CP3: se da una palabra que no tiene las 5 vocales.
if es_panvocalica('detergente'):
    print('CP3: la palabra "detergente" es panvocálica.')
else:
    print('CP3: la palabra "detergente" no es panvocálica.')
# CP4: se da una palabra panvocálica.
if es_panvocalica('pauperismo'):
    print('CP4: la palabra "pauperismo" es panvocálica.')
else:
    print('CP4: la palabra "pauperismo" no es panvocálica.')
# CP5: se da una palabra de longitud menor a 5.
if es_panvocalica('miau'):
    print('CP5: la palabra "miau" es panvocálica.')
else:
    print('CP5: la palabra "miau" no es panvocálica.')

