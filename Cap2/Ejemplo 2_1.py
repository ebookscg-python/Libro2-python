# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 2_1
Conjuntos: definición y algunas operaciones.
"""
# Definición por medio de {} y listado de elementos.
vocales = {'a', 'e', 'i', 'o', 'u'}
print('\nConjunto de las vocales:', vocales)
print('Tipo de dato:', type(vocales))

lista = [2, 24, 6, 8, 2]  
cadena = 'un granito de sal'
tupla = ('a', 'g', 'k', 'b', 'a')
# Usando el constructor set().
conj_lis = set(lista)  
print('\nA partir de una lista:', conj_lis)
conj_cad = set(cadena)
print('A partir de una cadena:', conj_cad)
conj_tup = set(tupla)
print('A partir de una tupla:', conj_tup)
vacio = set()
print(f'\nConjunto vacío: {vacio} \nCardinalidad = {len(vacio)}')

# Cardinalidad del conjunto: total de elementos.
print('\nCardinalidad:', len(conj_lis))  

# Operador de membresía: pertenencia al conjunto.
if 2 in conj_lis:
    print('\nEl 2 pertenece al conjunto.')
if 'm' not in vocales:
    print('La "m" no pertenece a las vocales.')
    