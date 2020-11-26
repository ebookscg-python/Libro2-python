# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 3_6
Creación de diccionarios usando otros datos estructurados.
"""

# Diccionarios con diccionarios.
alumnos = {'juan': {'matematica': 9.5, 'biologia': 7.5, 'literatura': 8.7, 'fisica': 8.0},
           'ines': {'matematica': 9.0, 'biologia': 8.5, 'literatura': 6.5, 'fisica': 9.0},
           'luis': {'matematica': 9.5, 'biologia': 7.5, 'literatura': 8.7, 'fisica': 8.0}}
solo_juan = alumnos['juan']
print('\nMaterias de Juan:', solo_juan)
calif = solo_juan.values()
prom = sum(calif) / len(calif)
print('Promedio:', prom)

# Diccionario con listas
pract_dep = {'juan': ['futbol', 'basquetbol'], 'ines': ['tenis', 'voleibol'],
             'luis': ['natacion', 'futbol', 'boxeo']}
deportes = list(pract_dep.values())
print('\nDeportes practicados por los alumnos:', deportes)
# Iterando sobre la vista de valores.
fut = 0
for dep in deportes:
    if 'futbol' in dep:
        fut += 1
print('\n(1)Total de alumnos que practican fútbol =', fut)
# Usando listas por comprensión.
lis_dep = [dep for lis in deportes for dep in lis]
print('(2)Total de alumnos que practican fútbol =', lis_dep.count('futbol'))

# Diccionario con tuplas.
# Tuplas como claves.
equipos = {('pat', 'lara'): 85, ('jorge', 'ines'): 80, ('luis', 'leti'): 103}
print('\nIntegrantes de los equipos y puntajes:', equipos)
puntajes = equipos.values()
ganador = max(puntajes)
print('El mayor número de puntos obtenidos es:', ganador)
# Tuplas como valores.
temporadas = {'cereza': ('verano'), 'naranja': ('otoño', 'invierno', 'primavera', 'verano'),
              'mango': ('primavera', 'verano')}
print('\nLas frutas y sus temporadas'.upper())
for fruta in temporadas:
    print(f'La/el {fruta} se cosecha en: {temporadas[fruta]}')
# Tuplas como claves y valores.
dieta = {('desay', 'merienda'): ('lacteo', 'fruta'), 
         ('comida', 'cena'): ('proteina', 'vegetal', 'granos', 'fruta')}
resp = True
for alim in dieta:
    if 'fruta' not in dieta[alim]:
        resp = False
        break
if resp:
    print('\nSe debe comer fruta con todos los alimentos.')
else:
    print('\nNo se debe comer fruta con todos los alimentos.')
              
# Mezclando tipos de datos.
dic_mez = {'lluvia': ['lun', 'juev', 'vie'], 25: 'mar'} 
print('\nDiversos tipos:', dic_mez)



