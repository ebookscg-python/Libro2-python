# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 1.9
"""

def guarda_invitados(nom_arch, mensaje, lista):
    """ Guarda los elementos de la lista en un archivo.    
    Parámetro:
        nom_arch: de tipo str. Indica el nombre del archivo 
        en el cual se escribirán los elementos de la lista.
        mensaje: de tipo str. Es un título para el archivo.
        lista: de tipo list.  
    Lanza:
        FileNotFoundError: si no se puede abrir el archivo.        
    """ 
    try:
        with open(nom_arch, 'w') as arch:  
            arch.write(mensaje + '\n\n')
            for dato in lista:
                arch.write(dato + '\n')                
    except FileNotFoundError:
        raise FileNotFoundError('Error: archivo de salida.'.upper())
        
def carga_lista_ordenada(nom_arch):
    """ Lee los datos de un archivo de texto y los guarda en 
    una lista, dejándola ordenada de menor a mayor.
    Cada dato se encuentra en una línea diferente del archivo.    
    Parámetro:
        nom_arch: de tipo str. Indica el nombre del archivo.
    Regresa:
        La lista con los datos leídos, guardados en orden creciente.
    Lanza:
        FileNotFoundError: si no se puede abrir el archivo.        
    """ 
    try:
        invitados = []
        with open(nom_arch, 'r') as arch:        
            for dato in arch:
                dato = dato.strip().upper()
                res = busca_binaria(dato, invitados)
                if not res[0]:
                    invitados.insert(res[1], dato)
            return invitados       
    except FileNotFoundError:
        raise FileNotFoundError('Error: archivo de lectura.'.upper())
        
def busca_binaria(elemento, lista):
    """...
    """ 
    izquierdo = 0
    derecho = len(lista) - 1
    centro = (izquierdo + derecho) // 2
    while izquierdo <= derecho and lista[centro] != elemento:
        if lista[centro] > elemento:
            derecho = centro - 1
        else:
            izquierdo = centro + 1
        centro = (izquierdo + derecho) // 2
    if izquierdo > derecho:
        esta = False
        posicion = izquierdo
    else:
        esta = True
        posicion = centro
    return esta, posicion

# =============================================================================
# Uso de las funciones para dar solución al problema 1.9
# =============================================================================
archivo = input('Ingrese el nombre del archivo de invitados: ')
try:    
    cumple = carga_lista_ordenada(archivo)
    nombre = input('Ingrese otro invitado (para terminar, dé enter): ')
    while nombre:
        nombre = nombre.upper()
        res = busca_binaria(nombre, cumple)
        if not res[0]:
            cumple.insert(res[1], nombre)
        nombre = input('Ingrese otro invitado (para terminar, dé enter): ')
    archivo = input('Ingrese el nombre del archivo donde se guardará la lista: ')  
    titulo = input('Ingrese el título de la lista: ')
    try:
        guarda_invitados(archivo, titulo.upper(), cumple)
    except FileNotFoundError as error:
        print('\n', error)
except FileNotFoundError as error:
    print('\n', error)


