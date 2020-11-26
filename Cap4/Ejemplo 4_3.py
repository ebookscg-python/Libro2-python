# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 4_3
Funciones y operadores con arreglos.
Subdivisión de arreglos.
"""
import array
import arreglo

letras = array.array('u', 'susurros') 
pares = array.array('b', [4, 12, -34, 48, -18]) 
impares = array.array('b', [17, 21, 13, 5, 47, 53]) 

conv = pares.tobytes()
print('\nLuego de convertir a bytes: ', end = '')
print(arreglo.a_cadena(conv))

lista = letras.tolist()
print('\nLista obtenida:', lista)

# Genera un nuevo arreglo con los elementos de los 2 arreglos.
numeros = pares + impares
print('\nNuevo arreglo: pares + impares.')
print(arreglo.a_cadena(numeros))

# Genera un nuevo arreglo con los elementos de impares repetidos 2 veces.
nuevo = impares * 2
print('\nNuevo arreglo: elementos de impares repetidos 2 veces.')
print(arreglo.a_cadena(nuevo))

# Repite 3 veces los elementos de pares y modifica a pares. 
pares *= 3
print('\nPares luego de repetir 3 veces su contenido.')
print(arreglo.a_cadena(pares)) 

# Subdivisión o partición (slicing) de arreglos.
print('\nDel tercero al quinto:', arreglo.a_cadena(nuevo[2:5]))
print('\nDesde el primero (ignora los últimos 5):', arreglo.a_cadena(nuevo[:-5]))
print('\nDesde el cuarto (ignora los últimos 5):', arreglo.a_cadena(nuevo[3:-5]))
print('\nDesde el cuarto hasta el final:', arreglo.a_cadena(nuevo[3:]))
print('\nTodo el arreglo:', arreglo.a_cadena(nuevo[:]))   
print('\nTomando de 2 en 2, del primero al último:', arreglo.a_cadena(nuevo[::2]))     
     
    

