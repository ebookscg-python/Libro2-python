# -*- coding: utf-8 -*-
"""
@author: guardati
Pruebas de las soluciones de los problemas 4.13 y 4.14
"""
import array
import arreglo

# =============================================================================
# Algunas pruebas para el problema 4.13
# =============================================================================
des1 = array.array('i', [2, 7, 8, 4, 1, 9])
des2 = array.array('i', [2, 7, 2, 2, 1, 9, 6, 7, 2, 2])
des3 = array.array('i', [2, 2, 2, 2])
des4 = array.array('i', [5, 7, 0, 1, 4])
des5 = array.array('i')
# CP1: arreglo con una sola ocurrencia a eliminar.
n = arreglo.elimina_todos_endesordenado(des1, 2)
print(f'\nCP1: quita {n} vez/veces el 2 -->', arreglo.a_cadena(des1))
# CP2: arreglo con varias ocurrencias a eliminar.
n = arreglo.elimina_todos_endesordenado(des2, 2)
print(f'CP2: quita {n} vez/veces el 2 -->', arreglo.a_cadena(des2))
# CP3: arreglo con todos los elementos iguales al dato.
n = arreglo.elimina_todos_endesordenado(des3, 2)
print(f'CP3: quita {n} vez/veces el 2 -->', arreglo.a_cadena(des3))
# CP4: arreglo con todos los elementos distintos al dato.
n = arreglo.elimina_todos_endesordenado(des4, 2)
print(f'CP4: quita {n} vez/veces el 2 -->', arreglo.a_cadena(des4))
# CP5: arreglo vacío.
n = arreglo.elimina_todos_endesordenado(des5, 2)
print(f'CP5: quita {n} vez/veces el 2 -->', arreglo.a_cadena(des5))

# =============================================================================
# Algunas pruebas para el problema 4.14 
# =============================================================================
ord1 = array.array('i', [2, 6, 7, 9, 15, 22])
ord2 = array.array('i', [-3, 1, 2, 2, 2, 9, 16, 17, 20, 32])
ord3 = array.array('i', [-3, 1, 9, 16, 17, 20, 26, 26, 26, 26])
ord4 = array.array('i', [2, 2, 2, 2])
ord5 = array.array('i', [15, 27, 30, 31, 42])
ord6 = array.array('i')
# CP1: arreglo con una sola ocurrencia a eliminar (inicio).
n = arreglo.elimina_todos_enordenado(ord1, 2)
print(f'\nCP1: quita {n} vez/veces el 2 -->', arreglo.a_cadena(ord1))
# CP2: arreglo con varias ocurrencia a eliminar (en el medio).
n = arreglo.elimina_todos_enordenado(ord2, 2)
print(f'CP2: quita {n} vez/veces el 2 -->', arreglo.a_cadena(ord2))
# CP3: arreglo con varias ocurrencia a eliminar (al final).
n = arreglo.elimina_todos_enordenado(ord3, 26)
print(f'CP3: quita {n} vez/veces el 26 -->', arreglo.a_cadena(ord3))
# CP4: arreglo con todos los elementos iguales al dato.
n = arreglo.elimina_todos_enordenado(ord4, 2)
print(f'CP4: quita {n} vez/veces el 2 -->', arreglo.a_cadena(ord4))
# CP5: arreglo con todos los elementos distintos al dato.
n = arreglo.elimina_todos_enordenado(ord5, 2)
print(f'CP5: quita {n} vez/veces el 2 -->', arreglo.a_cadena(ord5))
# CP6: arreglo vacío.
n = arreglo.elimina_todos_enordenado(ord6, 2)
print(f'CP6: quita {n} vez/veces el 2 -->', arreglo.a_cadena(ord6))