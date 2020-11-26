# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.12
Programa en el cual se lee un arreglo desde un archivo binario, se lo ordena 
y se lo utiliza para probar la solución de la función pedida en el problema
4.12.
"""
import arreglo
import array
     
arre = array.array('b')
try:
    file_e = open('numeros', 'rb')
    arre.fromfile(file_e, 15) 
    file_e.close()  
except Exception as error:
    print('\nHubo un error:', error)
else:
    arreglo.ordena_crec(arre)
    print('\nArreglo:', arreglo.a_cadena(arre)) 
    # CP1: se dan datos que no provocan errores.
    arreglo.cambia_ordenado(arre, 21, 25)
    print('\nCP1: se cambió 21 por 25 -->', arreglo.a_cadena(arre)) 
    # CP2: el segundo dato altera el orden.
    try:
        arreglo.cambia_ordenado(arre, 14, 17)
        print('CP2: se cambió 14 por 17 -->', arreglo.a_cadena(arre)) 
    except Exception as error:
        print('CP2: se intentó cambiar 14 por 17 -->', error)
    # CP3: el dato a cambiar no está en el arreglo.
    try:
        arreglo.cambia_ordenado(arre, 4, 3)
        print('CP3: se cambió 4 por 3 -->', arreglo.a_cadena(arre)) 
    except Exception as error:
        print('CP3: se intentó cambiar 4 por 3 -->', error)
    # CP4: el dato que se va a cambiar es el primero.
    arreglo.cambia_ordenado(arre, 5, 3)
    print('CP4: se cambió 5 por 3 -->', arreglo.a_cadena(arre)) 
    # CP5: el dato que se va a cambiar es el último.
    arreglo.cambia_ordenado(arre, 44, 51)
    print('CP5: se cambió 44 por 51 -->', arreglo.a_cadena(arre))
