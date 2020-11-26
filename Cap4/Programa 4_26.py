# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.29
Genera e imprime una espiral de tamaño n formada por los números
del 1 a n*n, siguiendo los movimientos de las agujas de un reloj.
"""
import matrices

def mueve_derecha(arre, inf, sup, fila, num):
    """ Asigna números en la fila desde la columna "inf" hasta la "sup",
    de izquierda a derecha.
    El número (num) se actualiza luego de cada asignación.
    Parámetros:
        arre: de tipo list. Lista de listas, es el arreglo bidimensional.
        inf: de tipo int. Indica la primera columna en la cual se asignará num.
        sup: de tipo int. Indica la última columna en la cual se asignará num.
        fila: de tipo int. Indica la fila en la cual se asignará num.
        num: de tipo int. Es el primer número que se asignará.
    Regresa:
        Un entero que indica el siguiente número que deberá asignarse.
    """
    while inf <= sup:
        arre[fila][inf] = num
        num += 1
        inf += 1
    return num

def mueve_izquierda(arre, inf, sup, fila, num):
    """ Asigna números en la fila desde la columna "sup" hasta la "inf",
    de derecha a izquierda.
    El número (num) se actualiza luego de cada asignación.
    Parámetros:
        arre: de tipo list. Lista de listas, es el arreglo bidimensional.
        inf: de tipo int. Indica la última columna en la cual se asignará
        el número (num).
        sup: de tipo int. Indica la primera columna en la cual se asignará
        el número (num).
        fila: de tipo int. Indica la fila en la cual se asignará el número.
        num: de tipo int. Es el primer número que se asignará.
    Regresa:
        Un entero que indica el siguiente número que deberá asignarse.
    """
    while sup >= inf:
        arre[fila][sup] = num
        num += 1
        sup -= 1
    return num

def mueve_abajo(arre, inf, sup, columna, num):
    """ Asigna números en la columna desde la fila "inf" hasta la "sup",
    de arriba hacia abajo.
    El número (num) se actualiza luego de cada asignación.
    Parámetros:
        arre: de tipo list. Lista de listas, es el arreglo bidimensional.
        inf: de tipo int. Indica la primera fila en la cual se asignará
        el número (num).
        sup: de tipo int. Indica la última fila en la cual se asignará
        el número (num).
        columna: de tipo int. Indica la columna en la cual se asignará el número.
        num: de tipo int. Es el primer número que se asignará.
    Regresa:
        Un entero que indica el siguiente número que deberá asignarse.
    """
    while inf <= sup:
        arre[inf][columna] = num
        num += 1
        inf += 1
    return num

def mueve_arriba(arre, inf, sup, columna, num):
    """ Asigna números en la columna desde la fila "sup" hasta la "inf",
    de abajo hacia arriba.
    El número (num) se actualiza luego de cada asignación.
    Parámetros:
        arre: de tipo list. Lista de listas, es el arreglo bidimensional.
        inf: de tipo int. Indica la última fila en la cual se asignará
        el número (num).
        sup: de tipo int. Indica la primera fila en la cual se asignará
        el número (num).
        columna: de tipo int. Indica la columna en la cual se asignará el número.
        num: de tipo int. Es el primer número que se asignará.
    Regresa:
        Un entero que indica el siguiente número que deberá asignarse.
    """
    while sup >= inf:
        arre[sup][columna] = num
        num += 1
        sup -= 1
    return num

n = int(input('\nIngrese el tamaño de la espiral (número impar > 0): '))
if n > 0 and n % 2 != 0:        
    espiral = matrices.forma_matriz_2(n, n)
    limite = n ** 2
    i = n // 2
    j = n // 2
    espiral[i][j] = 1
    i_max = i + 1
    i_min = i - 1
    j_max = j + 1
    j_min = j - 1
    num = 2
    derecha = True  # Indica desplazarse hacia la derecha.
    abajo = True  # Indica desplazarse hacia abajo.
    while num <= limite:        
        if derecha:
            j += 1
            if j_max == n:
                j_max -= 1
            num = mueve_derecha(espiral, j, j_max, i, num)
            j = j_max
            j_max += 1
        else:
            j -= 1
            num = mueve_izquierda(espiral, j_min, j, i, num)
            j = j_min
            j_min -= 1
        derecha = not derecha  # Alterna el movimiento horizontal.
        if num < limite:
            if abajo:
                i += 1
                num = mueve_abajo(espiral, i, i_max, j, num)
                i = i_max
                i_max +=1
            else:
                i -= 1         
                num = mueve_arriba(espiral, i_min, i, j, num)
                i = i_min
                i_min -= 1        
            abajo = not abajo  # Alterna el movimiento vertical.        
    cadena = ''    
    for f in range(0, n):
        for c in range(0, n):
            cadena += f'{espiral[f][c]}'.rjust(6) 
        cadena += '\n'            
    print(f'\nEspiral de {n} x {n}\n{cadena}')   
else:
    print('\nDato no válido.')
    
