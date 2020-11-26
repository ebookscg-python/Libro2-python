# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.25
Genera e imprime un cuadrado mágico.
"""

import matrices

def cuadrado_magico(n):
    """ Genera un cuadrado mágico de tamaño n.
    Parámetro:
        n: de tipo int. Indica el total de filas y columnas del cuadrado.
        Debe ser impar y > 0.
    Regresa: 
        Lista de listas que almacena el cuadrado mágico.
    """
    cuadrado = matrices.forma_matriz_2(n, n)
    f = 0
    c = n // 2
    for i in range(1, n ** 2 + 1):
        cuadrado[f][c]= i    
        if i % n != 0:
            f -= 1
            c += 1
            if f < 0:
                f = n - 1
            if c == n:
                c = 0
        else:
            f += 1       
    return cuadrado
  
def verifica_cuadrado_magico(cuadrado, n):
    """ Verifica que el cuadrado cumpla con la característica de que
    la suma de sus diagonales, filas y columnas son iguales.
    Parámetros:
        cuadrado: de tipo list. Lista de listas. Almacena el cuadrado mágico.
        n: de tipo int. Es el tamaño del cuadrado.
    Regresa:
        True si la matriz es un cuadrado mágico y False en otro caso.
    """    
    respuesta = False
    suma = matrices.suma_diagonal_principal(cuadrado)
    if suma == matrices.suma_diagonal_secundaria(cuadrado):
        fila = 0
        while fila < n and suma == matrices.suma_fila(cuadrado, fila):
            fila += 1
        if fila == n:
            col = 0
            while col < n and suma == matrices.suma_columna(cuadrado, col):
                col += 1
            respuesta = col == n
    return respuesta
    
n = int(input('\nIngrese tamaño del cuadrado mágico: '))
if n > 0 and n % 2 != 0:
    c_magico = cuadrado_magico(n)
    if verifica_cuadrado_magico(c_magico, n):
        print(f'\nSe generó un cuadrado mágico de {n} x {n}\n'.upper())
        print(matrices.a_cadena(c_magico))
    else:
        print('\nEl cuadrado generado no reúne las características solicitadas.')
else:
    print('\nDebe ingresar un número entero positivo impar.')
    