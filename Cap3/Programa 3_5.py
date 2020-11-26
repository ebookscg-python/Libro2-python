# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.5
Dado un diccionario formado por nombres de materias y número de
créditos, el programa genera un nuevo diccionario formada solo por 
las materias cuyos créditos sean menor o igual a un límite dado
por el usuario.
"""

materias = {'matematica': 6, 'fisica': 8, 'biologia': 8, 'idioma': 4, 
            'quimica': 9, 'computacion': 8, 'historia': 4, 'civismo': 5}
limite = int(input('Ingrese el máximo de créditos: '))
if limite > 0:
    elegidas = {}
    for mat, cred in materias.items():
        if cred <= limite:
           elegidas[mat] = cred
    if len(elegidas) > 0:
        print('\nMaterias elegidas:', elegidas)  
    else:
        print(f'\nNo hay materias con {limite} o menos créditos.')
else:
    print('\nDebe ingresar un valor > 0.')

      



