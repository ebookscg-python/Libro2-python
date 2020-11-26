# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 2.5
"""

def lectura(archivo):
    """ Lee desde un archivo los nombres de estudiantes que practican cierto
    deporte y los guarda en un conjunto.    
    Parámetro:
        archivo: de tipo str. Representa el nombre del archivo.
    Regresa:
        Un conjunto que almacena cadenas (nombres de los estudiantes).
    Lanza:
        FileNotFoundError: si no se puede abrir el archivo.
    """
    try:
        dep = set()
        with open(archivo, 'r') as lee:
            alum = lee.readline().strip()
            while alum != '':
                dep.add(alum)
                alum = lee.readline().strip()
        return dep
    except FileNotFoundError:
        raise FileNotFoundError('No se pudo abrir el archivo.'.upper())

def estudiantes_por_deporte(titulo, jugadores):
    """ Genera una cadena con el contenido de un conjunto.
    Parámetros:
        titulo: de tipo str. Es un mensaje que quiere 
        incluirse en el encabezado de la cadena que se forma.
        jugadores: de tipo set. Almacena nombres de jugadores.
    Regresa:
        Una cadena con un título y nombres de jugadores.
    """        
    res = ('\nLista de jugadores que practican ' + titulo + '\n').upper()
    for jug in jugadores:
        res += jug + '\n'
    return res

# Lectura de los nombres de los estudiantes, por deporte.
fut = lectura('futbol')
basq = lectura('basquetbol')
vol = lectura('voleibol')  # Usar archivo "volei" para probar el inciso 5.

# Inciso 1: nombres de estudiantes que practican voleibol.
print(estudiantes_por_deporte('Voleibol', vol)) 
# Inciso 2: cantidad de estudiantes que solo practican un deporte.
union_de3 = fut | basq | vol
inter_de3 = fut & basq & vol
solo_un_dep = union_de3 - inter_de3
print('Total de estudiantes que solo practican 1 deporte:', len(solo_un_dep))
# Inciso 3: nombre de los estudiantes que practican los 3 deportes.
print(estudiantes_por_deporte('los 3 deportes', inter_de3))
# Inciso 4: nombre de los que solo practican fútbol.
solo_fut = fut - basq - vol
print(estudiantes_por_deporte('solo fútbol', solo_fut))
# Inciso 5: nombre del deporte que practican estudiantes como 
# único deporte.
if len(fut & basq) == 0 and len(fut & vol) == 0:
    print('Todos los que practican fútbol no practican otro deporte.')
elif len(basq & fut) == 0 and len(basq & vol) == 0:
    print('Todos los que practican basquetbol no practican otro deporte.')
elif len(vol & fut) == 0 and len(vol & basq) == 0:
    print('Todos los que practican voleibol no practican otro deporte.')
else:
    print(f'En todos los deportes participa, al menos, un jugador que ' 
          f'practica un segundo deporte.')

