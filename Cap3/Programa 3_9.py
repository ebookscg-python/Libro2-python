# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.9
Obtiene:
1. Palabras en común que existen entre: inglés-italiano, inglés-francés y 
francés-italiano.
2. Cantidad de palabras aprendidas (considerando los 3 idiomas).
3. Cantidad de palabras distintas aprendidas.
"""

traduc = {'cero': ('zero', 'zero', 'zéro'), 'uno': ('one', 'uno', 'un'), 
          'dos': ('two', 'due', 'deux'), 'tres': ('three', 'tre', 'trois'), 
          'cuatro': ('four', 'quattro', 'quatre'),
          'cinco': ('five', 'cinque', 'cinq'), 
          'seis': ('six', 'sei', 'six'), 
          'siete': ('seven', 'sette', 'sept'), 
          'ocho': ('eight', 'otto', 'huit'), 
          'nueve': ('nine', 'nove', 'neuve'),
          'diez': ('ten', 'dieci', 'dix')}

valores = traduc.values()
ingles = set()
italiano = set()
frances = set()
for tupla in valores:
    ingles.add(tupla[0])
    italiano.add(tupla[1])
    frances.add(tupla[2])
    
# Inciso 1: palabras comunes entre idiomas.
comuni_i = ingles & italiano 
if comuni_i:
    print('\nPalabras que comparte el inglés con el italiano:', comuni_i)
else:
    print('\nNo hay palabras comunes entre el inglés y el italiano.')
comuni_f = ingles & frances 
if comuni_f:
    print('\nPalabras que comparte el inglés con el francés:', comuni_f)
else:
    print('\nNo hay palabras comunes entre el inglés y el francés.')
comunf_i = frances & italiano 
if comunf_i:
    print('\nPalabras que comparte el francés con el italiano:', comunf_i)
else:
    print('\nNo hay palabras comunes entre el francés y el italiano.')

# Inciso 2: total de palabras aprendidas.
total = len(ingles) + len(italiano) + len(frances)
print('\nTotal de palabras que conoce en otros idiomas:', total)

# Inciso 3: palabras diferentes.
diferentes = ingles | frances | italiano
print(f'\nConoce {len(diferentes)} palabras diferentes y son: ', diferentes)
