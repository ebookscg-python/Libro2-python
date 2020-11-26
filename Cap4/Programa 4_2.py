# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.2
En un arreglo de números enteros agrega a cada número par su cuadrado 
a su derecha. Además, imprime el arreglo modificado.
"""
import array

def agrega_cuadrados(arreglo):
    """ A cada número par del arreglo le agrega, a su derecha, su cuadrado.
    Parámetro:
        arreglo: de tipo array. Almacena números enteros.
    """
    n = len(arreglo)
    indice = 0
    for _ in range(0, n):
        if numeros[indice] % 2 == 0:
            cuadrado = numeros[indice] ** 2
            indice += 1
            numeros.insert(indice, cuadrado)
        indice += 1

# Entrada de datos, llamada a la función e impresión de resultado.
numeros = array.array('i')
n = int(input('\n¿Cuántos números? '))
for _ in range(0, n):
    num = int(input('Ingrese un número entero: '))
    numeros.append(num)
agrega_cuadrados(numeros)
res = '\nArreglo luego de agregar cuadrados:\n'
for num in numeros:
    res += str(num) + ' '
print(res)

