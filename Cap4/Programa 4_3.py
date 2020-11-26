# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.3
Elimina del arreglo todos aquellos elementos que sean menores que el promedio
de los valores almacenados, si el promedio es mayor o igual a 50.
"""
import array

n = int(input('¿Cuántos participantes hay en el concurso de baile?: '))
if n > 0:
    puntajes = array.array('B')
    suma = 0
    for i in range(1, n + 1):
        puntos = int(input(f'Ingrese el puntaje del participante {i}: '))
        puntajes.append(puntos)
        suma += puntos
    promedio = suma / n
    if promedio >= 50:
        indice = 0
        while indice < n:
            if puntajes[indice] < promedio:
                puntajes.pop(indice)
                n -= 1
            else:
                indice += 1
        print(f'\nQuedaron los {n} mejores puntajes y son: ')
        for i in range(0, n):
            print(puntajes[i], ' ', end = '')
    else:
        print(f'\nEl promedio es: {promedio:.2f}. No hubo cambios.')
    
    

