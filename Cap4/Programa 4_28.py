# -*- coding: utf-8 -*-
"""
@author: guardati
Pruebas aplicadas a la función del problema 4.10
"""


import array
import arreglo

arre = array.array('b', [4, 15, 12, -34, 48, -18, 11]) 

# CP1: se pide eliminar el dato de una posición que está en el arreglo.
print('\nCP1: elemento quitado:', arreglo.elimina(arre, 3))
print('Luego de quitar el 4to elemento:', arreglo.a_cadena(arre))

# CP2: se pide eliminar el dato que está al final del arreglo.
print('\nCP2: elemento quitado:', arreglo.elimina(arre, 5))
print('Luego de quitar el último elemento:', arreglo.a_cadena(arre))

# CP3: se pide eliminar el dato que está al inicio del arreglo.
print('\nCP3: elemento quitado:', arreglo.elimina(arre, 0))
print('Luego de quitar el primer elemento:', arreglo.a_cadena(arre))

# CP4: se pide eliminar el dato que está en una posición fuera del arreglo.
try:
    print('\nCP4: elemento quitado:', arreglo.elimina(arre, 12))
    print('El arreglo luego de la eliminación:', arreglo.a_cadena(arre))
except IndexError as error:
    print('\nCP4:', error)
    
# CP5: se pide eliminar un dato de un arreglo vacío.
vacio = array.array('b')
try:
    print('\nCP5: elemento quitado:', arreglo.elimina(vacio, 1))
    print('El arreglo luego de la eliminación:', arreglo.a_cadena(vacio))
except IndexError as error:
    print('\nCP5:', error)