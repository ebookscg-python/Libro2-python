# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 4_4
Arreglos y  archivos binarios.
"""

import array

# =============================================================================
# Ejemplo 1: se guarda un arreglo numérico en un archivo binario.
# =============================================================================
arre = array.array('b')
file_s = open('numeros', 'wb')
n = int(input('\nTotal de números: '))
for _ in range (0, n):
    num = int(input('¿Números?: '))
    arre.append(num)
arre.tofile(file_s)
file_s.close()

# =============================================================================
# Ejemplo 2: se guarda un arreglo de caracteres en un archivo binario.
# =============================================================================
letras = array.array('u', 'tres tristes tigres comen trigo')
file_s = open('letras', 'wb')
letras.tofile(file_s)
file_s.close()

# =============================================================================
# Ejemplo 3: se agregan al archivo de letras el contenido del arreglo
# de vocales.
# =============================================================================
vocales = array.array('u', 'aeiou')
file_a = open('letras', 'ab')
vocales.tofile(file_a)
file_a.close()

# =============================================================================
# Ejemplo 4: se lee un arreglo de números desde un archivo binario.
# =============================================================================
numeros = array.array('b')
file_e = open('numeros', 'rb')
numeros.fromfile(file_e, n)
print(numeros)

# =============================================================================
# Ejemplo 5: se lee un arreglo de caracteres desde un archivo binario.
# =============================================================================
caracteres = array.array('u')
file_e = open('letras', 'rb')
caracteres.fromfile(file_e, 36)
print(caracteres)