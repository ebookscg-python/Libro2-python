
# -*- coding: utf-8 -*-
"""
@author: guardati
Módulo: arreglo
Agrupa funciones auxiliares al uso de arreglos en la solución de problemas.
"""
import array
import math

# =============================================================================
# Solución del problema 4.5
# =============================================================================
def suma_arreglo(arreglo):
    """ Suma los elementos de un arreglo numérico.    
    Parámetro:
        arreglo: de tipo array de int o float.
    Regresa:
        suma: de tipo int o float (depende del tipo de los elementos del arreglo).
    """
    suma = 0
    for indice in range(0, len(arreglo)):
        suma += arreglo[indice]
    return suma

def minimo(arreglo):
    """ Encuentra la posición del elemento más pequeño.    
    Parámetro:
        arreglo: de tipo array. Almacena datos de cualquier tipo que sea 
        comparable.
    Regresa:
        El índice del elemento más pequeño o -1 si el arreglo está vacío.
    """
    minimo = -1
    n = len(arreglo)
    if n > 0:
        minimo = 0
        for indice in range(1, n):
            if arreglo[indice] < arreglo[minimo]:
                minimo = indice
    return minimo

def maximo(arreglo):
    """ Encuentra la posición del elemento más grande.    
    Parámetro:
        arreglo: de tipo array. Almacena datos de cualquier tipo que sea 
        comparable.
    Regresa:
        El índice del elemento más grande o -1 si el arreglo está vacío.
    """
    maximo = -1
    n = len(arreglo)
    if n > 0:
        maximo = 0
        for indice in range(1, n):
            if arreglo[indice] > arreglo[maximo]:
                maximo = indice
    return maximo

def a_cadena(arreglo):
    """ Genera una cadena con el contenido del arreglo.    
    Parámetro:
        arreglo: de tipo array.
    Regresa:
        Una cadena con el contenido del arreglo.
    """
    cadena = ''
    for dato in arreglo:
        cadena += str(dato) + ' '  
    return cadena

def mayores_o_iguales_que(arreglo, referencia):
    """ Determina si todos los elementos del arreglo son
    mayores o iguales al dato dado como referencia.
    Parámetros:
        arreglo: de tipo array. Almacena datos de cualquier tipo que sea 
        comparable.
        referencia: es del mismo tipo que los elementos del arreglo.
    Regresa:
        True/False si los elementos del arreglo cumplen o no con la condición.
    """
    respuesta = True
    n = len(arreglo)
    indice = 0
    while indice < n and respuesta:
        respuesta = arreglo[indice] >= referencia
        indice += 1
    return respuesta

def cuenta_menores_que(arreglo, dato):
    """ Cuenta los elementos del arreglo que son menores al dato recibido.
    Parámetros:
        arreglo: de tipo array. Almacena datos de cualquier tipo que sea 
        comparable.
        dato: es de un tipo comparable con los elementos del arreglo.
    Regresa:
        La cantidad de elementos del arreglo que son menores que el dato.
    """
    contador = 0
    for elemento in arreglo:
        if elemento < dato:
            contador += 1
    return contador
   
# =============================================================================
# Búsqueda secuencial en un arreglo desordenado.
# =============================================================================
def busca(arreglo, dato):
    """ Busca al dato en el arreglo, regresando su posición.
    Parámetros:
        arreglo: de tipo array.
        dato: del mismo tipo que los elementos del arreglo.
    Regresa:
        La posición del dato o -1 si no lo encontró.

    """
    n = len(arreglo)
    indice = 0
    while indice < n and arreglo[indice] != dato:
        indice += 1
    if indice == n:
        indice = -1
    return indice

# =============================================================================
# Búsqueda binaria en arreglo ordenado.
# =============================================================================
def busca_ordenado(arreglo, dato):
    """ Busca al dato en el arreglo, regresando su posición.
    Parámetros:
        arreglo: de tipo array. Debe estar ordenado de manera creciente.
        dato: del mismo tipo que los elementos del arreglo.
    Regresa:
        Una tupla en la cual el primer elemento (bool) indica si 
        el dato fue encontrado o no. Y el segundo (int) indica la 
        posición en la que está o en la que debería estar.
    """
    izquierdo = 0
    derecho = len(arreglo) - 1
    centro = derecho // 2
    while izquierdo <= derecho and arreglo[centro] != dato:
        if arreglo[centro] < dato:
            izquierdo = centro + 1
        else:
            derecho = centro - 1
        centro = (izquierdo + derecho) // 2
    if izquierdo <= derecho:
        resultado = True, centro
    else:
        resultado = False, izquierdo
    return resultado

