# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 1.8
Ejemplos de listas por comprensión.
"""

# A partir de una cadena de caracteres.
frase = 'listas'
lista_mayusculas = [letra.upper() for letra in frase]
print('\nA partir de una cadena:\n', lista_mayusculas)
# A partir de una tupla.
tupla = (2, 5, 8, 10)
lista_cuadrados = [numero ** 2 for numero in tupla]
print('A partir de una tupla:\n', lista_cuadrados)
# A partir de una lista.
lista_pares = [2, 4, 6, 8, 10]
lista_cubos_pares = [par ** 3 for par in lista_pares]
print('A partir de una lista:\n', lista_cubos_pares)

# Con condiciones.
varios = [2, 'calor', 4, 5, 7, 'verde', 'vacaciones', -3, 1.25]
solo_int = [num ** 2 for num in varios if type(num) == int]
print('\nSolo con enteros:', solo_int)
int_o_float = [num ** 2 for num in varios if type(num) == int or type(num) == float]
print('Con enteros o reales:', int_o_float)

# Genera lista de listas a partir de una tupla.
lista1 = [[num, num ** 2] for num in tupla]
print('\nLista de listas:', lista1)
# Genera lista de tuplas a partir de una lista.
lista2 = [(num, num / 2, num * 2) for num in lista_pares]
print('Lista de tuplas:', lista2)
# Genera lista de listas a partir de una cadena.
lista3 = [[letra, letra.upper()] for letra in frase]
print('Lista de listas:', lista3)

# Genera una lista operando con elementos de una lista y de una tupla.
lista4 = [x + y for x in tupla for y in lista_pares]
print('\nLista a partir de tupla y lista:', lista4)
# A partir de una lista de listas deja todos los elementos al mismo nivel.
lista5 = [x + 1 for sublista in lista1 for x in sublista]
print('Se pierde el anidamiento de listas:', lista5)
# Conserva los niveles de anidamiento que hay en la lista de listas.
lista6 = [[x + 1 for x in sublista] for sublista in lista1]
print('Se mantiene el nivel de anidamiento:', lista6)

# Se genera una lista de listas sin usar listas por comprensión.
lista7 = []
for sublista in lista1:
    lista = []
    for x in sublista:
        lista.append(x + 1)
    lista7.append(lista)
print('\nLista generada con 2 ciclos for:', lista7)
