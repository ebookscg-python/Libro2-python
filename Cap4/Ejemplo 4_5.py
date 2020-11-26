# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 4_5
Ejemplos de algunas operaciones con arreglos bidimensionales.
"""

import matrices

# =============================================================================
# Construcción e inicialización de arreglos bidimensionales.
# =============================================================================
f1 = int(input('\nIngrese total de filas: '))
c1 = int(input('Ingrese total de columnas: '))
m1 = matrices.forma_matriz_1(f1, c1)
print(f'\nUsando la función 1:\n{matrices.a_cadena(m1)}')

f2 = int(input('\nIngrese total de filas: '))
c2 = int(input('Ingrese total de columnas: '))
m2 = matrices.forma_matriz_2(f2, c2)
print(f'\nUsando la función 2:\n{matrices.a_cadena(m2)}')

f3 = int(input('\nIngrese total de filas: '))
c3 = int(input('Ingrese total de columnas: '))
m3 = matrices.forma_matriz_3(f3, c3)
print(f'\nUsando la función 3:\n{matrices.a_cadena(m3)}')

# =============================================================================
# Acceso a arreglos bidimensionales.
# =============================================================================
# Se modifica el valor de la casilla del extremo superior izquierdo.
m2[0][0] = 5  

# Se modifica el valor de la última fila.
m2[f2 - 1] = [8, 9]

# Se agrega una nueva fila.
m2.insert(1, [2, 4])
print(f'\nLuego de modificar algunas casillas y de agregar una fila:\n'
      f'{matrices.a_cadena(m2)}')

# Se elimina la primera fila.
del m2[0] 
print(f'\nLuego de eliminar la primera fila:\n{matrices.a_cadena(m2)}')




