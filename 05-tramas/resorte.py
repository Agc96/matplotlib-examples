# -*- coding: utf-8 -*-

"""
Determina el movimiento de un objeto unido a un resorte.
"""

import sys
import os
from IPython import get_ipython

# Limpiar la terminal
ipython = get_ipython()
ipython.magic('cls' if os.name == 'nt' else 'clear')

# Verificar si los datos existen con anterioridad
if 'amplitud' in globals():
    result = input('¿Desea utilizar las variables anteriores? (S/N): ')
    if result.upper() == 'S':
        request = False
    elif result.upper() == 'N':
        ipython.magic('reset -f')
        request = True
    else:
        print('El comando no es válido.')
        sys.exit()
else:
    request = True

import sys

# Solicitar los datos para el problema
if request:
    # Solicitar la masa del objeto
    try:
        masa = input('Ingrese la masa del objeto: ')
        masa = float(masa)
    except ValueError:
        print('La masa no es válida.')
        sys.exit()
    # Solicitar la constante elástica
    try:
        constante = input('Ingrese la constante elástica del resorte: ')
        constante = float(constante)
    except ValueError:
        print('La constante elástica no es válida.')
        sys.exit()
    # Solicitar la amplitud
    try:
        amplitud = input('Ingrese la amplitud: ')
        amplitud = float(amplitud)
    except ValueError:
        print('La amplitud no es válida.')
        sys.exit()

import numpy as np
import matplotlib.pyplot as plt

# Generar los rangos
rango, intervalo = np.linspace(0, 10, 1000, endpoint=False, retstep=True)
# print('Intervalo')
# print(intervalo)
# print('Rango')
# print(rango)

# Calcular la velocidad angular
velocidad = np.sqrt(constante/masa)
print('La velocidad angular es:', velocidad)

# Generar los datos de la función senoidal
datos = []
for num in rango:
    datos.append(amplitud * np.sin(velocidad * num))
# print('Datos')
# print(datos)

# Generar el lienzo
plt.plot(rango, datos, label='Senoidal')
plt.title('Ejemplo 2')
plt.legend()
plt.show()
