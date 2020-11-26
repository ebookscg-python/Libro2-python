# -*- coding: utf-8 -*-
"""
@author: guardati
Auxiliar para la creación de archivos con datos leídos de la terminal.
"""

nom_arch = input('Ingrese el nombre del archivo: ')
with open(nom_arch, 'w') as arch:
    dato = input('Dato: ')
    while dato != '':      
        arch.write(dato + '\n')
        dato = input('Dato: ')
   