# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 1.4
"""

def todos_son_multiplos(lista1, lista2):
    """ Determina si cada uno de los elementos de lista2 es múltiplo del
    correspondiente elemento de lista1 y, además, si las listas tienen la 
    misma longitud.   
    Parámetros:
        lista1: de tipo list. Almacena números.
        lista2: de tipo list. Almacena números.
    Regresa: 
        True si se cumplen las 2 condiciones, False en caso contrario.
    """ 
    if len(lista1) == len(lista2):       
        limite = len(lista1)
        indice = 0
        while indice < limite and lista1[indice] % lista2[indice] == 0:
            indice += 1
        respuesta = indice == limite
    else:
        respuesta = False
    return respuesta

def calcula_promedio(lista, n):
    """ Calcula y regresa el promedio de los números que están en posiciones
    que son múltiplos de n.       
    Parámetros:
        lista: de tipo list. Almacena números enteros o reales.
        n: de tipo int y es > 0.
    Regresa:
        El promedio de algunos números, elegidos por su posición.
    Lanza:
        ArithmeticError si no se puede calcular el promedio.
    """
    suma = 0
    contador = 0
    for i, elemento in enumerate(lista):
        if i % n == 0:
            suma += elemento
            contador += 1
    try:
        promedio = suma / contador
        return promedio
    except:
        raise ArithmeticError('No se puede calcular el promedio.')
    
# =============================================================================
# Algunas pruebas de las funcion todos_son_multiplos().
# =============================================================================
# CP1: se proporcionan dos listas de números, que cumplen con las condiciones.
lista1 = [9, 16, 15, 8, 21]
lista2 = [3, 2, 5, 8, 7]
if todos_son_multiplos(lista1, lista2):
    print('\nCP1: Sí cumplen las condiciones.')
else:
    print('\nCP1: No cumplen las condiciones.') 
# CP2: se proporcionan dos listas de números con distinta cantidad de elementos.
lista3 = [3, 2, 5, 8]
if todos_son_multiplos(lista1, lista3):
    print('CP2: Sí cumplen las condiciones.')  
else:
    print('CP2: No cumplen las condiciones.')  
# CP3: se proporcionan dos listas de números, de igual longitud, pero no todos 
# son múltiplos.
lista4 = [4, 2, 5, 8, 7]
if todos_son_multiplos(lista1, lista4):
    print('CP3: Sí cumplen las condiciones.')
else:
    print('CP3: No cumplen las condiciones.')
# =============================================================================
# Algunas pruebas de la función calcula_promedio().
# =============================================================================
# CP4: se proporciona una lista de números enteros.
lista1 = [11, -20, -7, 45, 10, -16, 14, 17]
prom1 = calcula_promedio(lista1, 2)
print('\nCP4 --> Promedio de enteros =', prom1)
# CP5: se proporciona una lista de números reales.
lista2 = [3.5, -2.8, 2.4, 1.5, -2.3, -3.1, -4.5, 5.2, 3.8, 6.0]
prom2 = calcula_promedio(lista2, 3)
print('CP5 --> Promedio de reales =', prom2) 
# CP6: se proporciona una lista vacía.
lista3 = []
try:
    prom3 = calcula_promedio(lista3, 3)
    print('CP6 --> Promedio (lista vacía) =', prom3)       
except ArithmeticError as error:
    print('CP6 -->', error)
    