# =============================================================================
# Búsqueda secuencial en un arreglo ordenado.
# =============================================================================
def buscasec_ordenado(arreglo, dato):
    """ Busca al dato en el arreglo, regresando su posición.
    Parámetros:
        arreglo: de tipo array. Ordenado de menor a mayor.
        dato: del mismo tipo que los elementos del arreglo.
    Regresa:
        Una tupla en la que el primer elemento (bool) indica si el dato fue 
        encontrado o no. El segundo (int) indica la posición en la que está 
        o en la que debería estar.
    """
    n = len(arreglo)
    indice = 0
    while indice < n and arreglo[indice] < dato:
        indice += 1
    if indice == n or arreglo[indice] > dato:
        resultado = False, indice
    else:
        resultado = True, indice
    return resultado

# =============================================================================
# Método de inserción en arreglo ordenado, sin repetidos.
# =============================================================================
def inserta_ordenado(arre, dato):
    """ Agrega el dato en el arreglo ordenado crecientemente, 
    sin alterar el orden y sin repetir datos.
    Parámetros:
        arreglo: de tipo array.
        dato: del mismo tipo que los elementos del arreglo.
    """
    esta, posicion = busca_ordenado(arre, dato)
    if not esta:
        arre.insert(posicion, dato)
    
# =============================================================================
# Eliminación de un dato en un arreglo desordenado. 
# =============================================================================
def elimina_desordenado(arre, dato):
    """ Elimina la primera ocurrencia del dato encontrada en
    el arreglo cuyos elementos están desordenados.
    Parámetros:
        arreglo: de tipo array.
        dato: del mismo tipo que los elementos del arreglo.
    Lanza:
        ValueError: si el dato no está en el arreglo.
    """
    posicion = busca(arre, dato)
    if posicion >= 0:
        temporal = arre.pop()
        if posicion < len(arre):
            arre[posicion] = temporal
    else:
        raise ValueError(f'{dato} no se encuentra en el arreglo.')
        
# =============================================================================
# Eliminación de un dato en un arreglo ordenado.
# =============================================================================
def elimina_ordenado(arre, dato):
    """ Elimina el dato en el arreglo ordenado crecientemente, 
    sin alterar el orden.
    Parámetros:
        arreglo: de tipo array.
        dato: del mismo tipo que los elementos del arreglo.
    Lanza:
        ValueError: si el dato no está en el arreglo.
    """
    esta, posicion = busca_ordenado(arre, dato)
    if esta:
        for indice in range(posicion, len(arre) - 1):
            arre[indice] = arre[indice + 1]
        arre.pop()
    else:
        raise ValueError(f'{dato} no se encuentra en el arreglo.')

# =============================================================================
# Método de ordenación: selección directa. Ordena de menor a mayor.
# =============================================================================
def ordena_crec(arreglo):
    """ Ordena de menor a mayor los elementos del arreglo.
    Parámetros:
        arreglo: de tipo array.
    Lanza:
        ValueError: si el arreglo está vacío.
    """
    n = len(arreglo)
    if n > 0:
        for i in range (0, n - 1):
            menor = arreglo[i]
            posicion = i
            for j in range(i + 1, n):
                if arreglo[j] < menor:
                    menor = arreglo[j]
                    posicion = j
            arreglo[posicion] = arreglo[i]
            arreglo[i] = menor
    else:
        raise ValueError('Arreglo vacío'.upper())

# =============================================================================
# Método de ordenación: selección directa. Ordena de mayor a menor.
# =============================================================================   
def ordena_decrec(arreglo):
    """ Ordena de mayor a menor los elementos del arreglo.
    Parámetros:
        arreglo: arreglo a ordenar.
    Lanza:
        ValueError: si el arreglo está vacío.
    """
    n = len(arreglo)
    if n > 0:
        for i in range (0, n - 1):
            mayor = arreglo[i]
            posicion = i
            for j in range(i + 1, n):
                if arreglo[j] > mayor:
                    mayor = arreglo[j]
                    posicion = j
            arreglo[posicion] = arreglo[i]
            arreglo[i] = mayor
    else:
        raise ValueError('Arreglo vacío'.upper())
        
# =============================================================================
# Método auxiliar para trabajar con arreglos y archivos binarios.
# =============================================================================
def guarda_en_archivo(tipo, nombre, mensaje1, mensaje2):
    """ Lee de la terminal una cierta cantidad de datos, los guarda en un 
    arreglo y luego almacena el arreglo en un archivo binario.
    Parámetros:
        tipo: de tipo str. Es el código de tipo de dato para el arreglo 
        que se creará.
        nombre: de tipo str. Es el nombre con el que se creará el archivo.
        mensaje1: de tipo str. Es el mensaje que se desplegará
        cuando se pida el total de datos a leer.
        mensaje2: de tipo str. Es el mensaje que se desplegará
        cuando se pida cada dato.
    Regresa:
        El total de elementos que tiene el arreglo guardado en el 
        archivo binario.
    """
    arre = array.array(tipo)
    file_s = open(nombre, 'wb')
    n = int(input(f'\n{mensaje1} '))
    for _ in range (0, n):
        dato = int(input(f'{mensaje2} '))
        arre.append(dato)
    arre.tofile(file_s)
    file_s.close()
    return n

