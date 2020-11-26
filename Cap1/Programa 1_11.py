# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 1.11
"""

def genera_tabla_multiplicar(numero, limite):
    """ Genera una lista de listas que almacena la tabla de 
    multiplicar de número desde 1 hasta el límite.    
    Parámetro:
        numero: de tipo int o float que representa un multiplicando.
        limite: de tipo int > 0 que indica el máximo valor 
        por el cual se multiplicará el multiplicando.
    Regresa: 
        Una lista de listas, donde cada una de ellas almacena el resultado 
        de una multiplicación. 
    """     
    oper1 = [numero] 
    oper2 = [valor for valor in range(1, limite + 1)]
    resultado = [[n1, n2, n1 * n2] for n1 in oper1 for n2 in oper2]
    return resultado

def guarda_tabla_multiplicar(archivo, lista):
    """ Guarda en un archivo el contenido de la lista.    
    Parámetro:
        archivo: de tipo str. Se usa para nombrar al archivo.
        lista: de tipo list. Lista de listas de tres elementos.
    Lanza: 
        FileNotFoundError: si no se puede abrir el archivo.
    """ 
    try:        
        with open(archivo, 'w') as arch:
            titulo = f'Tabla de multiplicar del: {lista[0][0]} \n\n'.upper()
            arch.write(titulo)
            for terna in lista:
                linea = f'{terna[0]} x {terna[1]:2d} = {terna[2]:.2f}'
                arch.write(linea + '\n')
    except FileNotFoundError:
        raise FileNotFoundError('No se pudo abrir el archivo.'.upper())

# =============================================================================
# Algunas pruebas de las funciones genera_tabla_multiplicar() y 
# guarda_tabla_multiplicar()  
# =============================================================================       
# CP1: con un entero positivo y nombre de archivo adecuado.
t5 = genera_tabla_multiplicar(5, 10)
guarda_tabla_multiplicar('Tabla del 5', t5)
# CP2: con un real positivo y nombre de archivo adecuado.
t3_4 = genera_tabla_multiplicar(3.4, 10)
guarda_tabla_multiplicar('Tabla del 3_4', t3_4)
# CP3: con un entero negativo y nombre de archivo adecuado.
t_8 = genera_tabla_multiplicar(-8, 15)
guarda_tabla_multiplicar('Tabla del -8', t_8)
# CP4: con cero y nombre de archivo adecuado.
t0 = genera_tabla_multiplicar(0, 5)
guarda_tabla_multiplicar('Tabla del 0', t0)
# CP5: igual que el CP1 pero dando un nombre no válido para el archivo.
try:
    guarda_tabla_multiplicar('', t5)
except FileNotFoundError as error:
    print('\n', error)  # Imprime error.