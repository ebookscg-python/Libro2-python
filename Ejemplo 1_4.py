# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 1_4
Ejemplos de partición de listas.
"""

# Se crea una lista de números enteros.
lista1 = [1, 2, 3, 4, 5, 6]
print('\nLista:', lista1)
# Sublista formada con los elementos de las posiciones 0 a la 2 inclusive.
l1 = lista1[0:3]
print('Del primero al tercero:', l1)
# Sublista formada con los elementos de las posiciones 0 a la 3 inclusive.
l2 = lista1[:4]
print('Del primero al cuarto:', l2)
# Sublista formada con los elementos de las posiciones 3 a la 5 inclusive.
l3 = lista1[3:]
print('Del cuarto al último:', l3)
# Sublista formada con los elementos desde el inicio hasta el final,
# con un salto de 2.
l4= lista1[::2]
print('De izquierda a derecha, tomando 1 cada 2:', l4)
# Sublista formada con los elementos desde el final hasta el inicio,
# con un salto de 3.
l5 = lista1[-1::-3]
print('De derecha a izquierda, tomando 1 cada 3:', l5)
# Quita los elementos de la posición 0 a la última inclusive.
del lista1[:]
print('Luego de quitar todos los elementos', lista1)

# Se crea una lista de cadenas de caracteres.
lista2 = list('abcdefghij')
print('\nLista:', lista2)
# Reemplaza los elementos de las posiciones 0 y 1 por los valores dados.
lista2[0:2] = ['rojo', 'verde']
print('Se reemplazaron los 2 primeros valores:', lista2)
# Quita los elementos de las posiciones 4 a la 8 inclusive.
lista2[4:9] = [] 
print('Se quitaron del 5to al 9no dato:', lista2)
# Agrega los valores de la lista en la posición 0, reemplazando el valor
# de esa posición y desplazando hacia la derecha todos los demás.
lista2[0:1] = ['azul', 'gris', 'blanco'] 
print('Luego de agregar 3 colores:', lista2)
# Agrega todos sus elementos al inicio.
lista2[:0] = lista2
print('Luego de agregar sus propios elementos:', lista2)
# Vacía la lista.
lista2[:] = [] 
print('Luego de vaciar la lista:', lista2)


