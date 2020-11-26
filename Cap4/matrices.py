# -*- coding: utf-8 -*-
"""
@author: guardati
Módulo: matrices
"""

def forma_matriz_1(filas, columnas):
    """ Construye y regresa un arreglo bidimensional inicializado en 0. 
    Parámetros:
        filas: de tipo int. Indica total de filas del arreglo.
        columnas: de tipo int. Indica total de columnas del arreglo.
    Regresa:
        Una lista de listas (matriz) que contienen ceros.
    """
    matriz = []
    for f in range(0, filas):
        fila = []
        for c in range(0, columnas):
            fila.append(0)
        matriz.append(fila)
    return matriz

def forma_matriz_2(filas, columnas):
    """ Construye y regresa un arreglo bidimensional inicializado en 0. 
    Parámetros:
        filas: de tipo int. Indica total de filas del arreglo.
        columnas: de tipo int. Indica total de columnas del arreglo.
    Regresa:
        Una lista de listas (matriz) que contienen ceros.
    """
    matriz = [[0 for c in range(columnas)] for f in range(filas)]
    return matriz

def forma_matriz_3(filas, columnas):
    """ Construye y regresa un arreglo bidimensional inicializado en 0. 
    Parámetros:
        filas: de tipo int. Indica total de filas del arreglo.
        columnas: de tipo int. Indica total de columnas del arreglo.
    Regresa:
        Una lista de listas (matriz) que contienen ceros.
    """
    matriz = [[0] * columnas for f in range(filas)]
    return matriz      

# =============================================================================
# Solución del problema 4.19
# =============================================================================
def matriz_vacia():
    """ Construye y regresa un arreglo bidimensional vacío. 
    Regresa:
        Una lista de listas vacías (matriz vacía).
    """
    matriz = [[]]
    return matriz

# =============================================================================
# Solución del problema 4.20
# =============================================================================
def suma_fila(matriz, fila):
    """ Suma y regresa los elementos de una fila del arreglo bidimensional.
    Parámetros:
        matriz: de tipo list. Es una lista de listas que guardan números.
        fila: de tipo int. Indica la fila de la cual se sumarán sus elementos.
    Regresa:
        La suma de los elementos de una fila del arreglo.
    Lanza:
        IndexError: si fila está fuera del rango del arreglo.
        TypeError: si matriz no es numérica.            
    """
    try:
        suma = 0
        columnas = len(matriz[0])
        for c in range(columnas):
            suma += matriz[fila][c]
        return suma
    except IndexError:
        raise IndexError(f'El número de fila está fuera del arreglo.')
    except TypeError:
        raise TypeError('El arreglo no es numérico.')

def suma_columna(matriz, columna):
    """ Suma y regresa los elementos de una columna del arreglo bidimensional.
    Parámetros:
        matriz: de tipo list. Es una lista de listas que guardan números.
        columna: de tipo int. Indica la columna de la cual se sumarán sus 
        elementos.
    Regresa:
        La suma de los elementos de una columna del arreglo.
    Lanza:
        IndexError: si columna está fuera del rango del arreglo.
        TypeError: si matriz no es numérica.  
    """
    try:
        suma = 0
        filas = len(matriz)
        for f in range(filas):
            suma += matriz[f][columna]
        return suma
    except IndexError:
        raise IndexError(f'El número de columna está fuera del arreglo.')
    except TypeError:
        raise TypeError('El arreglo no es numérico.')

# =============================================================================
# Solución del problema 4.21
# =============================================================================
def suma_diagonal_principal(matriz):
    """ Suma y regresa los elementos de la diagonal principal
    de un arreglo bidimensional cuadrado.
    Parámetros:
        matriz: de tipo list. Es una lista de listas que guardan números.
    Regresa:
        La suma de los elementos de la diagonal principal.
    """
    dimension = len(matriz)
    if dimension == len(matriz[0]):        
        suma = 0
        for indice in range(dimension):
            suma += matriz[indice][indice]
        return suma
    else:
        raise IndexError('Error: no es un arreglo cuadrado.')

def suma_diagonal_secundaria(matriz):
    """ Suma y regresa los elementos de la diagonal secundaria
    de un arreglo bidimensional cuadrado.
    Parámetros:
        matriz: de tipo list. Es una lista de listas que guardan números.
    Regresa:
        La suma de los elementos de la diagonal secundaria.
    """
    dimension = len(matriz)
    if dimension == len(matriz[0]):        
        suma = 0
        for indice in range(dimension):
            suma += matriz[indice][dimension - 1 - indice]
        return suma
    else:
        raise IndexError('Error: no es un arreglo cuadrado.')

