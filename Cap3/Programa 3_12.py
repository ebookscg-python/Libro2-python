# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.12
Cuenta e imprime el número de veces que aparece cada dato de una lista. 
"""

def llena_lista(nombre):
    """ Guarda en una lista los datos leídos de un archivo.
    Parámetro:
        nombre: de tipo str. Nombre del archivo de texto.
    Regresa:
        Una lista que almacena los datos leídos de un archivo. 
    Lanza:
        FileNotFoundError si no pudo abrir el archivo.
    """
    lista = list()
    try:
        with open(nombre, 'r') as arch:
            for elemento in arch:
                lista.append(elemento.strip())
        return lista
    except FileNotFoundError:
        raise FileNotFoundError('No se pudo abrir el archivo.')

def reporte_frecuencia(frecuencia):
    """ Genera un reporte con los datos de la frecuencia.
    Parámetro:
        frecuencia: de tipo dict. Almacena las frecuencias.
    Regresa:
        Una cadena con la información del diccionario.
    """
    reporte = '\nFrecuencia con la que aparece cada dato de la lista:\n'
    items = frecuencia.items()
    for dato, frec in items:
        reporte += f'{dato} -- {frec} vez/veces\n'
    return reporte

nom_arch = input('Ingrese el nombre del archivo: ')
try:
    lista = llena_lista(nom_arch)
except Exception as error:
    print(error)
else:
    frecuencia = dict()
    for elemento in lista:
        if elemento in frecuencia:
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1
    print(reporte_frecuencia(frecuencia))
    



