# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 1_9.
Ejemplos de uso de las funciones flter(), map() y zip(). 
"""

def multiplo_de4(numero):
    return numero % 4 == 0

def cubo(x):
    return x ** 3

def es_mayusc(c):
    return c.isupper()

def conv_mayus(c):
    res = c
    if c.islower():
        res = c.upper()
    return res

numeros = [2, 5, 8, 3, 12, 20, 31, 4, 16]
potencias = [4, 2, 2, 3, 2, 2, 1]
cadena = 'Juan baila'

# Uso del filter.
fil_lista = list(filter(multiplo_de4, numeros))
print('\n"Filter" aplicado a una lista:', fil_lista)
fil_cadena = list(filter(es_mayusc, cadena))
print('"Filter" aplicado a una cadena:', fil_cadena)

# Uso del map.
map_lista = list(map(cubo, numeros))
print('\n"Map" aplicado a una lista:', map_lista)
print('"Map" aplicado a una cadena: ', end = '')
for i in map(conv_mayus, cadena):
    print(i, end = '')
print('\n"Map" usando una función con 2 parámetros: ', end = '')
for n in map(pow, numeros, potencias):
    print(n, end = ' ')

# Uso del zip.
print('\n\nEjemplos de uso del zip'.upper())
preguntas = ['Nombre del abuelo', 'Comida preferida', 'Lugar de vacaciones']
respuestas = ['Alberto', 'risotto', 'playa']
for pre, resp in zip(preguntas, respuestas):
    print(f'¿{pre}?: {resp}')
ferreteria = ['martillo', 'clavo', 'tenaza', 'destornillador', 'taladro']
precios = [250, 1.2, 380.5, 195.3, 1500]
precio_max = 0
for material, precio in zip(ferreteria, precios):
    if precio > precio_max:
        precio_max = precio
        mat_max = material
print(f'\nEl/la {mat_max} es la herramienta más cara. Cuesta ${precio_max}.')
num_pot = [valor for valor in zip(numeros, potencias)]
print('\n"Zip" aplicado a dos listas de diferente longitud:', num_pot)
tupla = tuple(ele for ele in zip((1, 3, 5), (2, 4, 6)))    
print('\n"Zip" aplicado a dos tuplas:', tupla)  
resul = ''
for c1, c2 in zip('AEIOU', 'aeiou'):
    resul += c1 + '-' + c2 + ' '
print('\n"Zip" aplicado a dos cadenas:', resul)

 