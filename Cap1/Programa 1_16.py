# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 1.16
"""


def quita_todos(lista, valor):
    """ Genera una lista con los elementos de la lista que no son iguales al 
    valor.
    Parámetros:
        lista: de tipo list. Representa una lista.
        valor: representa el dato que no debe aparecer en la nueva lista.
    Regresa:
        Un lista.
    """
    return [elemento for elemento in lista if elemento != valor]

# CP1: se proporciona una lista y un valor que se encuentra varias veces.
numeros = [30, 50, 30, 30, 25, 41, 18, 30]
print('\nCP1: luego de quitar el 30 -->', quita_todos(numeros, 30))
# CP2: se proporciona una lista y un valor que no está en la lista.
vocales = list('aeiou')
print('CP2: el valor no está en la lista -->', quita_todos(vocales, 'g'))
# CP3: se proporciona una lista con todos sus elementos iguales y un
# valor igual a estos.
repetidos = [6, 6, 6, 6, 6, 6, 6, 6, 6]
print('CP3: elementos iguales al dado -->', quita_todos(repetidos, 6))
# CP4: se proporciona una lista vacía.
print('CP4: lista vacía -->', quita_todos([], 6))
# CP5: se proporciona una lista y un valor de distinto tipo.
print('CP5: lista y valor de distinto tipo -->', quita_todos(vocales, 6))

