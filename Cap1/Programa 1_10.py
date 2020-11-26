# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 1.10
"""

def nombres_sin_espacios(lista):
    """ Genera una lista con los elementos de la lista recibida 
    que no contengan espacios en blanco.    
    Parámetro:
        lista: de tipo list. Almacena cadenas de caracteres.
    Regresa: 
        Una lista que almacena cadenas de caracteres.
    """ 
    resultado = [ele for ele in lista if ele.find(' ') == -1]
    return resultado

# =======================================================================
# Algunas pruebas de la función nombres_sin_espacios()  
# =======================================================================
# CP1: algunas cadenas contienen espacios en blanco.
ciudades = ['Bogotá', 'Buenos Aires', 'México', 'Caracas', 'San Salvador', 'Río de Janeiro']
print('\nCP1:', nombres_sin_espacios(ciudades))
# CP2: algunas cadenas contienen espacios en blanco.
platillos = ['mousse de chocolate', 'sopa', 'hamburguesa', 'papas fritas', 'cocido']
print('CP2:', nombres_sin_espacios(platillos))
# CP3: las cadenas no contienen espacios en blanco.
colores = ['rojo', 'verde', 'blanco', 'amarillo']
print('CP3:', nombres_sin_espacios(colores))
# CP4: se proporciona una lista vacía.
vacia = []
print('CP4:', nombres_sin_espacios(vacia))
