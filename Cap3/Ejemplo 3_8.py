# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 3_8
Paso de parámetros y diccionarios.
"""

def calcular(importe, descuento, iva): 
    """ Calcula el importe final a pagar por una compra.    
    Parámetros:
        importe: de tipo int o float. Indica el monto de la compra.
        descuento: de tipo int o float. Descuento que debe aplicarse.
        iva: de tipo int o float. % de IVA que debe retenerse.
    Regresa:
        El total a pagar.    
    """
    total = importe - (importe * descuento / 100) 
    total *= 1 + iva / 100
    return total

def suma_valores(**dic):
    """ Obtiene la suma de los valores de un diccionario.
    Parámetros:
        dic: de tipo dict en el cual el valor debe ser numérico. 
    Regresa:
        La suma de los valores del diccionario.    
    """
    suma = 0
    for _, valor in dic.items():
        suma += valor
    return suma
            
# =============================================================================
# Algunas pruebas de la función calcular().
# =============================================================================
# CP1: se proporciona un diccionario de acuerdo a lo esperado.
compra1 = {'descuento': 8.5, 'iva': 15, 'importe': 720} 
print(f'\nTotal a pagar = ${calcular(**compra1):.2f}')
# CP2: falta un dato. Da TypeError.
# compra2 = {'descuento': 8.5, 'importe': 720} 
# print(f'\nTotal a pagar = ${calcular(**compra2):.2f}')
# CP3: se proporciona un dato extra. Da TypeError.
# compra3 = {'descuento': 8.5, 'importe': 720, 'iva': 15, 'bono': 50} 
# print(f'\nTotal a pagar = ${calcular(**compra3):.2f}')
# CP4: clave no coincide con parámetro. Da TypeError.
# compra4 = {'desc': 8.5, 'importe': 720, 'iva': 15} 
# print(f'\nTotal a pagar = ${calcular(**compra4):.2f}')


# =============================================================================
# Algunas pruebas de la función suma_puntos().
# =============================================================================
# CP1: se proporcionan 3 parámetros por nombre con sus valores. 
print('\nSuma-1:', suma_valores(eq1 = 76, eq2 = 45, eq3 = 81))
# CP2: se proporcionan 4 parámetros por nombre con sus valores.
print('Suma-2:', suma_valores(a = 1, b = 2, c = 3, d = 4))
# CP3: se proporcionan 4 parámetros posicionales. Da TypeError.
# print('Suma-3:', suma_valores(11, 35, 44, 28))
