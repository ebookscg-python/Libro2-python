# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 3_4
Recorrido de los elementos de un diccionario.
Métodos: keys(), values(), items().
Diccionarios y listas.
"""

num_meses = {'ene': 1, 'feb': 2, 'mar': 3, 'abr': 4, 'may': 5, 'jun': 6}
menu = {'helado': 25, 'tarta': 43, 'galleta': 12, 'merengue': 18}

# Recorrido de diccionarios usando el ciclo for.
for mes in num_meses:
    print(mes, ' ', end = '')
suma = 0
for postre in menu:
    suma += menu[postre]
print('\nSuma de los precios de los postres: $', suma)

# Métodos: keys(), values(), items().
claves = menu.keys()
print('\nTipo de keys():', type(claves))
print('Claves 1-:', claves)
menu['gelatina'] = 24  # Agrega un ítem al diccionario.
print('Claves 2-:', claves)  # Modificado por la inserción de arriba.

valores = menu.values()
print('\nTipo de values():', type(valores))
print('Valores 1-', valores)
menu['galleta'] = 16  # Modifica el valor.
print('Valores 2-', valores)  # Modificado por la actualización de arriba.

items = num_meses.items()
print('\nTipo de items():', type(items))
print('Items 1-', items)
del num_meses['mar']  # Borra el ítem.
print('Items 2-', items)  # Modificado por la eliminación de arriba.

# Regresa el total de elementos de la vista.
print('\nTotal de claves:', len(claves))
print('Total de ítems:', len(items))

# Ordena los elementos de la vista de acuerdo con la clave.
menu_ordenado = sorted(menu.items())  # Genera lista de tuplas.
print('\nMenú ordenado:', menu_ordenado)
# Otra manera de ordenar, usando el constructor dict.
meses_ordenados = dict(sorted(num_meses.items()))  # Genera diccionario.
print('Meses ordenados:', meses_ordenados)

# Uso del operador de membresía en las vistas.
if 'galleta' in claves:  # Valor posible de clave.
    print('\nSí hay galletas.')
else:
    print('\nNo hay galletas.')
if ('alfajor', 31) in items:  # Valor posible de ítem.
    print('Sí hay alfajores a $31.')
else:
    print('No hay alfajores a $31.')
if ('gelatina', 31) in items:  # Valor posible de ítem.
    print('Sí hay gelatinas a $31.')
else:
    print('No hay gelatinas a $31.')
    
# Iteración usando clave y valor de cada ítem.
print()
for mes, num in items:
    print(f'El mes {mes} es el {num} del año.')
suma_precios = 0
for precio in valores:
    suma_precios += precio
print('\nSuma de los precios de los postres = $', suma_precios)

# Constructor list() aplicado al diccionario.
lista_menu = list(menu)
print('\nLista generada con el diccionario:',lista_menu)

# Construcción de listas a partir de las vistas de diccionarios.
lista_claves = list(claves)  # Genera lista de cadenas.
print('\nLista de claves:', lista_claves)    
lista_items = list(items)  # Genera lista de tuplas.
print('Lista de ítems:', lista_items)   

# Se obtienen listas ordenadas de menor a mayor.
claves_ord = sorted(lista_claves)
print('\nLista de claves ordenadas:', claves_ord)
valores_ord = sorted(valores)
print('Lista de valores ordenados:', valores_ord)
items_ord = sorted(lista_items)
print('Lista de ítems ordenados:', items_ord)


