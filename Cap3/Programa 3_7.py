# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.7
Se define un diccionario para guardar los datos de los socios de un club. 
Además, el programa debe:
1.	Dar de alta nuevos socios.
2.	Dar de baja un socio.
3.	Consultar los datos de un cierto socio.
4.	Generar la lista completa de socios con todos sus datos.
5.	Generar la lista de los socios honoríficos: nombre y teléfono.

"""

def alta_socio(socios, clave, nombre, telefono, correo, honor):
    """ Agrega un nuevo socio al diccionario.
    ...
    """
    socios[clave] = {'Nombre': nombre, 'Teléfono': telefono, 'Correo': correo, 'Honor': honor}
      
def baja_socio(socios, clave):
    """ Da de baja un socio, dada su clave.
    ...
    """
    if socios.get(clave):
        del socios[clave]
        
def reporte_socios(socios):
    """ Genera un reporte con los datos de todos los socios.
    ...
    """
    reporte = '\nLISTA DE SOCIOS\n'
    items = socios.items()
    for cla, soc in items:
        linea = f'\nClave: {cla}'        
        for dato in soc:
            linea += f'\n{dato}: {soc[dato]}'
        reporte += linea + '\n'
    return reporte

def reporte_honorificos(socios):
    """ Genera un reporte de los socios honoríficos, incluyendo solo
    nombre y teléfono.
    ...
    """
    reporte = '\nSOCIOS HONORÍFICOS\n'
    items = socios.items()
    for cla, soc in items:
        if soc['Honor']:
            for dato in soc:
                if dato == 'Nombre' or dato == 'Teléfono':
                    reporte += f'\n{dato}: {soc[dato]}'
    return reporte        
        
def pide_opcion():
    """ Despliega opciones de trabajo y lee la opción elegida.
    ...
    """
    opciones = ('A', 'B', 'L', 'H', 'T')
    bandera = True
    while bandera:
        print('\n¿Qué quieres hacer?')
        print('A: Alta de un nuevo socio.')
        print('B: Baja de un socio.')
        print('L: Lista de socios.')
        print('H: Lista de socios honoríficos.')
        print('T: Terminar.')
        elec = input('Ingresa la opción elegida: ').upper()
        bandera = elec not in opciones
    return elec

socios = {}
opcion = pide_opcion()
while opcion != 'T':   
    if opcion == 'A':
        clave = int(input('Ingrese la clave del nuevo socio: '))
        nombre = input('Ingrese el nombre: ')
        telefono = input('Ingrese el teléfono: ')
        correo = input('Ingrese el correo: ')
        honor = bool(input('¿Es socio honorífico? True/False: '))
        alta_socio(socios, clave, nombre, telefono, correo, honor)
    elif opcion == 'B':
         clave = int(input('Ingrese la clave del socio a dar de baja: '))
         baja_socio(socios, clave)
    elif opcion == 'L':
         print(reporte_socios(socios))
    else:
          print(reporte_honorificos(socios))
    opcion = pide_opcion()
         