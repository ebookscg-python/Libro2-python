# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 1_6
Ejemplos del uso de operadores relacionales, de membresía y 
de identidad con listas.
"""
import copy

precios = [205.30, 107.18, 25, 450, 310.89, 170.23, 340]
vacia = []
colores_primarios = ['rojo', 'verde', 'azul']
colores = ['verde', 'azul', 'amarillo', 'blanco']

if precios:
    print('Lista precios: no vacía')  # Imprime.
else:
    print('Lista precios: vacía')
    
if not vacia:
    print('Lista vacía: vacía')  # Imprime.
else:
    print('Lista vacía: no vacía')

# Operadores relacionales.
otra_lista = precios  # Asigna la lista a otra variable.
if precios == otra_lista:  
    print('Las listas son iguales')  # Imprime.
else:
    print('Las listas no son iguales')
    
if precios == colores_primarios:
    print('precios y colores: son iguales')  
else:
    print('precios y colores: no son iguales')  # Imprime.
    
if colores_primarios != colores:
    print('Listas colores y colores_primarios: distintas')  # Imprime.
    
if colores_primarios < colores:
    print('Lista colores_primarios es menor que lista colores')  # Imprime.

if colores_primarios > colores:
    print('Lista colores_primarios es mayor que lista colores')  # No imprime.

'''
Se lanza la excepción: 
    TypeError: '<' not supported between instances of 'float' and 'str'
if precios < colores_primarios:
    print('precios y colores: son iguales')  
else:
    print('precios y colores: no son iguales')
'''
    
# Operadores de identidad.
if precios is otra_lista:  
    print('precios y otra_lista: son la misma lista')  # Imprime.
else:
    print('No son la misma lista')

copia = copy.copy(precios)  # Hace una copia de la lista. Es otro objeto.
if precios is copia:  
    print('Son la misma lista')
else:
    print('precios y copia: no son la misma lista')  # Imprime.
    
if colores is not colores_primarios:
    print('colores y colores_primarios: no son la misma lista')  # Imprime.
    
# Operadores de membresía.
if 'rojo' in colores_primarios:
    print('El rojo es un color primario')  # Imprime.
    
if 'dorado' not in colores_primarios:
    print('El dorado no es un color primario')  # Imprime.
