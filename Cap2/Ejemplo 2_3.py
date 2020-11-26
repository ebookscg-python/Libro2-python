# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 2_3
Operaciones entre conjuntos.
"""

vocales = {'a', 'e', 'i', 'o', 'u'}
letras1 = {'g', 'o', 'm', 'b', 'e', 'a', 'u', 'i'}
letras2 = {'u', 'm', 'b', 'o', 'e', 'i', 'g', 'a'}
consonantes = {'g', 'r', 'd', 's'}

# Unión de conjuntos.
union1 = vocales.union(consonantes)
union2 = vocales | consonantes
union3 = vocales | letras1 | letras2 | consonantes
print('\nUnión - CP1:', union1)
print('Unión - CP2:', union2)
print('Unión - CP3:', union3)

# Intersección de conjuntos.
inter1 = letras1.intersection(consonantes)
inter2 = letras1 & vocales
inter3 = vocales.intersection(consonantes)
print('\nIntersección - CP1:', inter1)
print('Intersección - CP2:', inter2)
print('Intersección - CP3:', inter3)

# Diferencia de conjuntos.
dif1 = letras2.difference(vocales)
dif2 = letras1 - letras2  # Debe quedar vacío.
print('\nDiferencia - CP1:', dif1)
print('Diferencia - CP2:', dif2)

# Diferencia simétrica de conjuntos.
difsim1 = consonantes.symmetric_difference(letras2)
difsim2 = vocales ^ letras1
print('\nDiferencia simétrica - CP1:', difsim1)
print('Diferencia simétrica - CP2:', difsim2)

# Igualdad de conjuntos.
if letras1 == letras2:
    print('\nSon conjuntos iguales.')  # Imprime.
    
# Conjuntos distintos.
if vocales != letras1:
    print('\nSon conjuntos distintos.')   # Imprime.

# Relación de subconjunto.
if vocales <= letras1:
    print('\nSubconjunto - CP1: es un subconjunto.')
else:
    print('\nSubconjunto - CP1: no es un subconjunto.')    
if vocales.issubset(consonantes):
    print('Subconjunto - CP2: es un subconjunto.')
else:
    print('Subconjunto - CP2: no es un subconjunto.')
    
# Relación de super conjunto.
if letras2 >= vocales:
    print('\nSuper conjunto - CP1: es un super conjunto.')
else:
    print('\nSuper conjunto - CP1: no es un super conjunto.')
    
if letras2.issuperset(consonantes):
    print('Super conjunto - CP2: es un super conjunto.')
else:
    print('Super conjunto - CP2: no es un super conjunto.')
    
# Conjuntos disjuntos.    
if vocales.isdisjoint(consonantes):
    print('\nSon disjuntos.')  # Imprime.
    
# Copia de conjuntos.
copia_voc = vocales.copy()
print(f'\nConjunto de vocales: {vocales} y su copia: {copia_voc}')