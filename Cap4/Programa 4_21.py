# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.24
Se obtiene e imprime la siguiente información del registro de temperaturas:
    - Temperatura máxima registrada en uno de los días
    - Promedio de todas las temperaturas registradas
    - Temperatura máxima registrada en un cierto horario 
    - Días en los cuales todas las temperaturas registradas fueron menores a 10°C
    - Cantidad de días que tuvieron una temperatura mayor a 13°C a las 18 horas
"""

import matrices

dias = {1, 2, 3, 4, 5, 6, 7}
horarios = [0, 6, 12, 18]  # Lista porque interesa posición
horas_registros = {0: '0 h', 1: '6 h', 2: '12 h', 3: '18 h'}
try:
    nombre = input('\nIngrese nombre del archivo de temperaturas: ')
    temp = matrices.lee_de_archivo(nombre, float)
    filas = len(temp)
    columnas = len(temp[0])    
    dia = int(input('Ingrese el día (1 a 7) para buscar la máxima temperatura: '))
    if dia in dias:
        dia -= 1  # Adapta para que corresponda al índice de las filas.
        horario = matrices.max_fila(temp, dia)
        max_temp = temp[dia][horario]
        print(f'\nLa máxima temperatura es = {max_temp}°C', end = '')
        print(f' y fue registrada a las {horas_registros[horario]}.')
    else:
        print('\nEl número de día es incorrecto.')
    suma_temperaturas = 0    
    for f in range(filas):
        suma_temperaturas += matrices.suma_fila(temp, f)
    promedio = suma_temperaturas / (filas * columnas)
    print(f'\nPromedio de temperaturas registradas en los 7 días es = {promedio}°C')
    hora = int(input('Ingrese la hora (0, 6, 12 o 18): '))
    if hora in horarios:
        hora = horarios.index(hora)
        dia = matrices.max_columna(temp, hora)
        max_temp = temp[dia][hora]
        print(f'\nLa máxima temperatura es = {max_temp}°C', end = '')
        print(f' y fue registrada el día {dia + 1}.')
    else:
        print('\nEl horario de registro es incorrecto.')
    dias_men = matrices.todos_menores_que(temp, 10)
    long = len(dias_men) - 1
    if long >= 0:
        cad = ''
        for i in range(long):
            cad += str(dias_men[i] + 1) + ' - ' 
        cad += str(dias_men[long] + 1)
        print(f'\nDías en los cuales todas las temperaturas < 10°C son: {cad}')
    cont = matrices.cuenta_por_columna_mayores_que(temp, 3, 13)
    print(f'\nCantidad de días con temperatura > 13°C a las 18 h = {cont}')     
except Exception:
    print('\nError en la lectura del archivo')