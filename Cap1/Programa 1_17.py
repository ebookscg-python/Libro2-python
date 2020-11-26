# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 1.17
"""

def genera_cadena(lista1, lista2, separador):
    """ Genera una cadena con el contenido de las listas:
        el primero de lista1 con el último de lista2,
        el segundo de lista1 con el penúltimo de lista2,
        etc.
    Parámetros:
        lista1: de tipo list.
        lista2: de tipo list. 
        separador: de tipo str. Se usa para separar cada par de datos.
    Regresa: 
        Una cadena con el contenido de las listas
    Lanza:
        ValueError: si las listas tienen distinta longitud.
    """
    if len(lista1) == len(lista2):
        resultado = ''
        for el1, el2 in zip(lista1, lista2[::-1]):
            resultado += str(el1) + separador + str(el2) + '\n'
        return resultado
    raise ValueError('Las listas tienen distintas longitudes.')

# CP1: se proporcionan dos listas de igual longitud.
ferreteria = ['martillo', 'clavo', 'tenaza', 'destornillador', 'taladro']
precios = [1500, 195.3, 380.5, 1.2, 250]
cad1 = genera_cadena(ferreteria, precios, ': $')
print('\nCP1 --> listas de igual longitud: \n', cad1)
# CP2: se proporcionan dos listas de igual longitud.
l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [49, 36, 25, 16, 9, 4, 1]
cad2 = genera_cadena(l1, l2, ' -- ')
print('CP2 --> listas de igual longitud: \n', cad2)
# CP3: se proporcionan dos listas de distinta longitud.
l3 = [36, 25, 16, 9, 4, 1]
try:
    cad3 = genera_cadena(l1, l3, ' - ')
    print('CP3 --> listas de distinta longitud: \n', cad3)
except Exception as error: 
    print('CP3 -->', error)
# CP4: se proporcionan dos listas vacías.
print('CP4 --> listas vacías: \n', genera_cadena([], [],', '))
    
    