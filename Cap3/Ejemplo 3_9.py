# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 3_9
Solución del problema 3.8 sin usar diccionarios.
"""
import random

espanol = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 
          'siete', 'ocho', 'nueve', 'diez']
ingles = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 
          'eight', 'nine', 'ten']
italiano = ['zero', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 
            'otto', 'nove', 'dieci']
frances = ['zéro', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept',
           'huit', 'neuve', 'dix']
traduc = list(zip(ingles, italiano, frances))

# En cada iteración del while se elige el idioma.
texto = f'Idioma: (1)inglés, (2)italiano, (3)francés o (4)terminar: '
idioma = int(input(texto))
while idioma != 4:
    numero = random.randint(0, 10) 
    nom_num = espanol[numero]
    respuesta = input(f'¿Cómo se escribe {nom_num}?: ')
    posibles_resp = traduc[numero]  # Tupla con las 3 traducciones.
    traducida = posibles_resp[idioma - 1]  # Según el idioma.
    if respuesta == traducida:
        print('Muy bien:)')
    else:
        print('Falta estudiar:(')
    idioma = int(input(texto))

