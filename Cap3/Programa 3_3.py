# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.3
Se cuenta con un diccionario que representa claves y precios de productos.
Se incrementan los precios de acuerdo a su clave y se genera un
reporte de los productos. 
"""

def aumenta_precio(dic, inferior, superior, aumento):
    """ Aumenta los precios de los elementos cuyas claves estén 
    comprendidas en cierto intervalo.    
    Parámetros:
        dic: de tipo dict. Almacena claves (int) y precios de productos.
        inferior: de tipo int. Límite inferior.
        superior: de tipo int. Límite superior.
        aumento: de tipo int o float. Es el aumento.
    """
    aumento /= 100
    for clave in dic:
        if clave >= inferior and clave <= superior:
            dic[clave] *= (1 + aumento)
            
def imprime_dic(dic, titulo):
    """ Genera un reporte con un título y el contenido de un diccionario,
    previamente ordenado.    
    Parámetros:
        dic: de tipo dict. Lo que se va a incluir en el reporte. 
        titulo: de tipo str. Es el título del reporte.
    Regresa: 
        Una cadena que almacena las claves y los precios de los productos.
    Lanza:
        ValueError: si el diccionario está vacío.
    """
    if len(dic) > 0:
        reporte = '\n\n' + titulo.upper() + '\n'
        reporte += '\nClaves:      Precios:'
        items = sorted(dic.items())
        for clave, precio in items:
            reporte += f'\n  {clave} {precio:13.2f}$'
    else:
        raise ValueError('Diccionario vacío.')
    return reporte
    
# =============================================================================
# Prueba de las funciones.
# =============================================================================
# CP1: con un diccionario con datos.
prod_prec = {101: 17, 209: 23, 108: 35, 135: 41, 206: 30, 180: 24, 220: 31, 
             240: 50, 170: 38}
aumenta_precio(prod_prec, 150, 210, 5)
print('\nCP1: con un diccionario con datos.', end = '')
print(imprime_dic(prod_prec, 'Lista de precios actualizada'))
# CP2: con un diccionario vacío.
vacio = {}
aumenta_precio(vacio, 150, 210, 5)
try:
    print('\nCP2:', imprime_dic(vacio, 'Lista de precios actualizada'))
except Exception as error:
    print('\nCP2:', error)

            