# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.17
Genera e imprime la conjugación de verbos regulares 
del español en tiempo presente.
"""

# Diccionario con las declinaciones del presente.
declin = {'ar': ['o', 'as', 'a', 'amos','áis', 'an'],
          'er': ['o', 'es', 'e', 'emos', 'éis', 'en'],
          'ir': ['o', 'es', 'e', 'imos', 'ís', 'en']}
# Lista con los pronombres.
pronom = ['yo', 'tú', 'él', 'nosotros', 'vosotros', 'ellos']
# Conjunto con las terminaciones de verbos.
terminaciones = {'ar', 'er', 'ir'}

verbo = input('Ingrese un verbo regular en infinitivo: ')
n = len(verbo) - 2
raiz = verbo[:n]
ter = verbo[n:]
if ter in terminaciones:    
    dec = declin[ter]
    conjug = [raiz + car for car in dec]
    print(f'\nConjugación del verbo "{verbo}":'.upper())
    for i in range(0, 6):
        print(pronom[i], conjug[i])
else:
    print('\nNo existe un verbo con esa terminación.')
