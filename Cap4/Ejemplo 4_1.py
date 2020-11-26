# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 4_1
Declaración e inicialización de variables tipo arreglo.
"""

import array

print('\nPosibles códigos de tipo:', array.typecodes)

# Arreglo de enteros con signo, sin valores iniciales.
impares = array.array('b')
# Arreglo de enteros con signo. Valores iniciales a partir de una lista.
pares = array.array('b', [4, 12, -34, 48, -18]) 
# Arreglo de caracteres. Valores iniciales a partir de una cadena.
letras = array.array('u', 'hola')  
# Arreglo de números reales. Valores iniciales a partir de un conjunto.
arre1 = array.array('f', {18, 5.6, 99, 12.5})
# Arreglo de números enteros.
# Valores iniciales a partir de un diccionario: toma las claves.
arre2 = array.array('i', {118: 'queso', 124: 'yogur', 110: 'crema'}) 
# Arreglo de números enteros. Valores iniciales a partir de otro arreglo. 
arre3 = array.array('i', arre2)  

print('\nTipo de dato:', type(pares))
print('Impresión de una variable tipo arreglo:', pares)  
print('Impresión del contenido de un arreglo: ', end = '')
for num in pares:
    print(num, ' ', end = '')

# Acceso a uno de los elementos del arreglo.
print('\n\nPrimer elemento:', pares[0])
print('Último elemento:', pares[-1])
# Índice fuera de rango. Provoca: IndexError: array index out of range.
# print('Octavo elemento:', pares[7])


