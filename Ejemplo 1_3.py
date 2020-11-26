# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 1_3
Funciones predefinidas para trabajar con  listas.
Ejemplos de uso.
"""

dias_laborables = ["lunes", "martes", "miércoles", "jueves", "viernes"]
colores_primarios = ['rojo', 'verde', 'azul']
precios = [205.30, 107.18, 25, 450, 310.89, 170.23, 340]
pares = list(range(0, 30, 2))
impares = list(range(29, 0, -2))
colores_repetidos = colores_primarios * 2 

# =============================================================================
# Algunas funciones para el manejo de listas.
# =============================================================================
dias_laborables.append('sábado')  # Agrega sábado al final de la lista.
print('\nSemana laborable con un día extra =', dias_laborables)
# Cuenta el número de veces que aparece lunes en la lista. 
print(f"\nEl lunes aparece = {dias_laborables.count('lunes')} vez (veces).")
# Regresa el total de elementos que tiene la lista.
print('Total de precios =', len(precios))
# Agrega en la primera posición el valor blanco.
colores_primarios.insert(0, 'blanco')  
print('\nLista con un nuevo elemento:', colores_primarios)
# No existe la posición 10. Lo inserta al final.
colores_primarios.insert(10, 'amarillo')  
print('Lista con un nuevo elemento:', colores_primarios)
# Agrega al final de la lista todos los elementos de la lista impares.
pares.extend(impares)  
print('\nLista de pares extendida con la lista impares:', pares)
# Quita el valor sábado de la lista.
dias_laborables.remove('sábado')
print('\nVolviendo a la normalidad =', dias_laborables)
# Regresa la posición de rojo dentro de la lista.
print('\nPosición del rojo:', colores_primarios.index('rojo'))
print('Posición del segundo azul:', colores_repetidos.index('azul', 3))
# Da el error: ValueError: 'gris' is not in list
# print('Posición del gris:', colores_repetidos.index('gris'))  
# Ordena los elementos de la lista de menor a mayor.
precios.sort()
print('\nPrecios ordenados de menor a mayor:', precios)
# Ordena los elementos de la lista de mayor a menor.
colores_repetidos.sort(reverse = True)
print('Colores ordenados de mayor a menor:', colores_repetidos)
# Genera una nueva lista ordenada, sin alterar la lista original.
lista_ordenada = sorted(dias_laborables)
lis_ord_long = sorted(dias_laborables, key = len)
print('\nDías laborables sin alterar:', dias_laborables)
print('Días laborables ordenados:', lista_ordenada)
print('Días laborables ordenados por longitud:', lis_ord_long)
# Invierte el orden de los elementos de la lista.
impares.reverse()
print('\nImpares en orden inverso:', impares)
# Quita y regresa el elemento de la posición 0.
quitado = colores_primarios.pop(0)
print('\nEl elemento quitado es:', quitado)
print('La lista quedó:', colores_primarios)
rescatado = dias_laborables.pop()  # Sin posición: quita el último.
print('Se rescató para el fin de semana:', rescatado)
print('Los días laborables quedaron:', dias_laborables)
# print(precios.pop(10))  # IndexError: pop index out of range
# Quita todos los elementos de la lista, dejándola vacía.
precios.clear()
print('\nLa lista de precios quedó vacía:', precios)
# print(precios.pop())  IndexError: pop from empty list
# Quita el segundo elemento de la lista.
del colores_primarios[1]
print('\nColores primarios luego de quitar el segundo elemento:', colores_primarios)