# =============================================================================
# Solución del problema 4.22    
# =============================================================================
def max_fila(matriz, fila):
    """ Obtiene y regresa la posición del elemento más grande de una 
    fila del arreglo bidimensional.
    Parámetros:
        matriz: de tipo list. Es una lista de listas que guardan 
        valores comparables.
        fila: de tipo int. Indica la fila en la cual se debe buscar
        el elemento más grande.
    Regresa:
        La columna en la cual está el valor más grande de la fila recibida.
    Lanza:
        IndexError: si el arreglo no tiene datos almacenados o los
        valores de fila o columnas están fueran del rango del arreglo.
    """
    try:
        maximo = matriz[fila][0]        
        posicion = 0
        columnas = len(matriz[0])
        for c in range(1, columnas):
            if matriz[fila][c] > maximo:
                maximo = matriz[fila][c]
                posicion = c
        return posicion
    except:
        raise IndexError('El arreglo no tiene elementos.')
    
def max_columna(matriz, columna):
    """ Obtiene y regresa la posición del elemento más grande de 
    una columna del arreglo bidimensional.
    Parámetros:
        matriz: de tipo list. Es una lista de listas que guardan 
        valores comparables.
        columna: de tipo int. Indica la columna en la cual se debe buscar
        el elemento más grande.
    Regresa:
        La fila en la cual está el valor más grande de la columna recibida.
    Lanza:
        IndexError: si el arreglo no tiene datos almacenados o los
        valores de filas o columna están fueran del rango del arreglo.
    """
    try:
        maximo = matriz[0][columna]
        posicion = 0
        filas = len(matriz)
        for f in range(1, filas):
            if matriz[f][columna] > maximo:
                maximo = matriz[f][columna]
                posicion = f
        return posicion
    except:
        raise IndexError('El arreglo no tiene elementos.')    
        
# =============================================================================
# Solución del problema 4.23
# =============================================================================
def suma_matrices(matriz1, matriz2):
    """ Suma dos matrices y regresa el resultado de la suma.
    Parámetros:
        matriz1: de tipo list. Es una lista de listas que guardan números.
        matriz2: de tipo list. Es una lista de listas que guardan números.
    Regresa:
        Una lista de listas que almacena la suma de las matrices.
    Lanza:
        IndexError: si las matrices recibidas no tienen el mismo tamaño.
    """    
    filas = len(matriz1)
    columnas = len(matriz1[0])
    if filas == len(matriz2) and columnas == len(matriz2[0]):
        resultado = forma_matriz_2(filas, columnas)
        for f in range(filas):
            for c in range(columnas):
                resultado[f][c] = matriz1[f][c] + matriz2[f][c]
        return resultado
    else:
        raise IndexError('Las matrices no tienen el mismo tamaño.')

# =============================================================================
# Solución del problema 4.26
# =============================================================================
def es_simetrica(matriz):
    """ Determina si una matriz es simétrica.
    Parámetro:
        matriz: de tipo list. Lista de listas.
    Regresa:
        True si es simétrica, False en caso contrario.
    """
    dimension = len(matriz)
    if dimension == len(matriz[0]):  # Es cuadrada.
        f = 1
        simetrica = True
        while simetrica and f < dimension:
            c = 0
            while simetrica and c < f:  
                simetrica = matriz[f][c] == matriz[c][f]
                c += 1
            f += 1
    else:
        simetrica = False
    return simetrica

