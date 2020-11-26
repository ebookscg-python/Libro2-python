# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 2_5
Ejemplos de conjuntos creados con el tipo frozenset.
"""

# A partir de una cadena.
vocales = frozenset('aeiou')
# A partir de un conjunto.
colores_primarios = frozenset({'rojo', 'verde', 'azul'})
# A partir de una tupla.
primos_hasta10 = frozenset((1, 2, 3, 5, 7))
print('\nUsando una cadena:', vocales)
print('Usando un conjunto:', colores_primarios)
print('Usando una tupla:', primos_hasta10)
print('\nTipo:', type(vocales))

# Operación de pertenencia.
if 'verde' in colores_primarios:
    print('\nEl verde es un color primario.')
# Operación de cardinalidad.
print('\nCardinalidad de vocales:', len(vocales))

# Intento de agregar un elemento, provoca:
# AttributeError: 'frozenset' object has no attribute 'add'
# vocales.add('ü')

# Operaciones con frozensets.
union1 = vocales | colores_primarios
print('\nUnión de 2 frozensets:', union1)
inter1 = vocales & colores_primarios
print('Intersección de 2 frozensets:', inter1)

numeros = {1, 25, 53, 18, 32}  # Tipo set.
# Unión combinando set y frozenset.
union2 = numeros | primos_hasta10  # Resultado: tipo set.
union3 = primos_hasta10 | numeros  # Resultado: tipo frozenset.
print('\nTipo al unir set y frozenset:', type(union2))
print('Tipo al unir frozenset y set:',type(union3))
# Comparación entre set y frozenset.
if numeros.isdisjoint(primos_hasta10):
    print('\nSon conjuntos disjuntos.')
else:
    print('\nNo son conjuntos disjuntos.')    
c1 = set('amor')
c2 = frozenset('roma')
if c1 == c2:
    print('\nIguales: por contenido.')
else:
    print('\nDistintos: por contenido.')

# Conjuntos de conjuntos.
# Se crea un frozenset con 2 elementos tipo frozenset.
vocales_acentuadas = frozenset({'á', 'é', 'í', 'ó', 'ú'})
mas_vocales = frozenset((vocales, vocales_acentuadas))
print('\nConjunto de conjuntos-1:'.upper(), 'tipo', type(mas_vocales)) 
print(mas_vocales)
if vocales in mas_vocales:
    print('\nLas vocales sí están en el conjunto.')

# Se crea un set con 2 elementos tipo frozenset.
mezcla = {vocales, colores_primarios}
print('\nConjunto de conjuntos-2:'.upper(), 'tipo', type(mezcla)) 
print(mezcla)
mezcla.add('hola')  # Permite el cambio.
print('\nLuego de agregar "hola" queda:', mezcla)
print('\nCon una cardinalidad =', len(mezcla))
