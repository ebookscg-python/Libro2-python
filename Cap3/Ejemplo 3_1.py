# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 3_1
Construcción de diccionarios.
"""

# La clave es una cadena.
num_meses = {'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6}
print('\n', num_meses)
# La clave es un entero.
nom_meses = {1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril', 5: 'mayo', 6: 'junio'}
print(nom_meses)
# Genera un diccionario con las claves tomadas de la lista y el valor 5.
puntaje = {}.fromkeys(['futbol', 'basquetbol', 'tenis', 'natación'], 5)
print(puntaje)
frutas = {'manzana': 34, 'pera': 45}
print('\nEl tipo es:', type(frutas))  # Imprime <class 'dict'>

# Uso del constructor dict para construir diccionarios.
# Por medio de una lista de tuplas.
dic1 = dict([('La Paz', 13), ('Lima', 27), ('Caracas', 30), ('Montevideo', 23)])
print('\nCon lista de tuplas:', dic1)
# Por medio de una lista por comprensión.
dpares = dict([(n, n ** 3) for n in range(1, 5)])
print('Con lista por comprensión:', dpares)
# Usando parámetros de palabras claves. 
dic2 = dict(juan = 56287041, irene = 98741245)
print('Con parámetros de palabras claves:', dic2)
# Por medio de un diccionario.
dic3 = dict({'irene': 98741245, 'juan': 56287041})
print('Con un diccionario:', dic3)
