# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 1.3
"""

def cuenta_positivos(lista):
    """ Cuenta el total de números positivos que contiene la lista.    
    Parámetro:
        lista: de tipo list. Todos sus elementos son del mismo tipo.
    Regresa: 
        La cantidad de números positivos almacenados en la lista.
    Lanza:
        ValueError: si el parámetro recibido no es una lista o si 
        sus elementos no son números.
    """ 
    if lista and (type(lista[0]) == int or type(lista[0]) == float):       
        positivos = 0
        for numero in lista:
            if numero > 0:
                positivos += 1
        return positivos
    raise ValueError('Error en los datos: no es un dato válido o no tiene números.')
    
# =============================================================================
# Algunas pruebas de la función cuenta_positivos().
# =============================================================================
# CP1: se proporciona una lista de números enteros.
lista1 = [405, -107, 210, 5, -23, -45, 87]
print('\nCP1 - Total de positivos =', cuenta_positivos(lista1))      
# CP2: se proporciona una lista de números reales negativos.
lista2 = [-35.61, -10.17, -15.99, -8.5]
print('CP2 - Total de positivos =', cuenta_positivos(lista2))
# CP3: se proporciona una lista de cadenas de caracteres.
lista3 = ['Costa Rica', 'Colombia', 'Canadá', 'Chile']
try:
    print('CP3 - Total de positivo s=', cuenta_positivos(lista3))
except ValueError as error:
    print('CP3 -', error)  
# CP4: no se proporciona una lista.
lista4 = None
try:
    print('CP4 - Total de positivos =', cuenta_positivos(lista4))
except ValueError as error:
    print('CP4 -', error)
        