# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.6
Procesa información de unidades vendidas en una agencia de autos,
obteniendo: total de unidades, promedio, meses con ventas inferiores
al promedio, mes con más ventas, mes con menos ventas y venta mínima
mensual.
"""

import array
import arreglo

def lee_ventas(ventas):
    """ Lectura de las ventas por mes. """ 
    for mes in range(0, 12):
        ventas.append(int(input(f'Autos vendidos en "{meses[mes]}": ')))

meses = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'set', 'oct',
         'nov', 'dic']
ventas = array.array('B')
lee_ventas(ventas)
refer = int(input('Ingrese cantidad de referencia: '))
total = arreglo.suma_arreglo(ventas)
promedio = total / 12
print('\nCantidad de autos vendidos el año anterior:', total)
print(f'Promedio mensual de unidades vendidas: {promedio:.2f}')
contmes = arreglo.cuenta_menores_que(ventas, promedio)
print('\nCantidad de meses con ventas inferiores al promedio:', contmes)
menos = arreglo.minimo(ventas)
print(f'\nMes en el que se vendieron menos autos: "{meses[menos]}",'
      f' con una venta total de {ventas[menos]} unidades.')
mas = arreglo.maximo(ventas)
print(f'Mes en el que se vendieron más autos: "{meses[mas]}",'
      f' con una venta total de {ventas[mas]} unidades.')
if arreglo.mayores_o_iguales_que(ventas, refer):
    print(f'\nSí se vendieron, al menos, {refer} unidades todos los meses.')
else:
    print(f'\nNo se vendieron, al menos, {refer} unidades todos los meses.')





