# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 1.2
"""

def carga_lista(nom_arch):
    """ Lee los datos de un archivo de texto y los guarda en una lista.
    Cada dato se encuentra en una línea diferente del archivo.    
    Parámetro:
        nom_arch: de tipo str. Indica el nombre del archivo del 
        cual se leerán los datos.
    Regresa:
        Una lista con los datos leídos del archivo.
    Lanza:
        FileNotFoundError: si no se pudo abrir el archivo.        
    """ 
    try:
        resultado = []
        with open(nom_arch, 'r') as arch:        
            for dato in arch:
               resultado.append(dato.strip())  # Quita el salto de línea.
            return resultado       
    except FileNotFoundError:
        raise FileNotFoundError('No se pudo abrir el archivo.'.upper())
        
# =============================================================================
# Algunas pruebas para la función carga_lista()
# =============================================================================    
  
# CP1: se proporciona el nombre de un archivo que tiene valores válidos.
lista1 = carga_lista('escritores')
print('\nCP1:', lista1)
# CP2: se proporciona el nombre de un archivo vacío.
lista2 = carga_lista('pintores')
print('CP2:', lista2)
# CP3: se proporciona el nombre de un archivo que no fue creado.
try:
    lista3 = carga_lista('escultores')
    print('CP3:', lista3)
except Exception as error:
    print('CP3:', error)