# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 4_2
Métodos para trabajar con arreglos.
"""
import array

impares = array.array('b')
pares = array.array('b', [4, 12, -34, 48, -18]) 
letras = array.array('u', 'hola') 

# Agrega al final del arreglo.
letras.append('!')  
# letras.append(45.23)  # TypeError: ...

# Cantidad de elementos almacenados en el arreglo.
print('\nTotal de elementos en "letras":', len(letras))
print('Total de elementos en "impares":', len(impares))

# Para conocer el código del tipo del arreglo.
print('El código del tipo:', letras.typecode)
# Para conocer el tamaño de un elemento del arreglo.
print('El tamaño de un elemento:', letras.itemsize)

# Cuenta el número de veces que el parámetro está en el arreglo.  
print('\nTotal de "h" en "letras":', letras.count('h'))    

# Agrega varios elementos a un arreglo. 
# A partir de una cadena.
letras.extend('saludos')
print('\n"letras" extendido: ', end = '')
for c in letras:
    print(c, ' ', end = '')
# A partir de una tupla y se extiende un arreglo vacío.
impares.extend((13, 41, 87, 55, 37, 49)) 
print('\n"impares" extendido: ', end = '') 
for n in impares:
    print(n, ' ', end = '')
  
# Regresa la posición del valor 48. 
posicion = pares.index(48)
print('\n\nEl 48 está en la posición:', posicion)
# indice = pares.index(101)  # ValueError:...

# Inserta el 7 en la posición 4: queda como 5to. elemento. 
impares.insert(4, 7)
# Inserta el 17 al final.
impares.insert(40, 17)
# Posición negativa: se considera de derecha a izquierda.
impares.insert(-4, 77)
print('\n"impares" luego de insertar: 7, 17 y 77')
for n in impares:
    print(n, ' ', end = '')
    
# Quita y regresa el elemento de la posición dada.
print('\n\nElemento quitado de "letras":', letras.pop(0))  # Primero.
print('Elemento quitado de "impares":', impares.pop(-1))  # Último.
print('Elemento quitado de "impares":', impares.pop())  # Último.

# Quita la primera ocurrencia de 'a'.  
letras.remove('a') 

# Invierte el orden del arreglo.
letras.reverse()
print('\nLuego de quitar una "a" y de invertir el orden de "letras"')
for c in letras:
    print(c, ' ', end = '')

# Quita el primer elemento.
del impares[0]  
print('\n\nLuego de quitar el primer elemento de "impares":')
for n in impares:
    print(n, ' ', end = '') 

# Borra el arreglo completo.
del impares



