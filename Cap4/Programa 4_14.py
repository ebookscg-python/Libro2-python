# -*- coding: utf-8 -*-
"""
@author: guardati
Auxiliar al problema 4.17
"""
import arreglo

print('\nIngrese las claves de los participantes, en forma ordenada.'.upper())
arreglo.guarda_en_archivo('B', 'claves', 'Total de participantes', '¿Clave?:')
print('\nIngrese los puntajes de acuerdo al orden dado a las claves.'.upper())
arreglo.guarda_en_archivo('B', 'puntajes', 'Total de participantes', '¿Puntaje?:')

