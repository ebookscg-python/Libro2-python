# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.4
Se tiene un diccionario con nombres y teléfonos de amigos: una agenda.
El programa permite agregar amigos y teléfonos, cambiar y eliminar el 
teléfono de un amigo.
"""

def pide_opcion():
    """ Despliega opciones de trabajo con la agenda.
    Regresa:
        Una cadena que almacena la opción de trabajo elegida. 
    """
    opciones = {'A', 'C', 'E', 'T', 'a', 'c', 'e', 't'}
    opc = ''
    while opc not in opciones:
        print('\n¿Qué quieres hacer?')
        print('A: Alta de un nuevo amigo y su teléfono.')
        print('C: Cambiar el teléfono de un amigo.')
        print('E: Eliminar el teléfono de un amigo.')
        print('T: Terminar.')
        opc = input('Ingresa la opción elegida: ')
    return opc

amigos = {}
opcion = pide_opcion()
opcion = opcion.upper()
while opcion != 'T':   
    nombre = input('Nombre de tu amigo: ').upper()
    if opcion == 'A':       
        telef = input('Teléfono de tu nuevo amigo: ')
        amigos[nombre] = telef
    else:
        if nombre in amigos:
            if opcion == 'C':
                telef = input('Nuevo teléfono: ')
                amigos[nombre] = telef
            else:
                amigos[nombre] = None
        else:
            print('\nEse nombre no está registrado.')
    opcion = pide_opcion().upper()
print('\nLos amigos y sus teléfonos:', amigos)