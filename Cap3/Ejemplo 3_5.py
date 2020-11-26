# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 3_5
Copia de diccionarios.
"""

import copy

num_meses = {'ene': 1, 'feb': 2, 'mar': 3, 'abr': 4, 'may': 5, 'jun': 6}

# Usando métodos del módulo copy.
copia_meses1 = copy.copy(num_meses)
copia_meses2 = copy.deepcopy(num_meses)

# Usando la función copy().
copia_meses = num_meses.copy()