# =============================================================================
# Función que calcula y regresa la moda de un grupo de números.
# =============================================================================
def calcula_moda(arreglo):
    """ Calcula y regresa la moda de un grupo de números 
    almacenados en el arreglo.
    Parámetro:
        arreglo: de tipo array. Almacena los datos.
    Regresa:
        La moda de un grupo de números. 
    Lanza:
        ValueError: si no hay moda.
    """
    dic = {}
    for n in arreglo:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1
    mayor = -1
    for clave in dic:
        if dic[clave] > mayor:
            mayor = dic[clave]
            moda = clave
    if mayor > 1:
        return moda
    raise ValueError('No hay moda.')

# =============================================================================
# Método auxiliar para leer n datos de la terminal y guardarlos
# en un arreglo.
# =============================================================================
def lectura(arre, n, tipo, mensaje):
    """ Lee de la terminal n datos del tipo solicitado y los guarda
    en un arreglo.
    Parámetros:
        arre: de tipo array. Donde se guardarán los n datos leídos.
        n: de tipo int. Indica el total de datos a leer.
        tipo: algún tipo de dato compatible con el tipo de los datos del arreglo.
        mensaje: de tipo str. Es el mensaje que se despliega al pedir el dato.
    """
    for _ in range(0, n):
        num = tipo(input(mensaje))
        arre.append(num)

# =============================================================================
# Solución del problema 4.7
# =============================================================================
def busca_todos(arreglo, dato):
    """ Busca al dato en todo el arreglo, regresando la posición
    de todas las ocurrencias encontradas.
    Parámetros:
        arreglo: de tipo array.
        dato: del mismo tipo que los elementos del arreglo.
    Regresa:
        Una lista que almacena todas las posiciones en las que se encontró al 
        dato. Si el dato no está, la lista queda vacía.
    """
    indices = [i for i in range (0, len(arreglo)) if arreglo[i] == dato]    
    return indices

# =============================================================================
# Solución del problema 4.10
# =============================================================================
def elimina(arreglo, posicion):
    """ Elimina y regresa el dato que se encuentra en la posición.
    Parámetros:
        arreglo: de tipo array (desordenado).
        posicion: de tipo int. Posición del dato que se quitará.
    Regresa:
        El dato quitado.
    Lanza:
        IndexError: si la posición está fuera del arreglo.
    """
    n = len(arreglo)
    if posicion >= 0 and posicion < n:
        dato = arreglo[posicion]
        temporal = arreglo.pop()
        if posicion < n - 1:
            arreglo[posicion] = temporal
        return dato
    raise IndexError('Posición fuera del arreglo.')

# =============================================================================
# Solución del problema 4.12
# =============================================================================
def cambia_ordenado(arre, dato1, dato2):
    """ Cambia en el arreglo ordenado crecientemente el dato1 por el dato2.
    Parámetros:
        arre: de tipo array (ordenado).
        dato1: del mismo tipo que los elementos del arreglo.
        dato2: del mismo tipo que los elementos del arreglo.
    Lanza:
        ValueError: si el dato1 no está en el arreglo o si el dato2 
        altera el orden. 
    """
    esta, pos = busca_ordenado(arre, dato1)
    if esta:
        if len(arre) == 1:  # Hay solo un dato.
            arre[pos] = dato2
        elif pos == 0:  # Es el primero.
            if dato2 <= arre[pos + 1]:
                arre[pos] = dato2
            else:
                raise ValueError(f'{dato2} altera el orden.')
        elif pos == len(arre) - 1:  # Es el último.
            if dato2 >= arre[pos - 1]:
                arre[pos] = dato2
            else:
                raise ValueError(f'{dato2} altera el orden.')
        else:  # Está en una posición intermedia.
            if dato2 >= arre[pos - 1] and dato2 <= arre[pos + 1]:
                arre[pos] = dato2
            else:
                raise ValueError(f'{dato2} altera el orden.')
    else:
        raise ValueError(f'{dato1} no se encuentra en el arreglo.')   
        
