# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 1.5 
"""

def determina_minimo_2cadenas(lista):
    """ Determina si en la lista hay, por lo menos, dos datos tipo
    cadena de caracteres (str).    
    Parámetro:
        lista: de tipo list. Almacena datos que pueden ser de cualquier tipo.
    Regresa: 
        True si se encuentran los datos solicitados, False caso contrario.
    """     
    limite = len(lista)
    indice = 0
    contador = 0
    while indice < limite and contador < 2:
        if type(lista[indice]) == str:
            contador += 1
        indice += 1
    return contador == 2

# =============================================================================
# Algunas pruebas de la función determina_minimo_2cadenas() 
# =============================================================================
# CP1: se da una lista con 4 cadenas.
colores = ['rojo', 'verde', 'blanco', 'amarillo']
if determina_minimo_2cadenas(colores):
    print('\nCP1: sí hay, mínimo, 2 cadenas.')  # Imprime.
else:
    print('\nCP1: no hay, mínimo, 2 cadenas.')
# CP2: se da una lista con 2 cadenas.
lista_mezcla = [305.23, True, 'blanco', 108, 30, 'azul']
if determina_minimo_2cadenas(lista_mezcla):
    print('CP2: sí hay, mínimo, 2 cadenas.')  # Imprime.
else:
    print('CP2: no hay, mínimo, 2 cadenas.')
# CP3: se da una lista con 1 cadena.
lista_mezcla.pop(5)
if determina_minimo_2cadenas(lista_mezcla):
    print('CP3: sí hay, mínimo, 2 cadenas.')  
else:
    print('CP3: no hay, mínimo, 2 cadenas.')  # Imprime.
# CP4: se da una lista de números.
pares = [2, 4, 6, 8]
if determina_minimo_2cadenas(pares):
    print('CP4: sí hay, mínimo, 2 cadenas.')
else:
    print('CP4: no hay, mínimo, 2 cadenas.')  # Imprime.
# CP5: se da una lista vacía.
vacia = []
if determina_minimo_2cadenas(vacia):
    print('CP5: sí hay, mínimo, 2 cadenas.')
else:
    print('CP5: no hay, mínimo, 2 cadenas.')  # Imprime.
    