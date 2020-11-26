# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 3_10
Diccionarios y conjuntos.
"""

# Se crean 4 diccionarios.
menu1 = {'ensalada': 35, 'sopa': 28, 'pollo': 40, 'fruta': 15}    
menu2 = {'ensalada': 35, 'pollo': 40, 'gelatina': 20}   
menu3 = {'ensalada': 35, 'sopa': 28, 'ternera': 50, 'pastel': 30}   
menu4 = {'ensalada': 35, 'sopa': 28, 'cerdo': 45, 'pastel': 30}  

# Vistas de claves (tratadas como conjuntos) de 3 diccionarios.
claves1 = menu1.keys() 
claves2 = menu2.keys() 
claves3 = menu3.keys() 
claves4 = set(menu4)  # Se crea un conjunto a partir de un diccionario.

# Todos los platillos que se sirven: unión de conjuntos.
platillos = claves1 | claves2 | claves3 | claves4
print('\nLos platillos que se sirven son:', platillos)
# Platillo que se repite en todos los menús: intersección de conjuntos.
lo_comun = claves1 & claves2 & claves3 & claves4 
print('\nEn todos los menús se sirve:', lo_comun) 

# Vistas de ítems (tratadas como conjuntos) de 2 diccionarios.
pla_pre1 = menu1.items()
pla_pre2 = menu2.items()

# Platillo y precio que está en el menú1 pero no en el menú2:
# diferencia de conjuntos.
no_estan = pla_pre1 - pla_pre2
print('\nLos platillos que se sirven en el menú1 y no en el menú2:', no_estan)

