# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 2.2
"""

def realiza_encuesta(ingles, chino, frances, otros):
    """ Despliega la encuesta y pide la respuesta.
    Agrega la respuesta al grupo que corresponda.
    Parámetros:
        ingles: de tipo set. Se guardarán los documentos de los que dominan inglés.
        chino: de tipo set. Lo mismo para el chino.
        frances: de tipo set. Lo mismos para el francés.
        otros: de tipo list. Se guardarán los documentos de las
        personas que dominen otros idiomas. 
    """
    idioma = contesta()
    while idioma != 'T':
        docum = input('Ingrese su documento de identidad: ')
        if idioma == 'I':
            ingles.add(docum)
        elif idioma == 'C':
            chino.add(docum)
        elif idioma == 'F':
            frances.add(docum)
        else:
            otros.append(docum)
        idioma = contesta()
        
def contesta():
    """ Solicita el idioma que domina el encuestado.
    Regresa:
        Una letra que indica el idioma que domina el encuestado.
    """
    print('\n¿Qué idioma extranjero domina?'.upper())
    print('I-Inglés, C-Chino, F-Francés, O-Otros')
    print(f'\n-Ingrese uno a la vez. Si domina más de uno, diferente' 
          f' de los 3 nombrados, vuelva a contestar la encuesta.')
    print(f'-Para terminar la encuesta ingrese T')
    resp = input('Opción elegida: ')
    return resp.upper()

# Inicialmente están los conjuntos y la lista vacíos.
ingles = set()
chino = set()
frances = set()
otros = list()
# Se capturan las respuestas de los encuestados.     
realiza_encuesta(ingles, chino, frances, otros)
conj_otros = set(otros)  # Favorece algunas operaciones.
# Inciso 1. 
print('\nTotal de personas que dominan inglés:', len(ingles))
print('Total de personas que dominan chino:', len(chino))
print('Total de personas que dominan francés:', len(frances))
# Inciso 2. 
union_de3 = ingles.union(frances, chino)
respuesta = union_de3.intersection(conj_otros) 
print(f'\nTotal de encuestados que dominan, por lo menos, uno de los 3'
      f' y uno de los otros:', len(respuesta))
# Inciso 3.
dos_otros = set()
for doc in otros:
    if otros.count(doc) >= 2:
        dos_otros.add(doc)
print('\nTotal de encuestados que dominan, por lo menos, dos de los '
      f'otros idiomas:', len(dos_otros))
# Inciso 4.
chi_ing = chino.difference(ingles)
if len(chi_ing) == 0:
    print(f'\nTodos los encuestados que dominan chino también '
          f'dominan inglés.')
else:
    print(f'\nNo todos los encuestados que dominan chino también '
          f'dominan inglés.')
# Inciso 5.
solo_otros = conj_otros.difference(union_de3)
total_solo_otros = len(solo_otros)
if total_solo_otros > 0:
    print(f'\nHay {total_solo_otros} encuestados que dominan idiomas '
      f'diferentes a: inglés, chino y francés.')        



