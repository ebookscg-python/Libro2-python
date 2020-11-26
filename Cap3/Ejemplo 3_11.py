# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 3_11
Diccionarios y la función enumerate.
"""

# Se crea un diccionario con los meses del primer semestre del año y los 
# números que los identifican. 
primer_semestre = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']
mapeo = {}
for i, elemento in enumerate(primer_semestre, 1):  # Se enumera a partir del 1.
    mapeo[elemento] = i
print('\nMeses-número:\n', mapeo)

# Se crea un diccionario con las letras del abecedario y los valores decimales
# que les corresponden según el código ASCII.
abecedario = 'abcdefghijklmnopqrstuvwxyz'  # Se omite la ñ.
letras = {}
for i, elemento in enumerate(abecedario, 97):  # Se enumera a partir del 97.
    letras[elemento] = i
print('\nLetras-código ASCII:\n', letras)
