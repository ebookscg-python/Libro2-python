# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 2_4
Comnbinación del método update() con las operaciones de
intersección, diferencia y diferencia simétrica.
"""

colores_primarios = {'rojo', 'verde', 'azul'}
colores = {'gris', 'verde', 'azul', 'blanco', 'amarillo', 'negro'}
vocales = {'a', 'e', 'i', 'o', 'u'}
letras = {'g', 'o', 'm', 'b', 'e', 'a', 't', 'y', 'r', 'p', 'c', 'j'}

# Actualiza el conjunto con el resultado de la intersección.
colores.intersection_update(colores_primarios)
print('\nActualización con intersección:', colores)

# Actualiza el conjunto con el resultado de la diferencia simétrica.
vocales.symmetric_difference_update(letras)
print('\nActualización con diferencia simétrica:', vocales)

# Actualiza el conjunto con el resultado de la diferencia.
letras.difference_update(vocales)
print('\nActualización con diferencia:', letras)