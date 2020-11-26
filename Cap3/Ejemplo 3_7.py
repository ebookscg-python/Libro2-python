# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 3_7
Definición de diccionarios por comprensión.
"""

# Ejemplo 1: a partir de un rango.
cuadrados = {n: n*n for n in range(11)}
print('\nCuadrados-1:', cuadrados)
# Se pudo hacer:
otros = {}
for n in range(11):
   otros[n] = n * n
print('Cuadrados-2:', otros)

# Ejemplo 2: a partir de un diccionario.
menu = {'helado': 25, 'tarta': 43, 'galleta': 12, 'merengue': 18}          
menu_ord = {pla: pre for pla, pre in sorted(menu.items())}  
print('\nMenú ordenado-1:', menu_ord)
# Se pudo hacer:
otro_menu = {}
for pla, pre in sorted(menu.items()):
    otro_menu[pla] = pre
print('Menú ordenado-2:', otro_menu)

# Ejemplo 3: a partir de una lista de tuplas.
lenguajes = [('python', 'medio'), ('java', 'medio'), ('ruby', 'fácil'), 
             ('lisp', 'difícil')]
leng_dic = {leng: dif for leng, dif in lenguajes}
print('\nLenguajes y dificultad-1:', leng_dic)
# Se pudo hacer:
otro_leng = {}
for leng, dif in lenguajes:
    otro_leng[leng] = dif
print('Lenguajes y dificultad-2:', otro_leng)


    



