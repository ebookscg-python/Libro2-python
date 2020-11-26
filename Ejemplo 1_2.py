# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 1_2
Operaciones con listas.
"""

dias_laborables = ["lunes", "martes", "miércoles", "jueves", "viernes"]
colores_primarios = ['rojo', 'verde', 'azul']
precios = [205.30, 107.18, 25, 450, 310.89, 170.23, 340]

# =============================================================================
# Acceso a los elementos de las listas.
# =============================================================================
print('\nPrimer elemento:', dias_laborables[0])  # Imprime 'lunes'.
print('Último elemento:', dias_laborables[-1])  # Imprime 'viernes'.
print('Último desde la derecha:', dias_laborables[-5])  # Imprime 'lunes'.
# print(dias_laborables[-100])  # IndexError: list index out of range 

# =============================================================================
# Ejemplos de uso de los operadores + y *.
# =============================================================================
fin_semana = ['sábado', 'domingo']
# Concatena las listas en el orden dado.
semana = fin_semana + dias_laborables  
# Repite los elementos. El número debe ser un entero.
colores_repetidos = colores_primarios * 2  
# TypeError: can't multiply sequence by non-int of type 'float'
# precios_repetidos = precios * 3.5 
print('\nListas concatenadas:', semana)
print('Elementos repetidos:', colores_repetidos)

