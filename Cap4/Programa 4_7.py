# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.8
A partir de un número entero, genera e imprime el mayor y el menor
de los números que se pueden formar con los dígitos del número.
"""

import array
import arreglo

def forma_mayor(arre):
    """Genera y regresa un número entero a partir de los 
    datos que almacena el arreglo, de izquierda a derecha.
    Parámetro:
        arre: de tipo array. Almacena números enteros de un dígito.
    Regresa:
        El mayor número entero que se puede formar con los dígitos que 
        almacena el arreglo. 
    """
    numero = 0
    for n in arre:
        numero = numero * 10 + n
    return numero 

def forma_menor(arre):
    """Genera y regresa un número entero a partir de los 
    datos que almacena el arreglo, de derecha a izquierda.
    Parámetro:
        arre: de tipo array. Almacena números enteros de un dígito.
    Regresa:
        El menor número entero que se puede formar con los dígitos que 
        almacena el arreglo. 
    """
    numero = 0
    for i in range(len(arre) - 1, -1, -1):
        numero = numero * 10 + arre[i]
    return numero         

arre_digitos = array.array('b')
numero = int(input('\nIngrese un número entero: '))
while numero > 0:
    digito = int(numero % 10)
    arre_digitos.append(digito)
    numero //= 10
arreglo.ordena_decrec(arre_digitos)   
mayor = forma_mayor(arre_digitos)
menor = forma_menor(arre_digitos)
print('\nEl mayor número que puede formarse =', mayor)
print('El menor número que puede formarse =', menor)