# =============================================================================
# Solución del problema 4.13
# =============================================================================
def elimina_todos_endesordenado(arre, dato):
    """ Elimina del arreglo todas las ocurrencias del dato.    
    Parámetros:
        arre: de tipo array (desordenado).
        dato: del mismo tipo que los elementos del arreglo.
    Regresa:
        El total de veces que se eliminó el dato.
    """    
    n = len(arre)
    cont = 0
    if n > 0:
        n -= 1
        indice = 0
        while indice < n:
            if arre[indice] == dato:
                arre[indice] = arre.pop()
                n -= 1
                cont += 1
            else:
                indice += 1
        # El último elemento no se evalúa en el ciclo.
        if arre[indice] == dato:
            cont += 1
            arre.pop()
    return cont

# =============================================================================
# Solución del problema 4.14
# =============================================================================
def elimina_todos_enordenado(arre, dato):
    """ Elimina del arreglo todas las ocurrencias del dato.    
    Parámetros:
        arre: de tipo array (ordenado).
        dato: del mismo tipo que los elementos del arreglo.
    Regresa:
        El total de veces que se eliminó el dato.
    """    
    n = len(arre)
    cont = 0
    if n > 0:
        esta, pos = buscasec_ordenado(arre, dato)
        if esta:
            indice = pos + 1
            cont = 1
            while indice < n and arre[indice] == dato:
                cont += 1
                indice += 1
            for indice in range(pos, len(arre) - cont):
                arre[indice] = arre[indice + cont]
            for _ in range(0, cont):
                arre.pop()
    return cont

# =============================================================================
# Solución del problema 4.16
# =============================================================================
def desviacion_estandar(arre):
    """ Calcula la desviación estándar de un grupo de n datos.
    Parámetro:
        arre: de tipo array. Almacena números.
    Regresa:
        La desviación estándar de un grupo de números.
    Lanza:
        ValueError: si el arreglo está vacío.
    """
    n = len(arre)
    if n > 0:
        media = suma_arreglo(arre) / n
        sumat = 0
        for i in range (0, n):
            sumat += (arre[i] - media) ** 2
        desv = math.sqrt(sumat / n)
        return desv
    raise ValueError('No hay datos.')

# =============================================================================
# Algunas pruebas de los métodos definidos en este módulo.
# =============================================================================

# letras = array.array('u', 'tigres')
# print('\nCP1: "g" está en el arreglo. -->', busca(letras, 'g'))
# print('CP2: "z" no está en el arreglo. -->', busca(letras, 'z'))
# =============================================================================
# numeros = array.array('i', [10, 21, 23, 40, 45, 61, 72, 83])
# print('\nCP1: el dato está. -->', busca_ordenado(numeros, 21))
# print('CP2: el dato no está. -->', busca_ordenado(numeros, 93))
# =============================================================================
# numeros = array.array('i', [10, 21, 23, 40, 45, 61, 72, 83])
# inserta_ordenado(numeros, 35)
# print('\nCP1: 35 no está, se inserta. -->', a_cadena(numeros))
# inserta_ordenado(numeros, 72)
# print('CP2: 72 ya está, no se inserta. -->', a_cadena(numeros))
# =============================================================================
# letras = array.array('u', 'tigres')
# numeros = array.array('i', [88])
# try:    
#     elimina_desordenado(letras, 'g')
#     print('\nCP1: "g" está, se elimina. -->', a_cadena(letras))
#     elimina_desordenado(numeros, 88)
#     print('CP2: 88 está (es el único dato). -->', a_cadena(numeros))
#     elimina_desordenado(letras, 'z')
#     print('CP3: intento de eliminar la "z". -->', a_cadena(letras))
# except Exception as error:
#     print('CP3: un dato que no está. -->', error)
# =============================================================================
# try:
#     elimina_ordenado(numeros, 61)
#     print('\nCP1: 61 está, se elimina. -->', a_cadena(numeros))
#     elimina_ordenado(numeros, 11)
#     print('CP2: intento de eliminar el 11. -->', a_cadena(numeros))
# except Exception as error:
#     print('CP2: un dato que no está. -->', error)
# =============================================================================
# letras = array.array('u', 'tigres')
# numeros = array.array('i', [10, 21, 23, 40, 45, 61, 72, 83])
# vacio = array.array('b')
# ordena_crec(letras)
# print('\nCP1: se da un arreglo desordenado. -->', a_cadena(letras))
# try:
#     ordena_crec(vacio)
#     print('CP2: se da un arreglo vacío. -->', a_cadena(vacio))
# except Exception as error:
#     print('CP2: se da un arreglo vacío. -->', error)
# ordena_decrec(numeros) 
# resultado = a_cadena(numeros)
# print('CP3: se da un arreglo ordenado de menor a mayor. -->', resultado)



