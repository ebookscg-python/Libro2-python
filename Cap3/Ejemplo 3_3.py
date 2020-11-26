# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 3_3
Diccionarios: aplicación de funciones predefinidas y operadores.
"""
# Se importa el módulo operator para poder ordenar por valor.
import operator

num_meses = {'ene': 1, 'feb': 2, 'mar': 3, 'abr': 4, 'may': 5, 'jun': 6}
nom_meses = {1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril', 5: 'mayo', 6: 'junio'}
d1 = {1: 'azul', 2: 'rojo', 3: 'verde'}
d2 = {}
d3 = {2: 'rojo', 1: 'azul', 3: 'verde'}
d4 = {0: 'amarillo', 1: 'azul', 2: 'rojo', 3: 'verde'}

# Regresa el total de elementos del diccionario.
print('\nTotal de elementos del diccionario:', len(num_meses))

# Evalúa si todas las claves son True.
print('\nCP1: Resultado de "all" con d1 -->', all(d1))
print('CP2: Resultado de "all" con d4 -->', all(d4))
print('CP3: Resultado de "all" con diccionario vacío -->', all(d2))  
# Evalúa si alguna clave es True.
print('\nCP1: Resultado de "any" con d1 -->', any(d1))
print('CP2: Resultado de "any" con diccionario vacío -->', any(d2))

# Regresa una lista de claves ordenadas de mayor a menor.
ordenado = sorted(num_meses, reverse = True)
print('\nClaves ordenadas:', ordenado)
menu = {'helado': 25, 'tarta': 43, 'galleta': 12, 'merengue': 18} 
# Genera un diccionario ordenado por valor.   
menu_ord = dict(sorted(menu.items(), key = operator.itemgetter(1)))
print('Menú ordenado por precio:', menu_ord)  

# Compara los elementos de dos diccionarios. No importa el orden.
if num_meses == nom_meses:
    print('\nSí son iguales.')
else:
    print('\nNo son iguales.')  # Imprime.
if d1 == d3:
    print('Sí son iguales.')  # Imprime.
else:
    print('No son iguales.')
if d1 != d2:
    print('Sí son diferentes.')  # Imprime.
else:
    print('No son diferentes.')
    

