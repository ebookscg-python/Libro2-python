# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.9
Elimina los elementos de un arreglo que son múltiplos de un
valor dado.
Los datos del arreglo se leen de un archivo binario.
"""

import array
import arreglo

def elimina_multiplos(arrenum, numero):
    """ Elimina del arreglo todos los elementos que son múltiplos de numero.
    Parámetros:
        arrenum: de tipo array. Almacena datos numéricos.
        numero: número del mismo tipo que los elementos del arreglo. 
    """    
    n = len(arrenum)
    if n > 0:
        n -= 1
        indice = 0
        while indice < n:
            if arrenum[indice] % numero == 0:
                arrenum[indice] = arrenum.pop()
                n -= 1
            else:
                indice += 1
        # El último elemento no se evalúa en el ciclo.
        if arrenum[indice] % numero == 0:
                arrenum.pop()

# Existe un archivo llamado 'numeros' con, al menos, 10 números.
arre = array.array('b')
try:
    file_e = open('numeros', 'rb')
    arre.fromfile(file_e, 10) 
    file_e.close()  
    print('\nArreglo leído:', arreglo.a_cadena(arre)) 
    elimina_multiplos(arre, 3)
    print('Luego de eliminar los múltiplos de 3:', arreglo.a_cadena(arre)) 
except Exception as error:
    print('\nHubo un error:', error)
  
