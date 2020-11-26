# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 1_7
Ejemplo de listas anidadas.
"""

colores = ['azul', 'rojo', 'blanco']
pares = [2, 4, 6, 8]
dias = ['lun', 'mar', 'mie', 'jue', 'vie']
# Lista de listas.
lista1 = [colores, pares, dias]  
print('\nLista de listas:', lista1)
print('\nPrimer elemento de la lista:', lista1[0])

# Agrega a la segunda lista el número 10.
lista1[1].append(10)
print('\nLuego de agregar el 10 a la segunda lista:', lista1)
print('Lista "pares" también se modificó:', pares)
# Modifica el tercer elemento de la segunda lista.
lista1[1][2] = 24
print('\nLuego de reemplazar el 6 por 24:', lista1)
print('Lista "pares" también se modificó:', pares)
# Pasa a mayúsculas el quinto elemento de la tercera lista.
lista1[2][4] = lista1[2][4].upper()
print('\nLuego de pasar a mayúsculas a "vie":', lista1)
print('Lista "dias" también se modificó:', dias)

# Se define una lista con un nivel mayor de anidamiento.
lista2 = [lista1, [[20, 30, 40], [-20, -30, -40]]]
print('\nLista de listas de listas:', lista2)
# Eleva al cuadrado al quinto elemento del segundo 
# elemento (que es una lista) del primer elemento (también lista)
# de la lista2.
lista2[0][1][4] = lista2[0][1][4] ** 2
print('\nLuego de elevar al cuadrado:', lista2[0][1])
print('\nLista "pares" también se modificó:', pares)

# Acceso a los elementos por medio de índices cuyos valores
# están controlados por ciclos for.
print('\nElementos de lista2:\n')
for i in range(0, len(lista2)):
    for j in range(0, len(lista2[i])):
        for k in range(0, len(lista2[i][j])):
            print(lista2[i][j][k], end = ' ')
        print('')
    print('')
