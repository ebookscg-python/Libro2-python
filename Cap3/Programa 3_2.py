# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.2
Construye un diccionario formado por ítems donde la clave son las letras 
mayúsculas del abecedario y el valor su correspondiente minúscula. 
"""

# Usando listas por comprensión y el constructor dict.
letras = dict([(chr(n), chr(n).lower()) for n in range(65, 91)])
print('\nDiccionario may:min -->'.upper(), letras)

# Usando listas por comprensión, la función zip() y el constructor dict.
mayusculas = [chr(n) for n in range(65, 91)]
minusculas = [chr(n) for n in range(97, 123)]
dic = dict(zip(mayusculas, minusculas))
print('\nSegunda solución -->'.upper(), dic)