# =============================================================================
# Solución del problema 4.27        
# =============================================================================
def traspuesta(matriz):
    """ Obtiene la matriz traspuesta de la matriz recibida. 
    Parámetro: 
        matriz: de tipo list. Lista de listas.
    Regresa:
        La matriz traspuesta de la matriz recibida. Es de tipo list.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    trasp = forma_matriz_2(columnas, filas)
    for f in range(filas):
        for c in range(columnas):
            trasp[c][f] = matriz[f][c]
    return trasp
      
# =============================================================================
# Solución del problema 4.28
# =============================================================================
def multiplica_matrices(matriz1, matriz2):
    """ Multiplica dos matrices y regresa el resultado que es otra matriz.
    Parámetros:
        matriz1: de tipo list. Lista de listas.
        matriz2: de tipo list. Lista de listas.
    Regresa:
        La matriz resultado de la multiplicación de las matrices recibidas.
    """
    filas1 = len(matriz1)
    columnas1 = len(matriz1[0])
    filas2 = len(matriz2)
    columnas2 = len(matriz2[0])
    if columnas1 == filas2:
        resultado = forma_matriz_2(filas1, columnas2)
        for i in range(filas1):
            for j in range(columnas2):
                acum = 0
                for k in range(columnas1):
                    acum += matriz1[i][k] * matriz2[k][j]
                resultado[i][j] = acum
        return resultado
    else:
        raise ValueError('Las matrices no pueden multiplicarse.')

# =============================================================================
# Solución del problema 4.30
# =============================================================================
def es_triangular_superior(matriz):
    """ Determina si la matriz recibida es una matriz triangular superior.
    Parámetro:
        matriz: de tipo list. Lista de listas que guardan números.
    Regresa:
        True si la matriz cumple con la condición o False en caso contrario.
    Lanza:
        ValueError: si la matriz no es cuadrada.
    """        
    n = len(matriz)
    if n > 0 and n == len(matriz[0]):   # Es cuadrada.
        respuesta = True
        fila = 1
        while respuesta and fila < n:
            columna = 0
            while respuesta and columna < fila:
                respuesta = matriz[fila][columna] == 0
                columna += 1
            fila += 1
        return respuesta
    raise ValueError('La matriz no es cuadrada.')
    
def es_triangular_inferior(matriz):
    """ Determina si la matriz recibida es una matriz triangular inferior.
    Parámetro:
        matriz: de tipo list. Lista de listas que guardan números.
    Regresa:
        True si la matriz cumple con la condición o False en caso contrario.
    Lanza:
        ValueError: si la matriz no es cuadrada.
    """ 
    n = len(matriz)
    if n > 0 and n == len(matriz[0]):   # Es cuadrada.
        respuesta = True
        fila = 0
        una_antes = n - 1
        while respuesta and fila < una_antes:
            columna = fila + 1
            while respuesta and columna < n:
                respuesta = matriz[fila][columna] == 0
                columna += 1
            fila += 1
        return respuesta
    raise ValueError('La matriz no es cuadrada.')

# =============================================================================
# Funciones auxiliares usadas en algunos de los problemas resueltos.  
# =============================================================================
def a_cadena(matriz):
    """ Genera una cadena con el contenido del arreglo.    
    Parámetro:
        matriz: de tipo list (lista de listas). 
        Representa un arreglo bidimensional.
    Regresa:
        Una cadena con el contenido del arreglo o una cadena vacía si 
        el arreglo está vacío.
    """
    cadena = ''
    filas = len(matriz)
    if filas > 0:
        columnas = len(matriz[0])
        for f in range(0, filas):
            for c in range(0, columnas):
                cadena += str(matriz[f][c]) + ' ' 
            cadena += '\n'
    return cadena

def lee(matriz, tipo):
    """ Lee datos de la terminal y los almacena en un arreglo bidimensional, 
    por filas.
    Parámetros:
        matriz: de tipo list. Es una lista de listas. 
        tipo: de tipo str. Indica el tipo de datos que se leerá.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = tipo(input(f'Ingrese el elemento ({f}, {c}): '))

def lee_de_archivo(archivo, tipo):
    """ Lee números de un archivo de texto y los almacena en un 
    arreglo bidimensional, por filas. El primer dato del archivo es el
    número de filas y, el segundo, es el número de columnas.
    Todos los valores guardados en el archivo se encuentran en líneas
    distintas.
    Parámetros:
        archivo: de tipo str. Es el nombre del archivo.
        tipo: de tipo str. Indica el tipo de dato que se leerá del archivo.
    Regresa:
        Una lista de listas (matriz).
    Lanza:
        Exception: si se produjo algún error (al abrir el archivo, al 
        convertir a tipo, al acceder a una posición del arreglo, etc.)
    """
    try:
        with open(archivo, 'r') as arch:  
            filas = int(arch.readline())
            columnas = int(arch.readline())
            matriz = forma_matriz_3(filas, columnas)
            for f in range(filas):
                for c in range(columnas): 
                    matriz[f][c] = tipo(arch.readline().strip())
            return matriz
    except Exception:
        raise Exception('Error al leer el archivo.')

def todos_menores_que(matriz, referencia):
    """ Genera una lista con las filas cuyos valores son todos menores
    que el valor dado como referencia.
    Parámetros:
        matriz: de tipo list. Lista de listas de datos comparables.
        referencia: del mismo tipo que los datos de la matriz.
    Regresa:
        Una lista de enteros. 
    """
    resultado = []
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        bandera = True
        indice = 0
        while bandera and indice < columnas:
            bandera = matriz[f][indice] < referencia
            indice += 1
        if bandera:
            resultado.append(f)
    return resultado

def cuenta_por_columna_mayores_que(matriz, columna, referencia):
    """ Cuenta los elementos de una columna que son mayores que el valor
    dado como referencia.
    Parámetros:
        matriz: de tipo list. Lista de listas de datos comparables.
        columna: de tipo int. Indica la columna que se analizará.
        referencia: del mismo tipo que los datos de la matriz.
    Regresa:
        Cantidad de elementos mayores que el valor recibido.
    Lanza:
        IndexError: si el arreglo no tiene datos almacenados o los
        valores de filas o columna están fueran del rango del arreglo.
    """
    try:
        filas = len(matriz)
        contador = 0
        for f in range(filas):
            if matriz[f][columna] > referencia:
                contador += 1
        return contador
    except:
        raise IndexError(f'El número de columna está fuera del arreglo.')