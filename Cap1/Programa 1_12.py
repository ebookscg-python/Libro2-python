# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 1.12
"""

def genera_lista_pares(lista):
    """Genera una lista con los números pares almacenados en lista.    
    Parámetro:
        lista: de tipo list. Almacena números enteros.
    Regresa: 
        Una lista con números enteros pares.
    Lanza:
        ValueError: cuando la lista recibida no almacena ningún número par.
    """ 
    pares = [num for num in lista if num % 2 == 0]
    if len(pares) == 0:
        raise ValueError('No hay pares en la lista recibida.')
    return pares

# =============================================================================
# Algunas pruebas de la función genera_lista_pares
# =============================================================================
# CP1: se da una lista que tiene pares e impares.
lista1 = [13, 45, 64, 32, 11, 17, -14, 81]
print('\nCP1:', genera_lista_pares(lista1))
# CP2: se da una lista que tiene solo pares.
lista2 = [130, 48, 64, 32, 10, 174, -14, 88]
print('CP2:', genera_lista_pares(lista2))
# CP3: se da una lista que tiene solo impares.
lista3 = [13, 45, 61, 321, 101, 173, -11, 87]
try:    
    print('CP3:', genera_lista_pares(lista3))
except ValueError as error:
    print('CP3:', error)
# CP4: se da una lista vacía.
lista4 = []
try:    
    print('CP4:', genera_lista_pares(lista4))
except ValueError as error:
    print('CP4:', error)