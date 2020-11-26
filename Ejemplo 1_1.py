# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 1_1
Declaración e inicialización de variables de tipo list.
"""

# =============================================================================
# Usando los [] y dando valores para inicializar las listas.
# =============================================================================
dias_laborables = ["lunes", "martes", "miércoles", "jueves", "viernes"]
print('Lista de días laborables:', dias_laborables)
colores_primarios = ['rojo', 'verde', 'azul']
print('Lista de colores:', colores_primarios)
precios = [205.30, 107.18, 25, 450, 310.89, 170.23, 340]
print('Lista de precios:', precios)
print('El tipo es:', type(precios))
mezcolanza = [12, 'octubre', 1492, 'llegó Colón'] 
print('Lista con diferentes tipos de datos:', mezcolanza)
vacia1 = []
print('\nLista vacía-1:', vacia1)

# Se genera una lista vacía usando el constructor list() sin parámetros.
vacia2 = list()
print('Lista vacía-2:', vacia2)

# Se genera una lista a partir de un rango.
pares = list(range(0, 30, 2))
print('\nPares menores a 30:', pares)
impares = list(range(29, 0, -2))
print('\nImpares menores a 30:', impares)

# Se genera una lista con los caracteres de una cadena de caracteres.
caracteres = list('2020 es bisiesto')
print('\nLista de caracteres:', caracteres)

# Se genera una lista con subcadenas de una cadena de caracteres.
frase = '''La emigración no solo se hace para huir de la opresión en casa, 
sino también para llegar a lo más hondo de nuestra alma.'''  # Autor: Orhan Pamuk
palabras = frase.split()  # Si no se da parámetro, se toma el ' '.
print('\nLista de palabras:', palabras)

# Se genera una lista con los elementos de una tupla.
con_tuplas = list((6, 3, 8, 12, 15))
print('\nLista con los elementos de la tupla:', con_tuplas)

# Se genera una lista con los elementos de otra lista.
otra_lista = list(precios)
print('\nTengo lo mismo, pero soy otra lista:', otra_lista)

