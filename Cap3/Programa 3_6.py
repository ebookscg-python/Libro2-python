# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.6
Dado un diccionario formado por equipos y puntajes obtenidos, se pide:
- Los nombres de los integrantes del equipo que sacó más puntos.
- Los nombres de los integrantes del equipo que sacó menos puntos.
- Promedio de puntos obtenidos por todos los equipos.
""" 

equipos = {('Pat', 'Lara'): 85, ('Jorge', 'Ines'): 80, ('Luis', 'Leti'): 103,
           ('Daniel', 'Paco'): 90, ('Mari', 'Tita'): 110, ('Juan', 'Javi'): 74}
items = equipos.items()
total_eq = len(items)
if total_eq > 0:
    max_punt = -1
    min_punt = 121
    suma = 0
    for equi, puntaje in items:
        suma += puntaje
        if puntaje > max_punt:
            max_punt = puntaje
            equi_max = equi
        if puntaje < min_punt:
            min_punt = puntaje
            equi_min = equi
    promedio = suma / total_eq
    nombres = equi_max[0] + ' y ' + equi_max[1]
    print(f'\nEl máximo puntaje fue: {max_punt} obtenido por: {nombres}')
    nombres = equi_min[0] + ' y ' + equi_min[1]
    print(f'El mínimo puntaje fue: {min_punt} obtenido por: {nombres}')
    print(f'Promedio de puntos: {promedio:.2f}')
else:
    print('\nNo hay equipos registrados.')
