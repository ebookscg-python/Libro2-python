# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.17
Procesa los datos de un concurso de pogramación:
    - clave del participante que sacó el puntaje más alto
    - clave del participante que sacó el puntaje más bajo.
    - promedio del puntaje obtenido por los participantes.
    - elimina a todos los participantes que hayan obtenido menos de 80 puntos.
    - total de participantes que pasan a la ronda final (80 o más puntos).
"""

import array
import arreglo

def elimina_menores_a_minimo(claves, puntajes, minimo):
    """ Elimina clave y puntaje de todos aquellos participantes que obtuvieron 
    menos de una cierta cantidad mínima de puntos. 
    No altera el orden de las claves.
    """
    n = len(claves) - 1
    indice = 0
    while indice < n:
        if puntajes[indice] < minimo:
            for i in range(indice, len(puntajes) - 1):
                puntajes[i] = puntajes[i + 1]
                claves[i] = claves[i + 1]
            puntajes.pop()
            claves.pop()
            n -= 1
        else:
            indice += 1
    if puntajes[indice] < minimo:  
        puntajes.pop()
        claves.pop()

claves = array.array('B')
puntajes = array.array('B')
TOTAL = 10
try:
    file_c = open('claves', 'rb')
    claves.fromfile(file_c, TOTAL) 
    file_p = open('puntajes', 'rb')
    puntajes.fromfile(file_p, TOTAL)     
    file_c.close()  
    file_p.close()  
except Exception as error:
    print('\nHubo un error:', error)
else:
    alto = arreglo.maximo(puntajes)
    print('\nClave del participante con más puntos:', claves[alto])
    bajo = arreglo.minimo(puntajes)
    print('Clave del participante con menos puntos:', claves[bajo])
    promedio = arreglo.suma_arreglo(puntajes) // TOTAL
    print(f'Promedio de puntos obtenidos en esta etapa = {promedio:.2f}')
    elimina_menores_a_minimo(claves, puntajes, 80)
    n = len(claves) 
    if n > 0:
        print(f'A la ronda final pasan {n} participantes.')
    else:
        print('Ningún participante superó la ronda. ')
        
        

