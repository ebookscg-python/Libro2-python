# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 3_2
Algunas operaciones con diccionarios.
"""
nom_meses = {1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril', 5: 'mayo', 6: 'junio'}
puntaje = {}.fromkeys(['futbol', 'basquetbol', 'tenis', 'natación'], 5)
frutas = {'manzana': 34, 'pera': 45}

# Agrega un nuevo par clave: valor
frutas['cereza'] = 90 
print('\nLuego de agregar cereza: 90 -->', frutas)
# Modifica el valor correspondiente a la clave.
frutas['manzana'] = 37  # Como la clave ya está, asigna este valor.
print('Luego de modificar el valor de manzana -->', frutas)
# Agrega los ítems de un diccionario a otro.
nuevo = {}
nuevo.update(puntaje)
print('\nUsando update-1:', nuevo)
nuevo.update(frutas)
print('\nUsando update-2:', nuevo)
frutas['guayaba'] = 32
nuevo.update(frutas)
print('\nUsando update-3:', nuevo)

# Acceso y modificación a un elemento por medio de su clave.
print('\nEl valor de pera es:', frutas['pera']) 
frutas['cereza'] += 10  # Le suma 10 al valor actual.
# frutas['mango'] += 5  # Da KeyError: 'mango'
# Consulta el valor, dada una clave.
print('El valor de cereza:', frutas.get('cereza'))  # Regresa el valor.
print('El valor de banana:', frutas.get('banana'))  # Regresa None.

# Elimina el par correspondiente a la clave dada.
del frutas['pera']  
print('\nLuego de quitar pera: 45 -->', frutas)
# del d['higo']  # Da KeyError: 'higo'
elem = nom_meses.pop(1)  # Quita el elemento y regresa solo su valor.
print(f'Luego de quitar {elem} -->', nom_meses)
# Quita arbitrariamente un elemento y lo regresa.
elem = nom_meses.popitem()  
print(f'Luego de quitar {elem} -->', nom_meses)
nom_meses.clear()  # Vacía el diccionario.
print(f'Luego de quitar todos los elementos -->', nom_meses)

# Uso del operador de membresía: in. Es solo para claves.
if 'cereza' in frutas:  
    print('\nSí está cereza en el diccionario.')  # Imprime.
else:
    print('No está cereza en el diccionario.')
if 'uva' not in frutas:
    print('No está uva en el diccionario.')  # Imprime.
else:
    print('Sí está uva en el diccionario.')  
if 100 in frutas:  # Membresía de un valor.
    print('Sí está el 100 en el diccionario.')  
else:
    print('No está el 100 en el diccionario.')  # Imprime.