# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 2.7
"""

# Alternativa de solución 1 (presentada en el libro y en el vídeo).
def es_pangrama(alfabeto, texto):
    """ Determina si el texto es un pangrama.
    Parámetros:
        alfabeto: de tipo set. Almacena todos los caracteres de un alfabeto.
        texto: de tipo str. Es el texto que debe analizarse.
    Regresa:
        True si el texto es un pangrama y False en caso contrario.
    """
    long_tex = len(texto)
    resp = False
    if long_tex >= len(alfabeto):
        indice = 0
        while indice < long_tex and len(alfabeto) > 0:
            if texto[indice] in alfabeto:
                alfabeto.remove(texto[indice])
            indice += 1
        resp = len(alfabeto) == 0
    return resp 

# Alternativa de solución 2.
def es_pangrama_2(alfabeto, texto):
    for caracter in alfabeto:
        if caracter not in texto:
            return False
    return True

# Alternativa de solución 3: utiliza solo conjuntos. 
def es_pangrama_3(alfabeto, texto):
    conj_texto = set(texto)
    return conj_texto.issuperset(alfabeto)  
    
arch_alf = input('\nIngrese nombre del archivo con el alfabeto: ')
arch_tex = input('Ingrese nombre del archivo con el texto: ')
try:
    conj_alf = set()
    with open(arch_alf, 'r') as alf:
        for letra in alf:
            conj_alf.add(letra.strip().lower())  
    with open(arch_tex, 'r') as tex:
        texto = tex.read().lower()   
except FileNotFoundError:
    print('\nNo se pudo abrir uno o ninguno de los archivos.')
else:
    if es_pangrama(conj_alf, texto):
        print('\nEs un pangrama.'.upper())
    else:
        print('\nNo es un pangrama.'.upper())
 
