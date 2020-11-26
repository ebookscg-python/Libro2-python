# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.1
Determina si la frase contiene a las 5 vocales, cuántas veces la letra "m"
está en la frase y, por último, quita todas las letras "t".
"""
import array

frase = input('Ingrese la frase que quiere analizar: ')
arreglo = array.array('u', frase)
try:   
    arreglo.index('a') 
    arreglo.index('e') 
    arreglo.index('i') 
    arreglo.index('o') 
    arreglo.index('u')
    respuesta = True
except:
    respuesta = False
if respuesta:
    print('\nLa frase contiene las 5 vocales.')
else:
    print('\nLa frase no contiene las 5 vocales.')
cuenta_m = arreglo.count('m')
if cuenta_m > 0:
    print(f'La letra "m" aparece: {cuenta_m} veces.')    
else:
    print(f'La letra "m" no aparece en la frase.') 
cuenta_t = arreglo.count('t')
for _ in range(0, cuenta_t):
    arreglo.remove('t')
print('La frase luego de quitar todas las "t":'.upper())
for letra in arreglo:
    print(letra, end = '')

    


