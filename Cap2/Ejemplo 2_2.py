# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 2_2
Operaciones de inserción y eliminación de elementos.
"""
# Se definen algunos conjuntos.
lista = [2, 24, 6, 8, 2]  
cadena = 'un granito de sal'
vocales = {'a', 'e', 'i', 'o', 'u'}
conj_lis = set(lista)  
conj_cad = set(cadena)
vacio = set()

# Agrega un elemento al conjunto, siempre que no esté.
print('\nConjunto original:', conj_lis)
conj_lis.add(16)
print('Luego de agregar el 16:', conj_lis)
conj_lis.add(16)  # No lo agrega.
print('Luego de intentar con el segundo 16:', conj_lis)
conj_lis.add(64) 
conj_lis.add(10)
print('Luego de agregar el 64 y el 10:', conj_lis)
# Agrega todos los elementos del conjunto parámetro.
vocales.update(conj_cad)
print('Luego de agregar otro conjunto:', vocales)

# Quita aleatoriamente un elemento y lo regresa.  
print('\nResultado del pop():', conj_lis.pop())
print('Resultado del pop():', conj_cad.pop())
# Genera: KeyError: 'pop from an empty set'
# print('Resultado del pop():', vacio.pop()) 

# Quita un elemento del conjunto.
conj_lis.remove(8)
print('\nLuego de quitar el 8:', conj_lis)
# conj_tup.remove('d')  # Provoca: KeyError: 'd'

vocales.discard('d')  # No provoca error.
conj_cad.discard('a')
print('\nLuego de quitar la "a":', conj_cad)

# Borra todos los elementos del conjunto.
vocales.clear()
print('\nLuego de eliminar todos los elementos:', vocales)

