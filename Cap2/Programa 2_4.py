# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 2.4
"""

# Solución 1: regresando una tupla de conjuntos.
def pares_impares1(conj):
    """ Genera dos subconjuntos, uno formado por números pares
    y otro con números impares.
    Parámetro:
        conj: de tipo set. Almacena números enteros.
    Regresa:
        Una tupla formada por dos conjuntos.
    """
    pares = set()
    impares = set()
    for num in conj:
        if num % 2 == 0:
            pares.add(num)
        else:
            impares.add(num)
    return pares, impares

# Solución 2: usando 2 de los parámetros para guardar los resultados.
def pares_impares2(conj, pares, impares):
    """...
    Parámetros:
        conj: de tipo set. Almacena números enteros.
        pares: de tipo set. Llega vacío y almacenará los números pares.
        impares: de tipo set. Llega vacío y almacenará los números impares.
    """
    for num in conj:
        if num % 2 == 0:
            pares.add(num)
        else:
            impares.add(num)

# =============================================================================
# Algunas pruebas de la función pares_impares1().
# =============================================================================
numeros = {1, 25, 53, 18, 32, 17, 41, 84, 46, 38, 52, 13, 57}
solopares = {22, 30, 18, 46, 54, 74}
vacio = set()
# CP1: se proporciona un conjunto con números pares e impares.
pares1, impares1 = pares_impares1(numeros)
print(f'\nCP1 --> Pares: {pares1} - Impares: {impares1}')
# CP2: se proporciona un conjunto solo con números pares.
pares2, impares2 = pares_impares1(solopares)
print(f'CP2 --> Pares: {pares2} - Impares: {impares2}')
# CP3: se proporciona un conjunto vacío.
pares3, impares3 = pares_impares1(vacio)
print(f'CP3 --> Pares: {pares3} - Impares: {impares3}')

# =============================================================================
# Algunas pruebas de la función pares_impares2().
# =============================================================================
# CP1: se proporciona un conjunto con números pares e impares.
pares1 = set()
impares1 = set() 
pares_impares2(numeros, pares1, impares1)
print(f'\nCP1 --> Pares: {pares1} - Impares: {impares1}')
# CP2: se proporciona un conjunto solo con números pares.
pares2 = set()
impares2 = set() 
pares_impares2(solopares, pares2, impares2)
print(f'CP2 --> Pares: {pares2} - Impares: {impares2}')
# CP3: se proporciona un conjunto vacío.
pares3 = set()
impares3 = set() 
pares_impares2(vacio, pares3, impares3)
print(f'CP3 --> Pares: {pares3} - Impares: {impares3}')
