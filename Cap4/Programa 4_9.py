# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.11
Obtiene e imprime la media, la moda y la mediana de un grupo de edades.
"""
import arreglo
import array


arre = array.array('b')
resp = input('\n¿Ya existe el archivo S/N? ')
if resp.upper() == 'S':
    nombre = input('Nombre del archivo: ')
    n = int(input('Total de asistentes: '))
else:
    nombre = input('Nombre del archivo donde se guardarán las edades: ')
    n = arreglo.guarda_en_archivo('B', nombre, '¿Total de asistentes?', '¿Edad?')
try:
    file_e = open(nombre, 'rb')
    arre.fromfile(file_e, n) 
    file_e.close()
except Exception as error:
    print('\nHubo un error:', error)
else:
    arreglo.ordena_crec(arre)
    media = arreglo.suma_arreglo(arre) / n    
    cen = n // 2
    if n % 2 != 0:
        mediana = arre[cen]
    else:        
        mediana = (arre[cen] + arre[cen - 1]) / 2 
    print(f'\nLa media de las edades es: {media:.2f}')
    try:
        moda = arreglo.calcula_moda(arre)
        print('La moda de las edades es:', moda)
    except Exception as error:
        print(error)
    print(f'La mediana de las edades es: {mediana:.2f}')
