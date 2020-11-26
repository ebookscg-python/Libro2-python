# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.8
Programa que ayuda a aprender los números del 1 al 10 en 
diferentes idiomas: inglés, italiano y francés.
"""
import random

# Lista con los nombres de los números del 0 al 10.
numeros = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 
           'siete', 'ocho', 'nueve', 'diez']
# Diccionario con las traducciones de los números a 3 idiomas: inglés, 
# italiano y francés, en ese orden.
traduc = {'cero': ('zero', 'zero', 'zéro'), 'uno': ('one', 'uno', 'un'), 
          'dos': ('two', 'due', 'deux'), 'tres': ('three', 'tre', 'trois'), 
          'cuatro': ('four', 'quattro', 'quatre'),
          'cinco': ('five', 'cinque', 'cinq'), 'seis': ('six', 'sei', 'six'),
          'siete': ('seven', 'sette', 'sept'), 
          'ocho': ('eight', 'otto', 'huit'),
          'nueve': ('nine', 'nove', 'neuve'), 'diez': ('ten', 'dieci', 'dix')}

# En cada iteración del while se elige el idioma.
texto = f'Idioma: (1)inglés, (2)italiano, (3)francés o (4)terminar: '
idioma = int(input(texto))
while idioma != 4:
    numero = random.randint(0, 10) 
    nom_num = numeros[numero]
    respuesta = input(f'¿Cómo se escribe {nom_num}?: ')
    posibles_resp = traduc[nom_num]  # Tupla con las 3 traducciones.
    traducida = posibles_resp[idioma - 1]  # Según el idioma.
    if respuesta == traducida:
        print('Muy bien:)')
    else:
        print('Falta estudiar:(')
    idioma = int(input(texto))
    
   
