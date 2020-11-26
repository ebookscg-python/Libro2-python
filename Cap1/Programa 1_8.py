# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 1.8
"""
import bisect

def busca_binaria(elemento, lista):
    """ Busca el elemento en la lista.    
    Parámetro:
        lista: de tipo list. Formada por elementos del mismo tipo, 
        ordenados de menor a mayor.
        elemento: dato del mismo tipo que los elementos de la lista.
    Regresa: 
        Una tupla en la que el primer valor (tipo bool) indica si elemento 
        está o no en la lista y el segundo valor (tipo int) indica la 
        posición en la que está o en la que debería estar.
    """ 
    izquierdo = 0
    derecho = len(lista) - 1
    centro = (izquierdo + derecho) // 2
    while izquierdo <= derecho and lista[centro] != elemento:
        if lista[centro] > elemento:
            derecho = centro - 1
        else:
            izquierdo = centro + 1
        centro = (izquierdo + derecho) // 2
    if izquierdo > derecho:
        esta = False
        posicion = izquierdo
    else:
        esta = True
        posicion = centro
    return esta, posicion

# =============================================================================
# Algunas pruebas de la función busca_binaria()
# =============================================================================
# CP1: se da una lista ordenada y un dato que está en la lista.
lista1 = ['Alicia', 'Clara', 'David', 'Dolores', 'Luisa', 'Manuel', 'Pedro']
res1 = busca_binaria('Clara', lista1)
if res1[0]:
    print('\nCP1: Clara está en la lista. Posición =', res1[1])
# CP2: se da una lista ordenada y un dato que no está.
res2 = busca_binaria('Alan', lista1)
if res2[0]:
    print('CP2: Alan está en la lista. Posición =', res2[1])
else:
    print('CP2: Alan no está en la lista. Debería estar en:', res2[1]) 
# CP3: se da una lista ordenada y un dato que no está.
res3 = busca_binaria('Samuel', lista1)
if res3[0]:
    print('CP3: Samuel está en la lista. Posición =', res3[1])
else:
    print('CP3: Samuel no está en la lista. Debería estar en:', res3[1]) 
# CP4: se da una lista ordenada y un dato que no está.
res4 = busca_binaria('Elena', lista1)
if res4[0]:
    print('CP4: Elena está en la lista. Posición =', res4[1])
else:
    print('CP4: Elena no está en la lista. Debería estar en:', res4[1])
# CP5: se proporciona una lista vacía y un nombre.
lista2 = []
res5 = busca_binaria('Irene', lista2)
if res5[0]:
    print('CP5: Irene está en la lista. Posición =', res5[1])
else:
    print('CP5: Irene no está en la lista. Debería estar en:', res5[1])
    
