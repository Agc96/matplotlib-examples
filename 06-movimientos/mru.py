# -*- coding: utf-8 -*-
"""
Mostrar la trayectoria y velocidad de un movimiento rectilíneo uniforme.
"""

import sys

import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython

# Limpiar la terminal
get_ipython().magic('clear')

# Solicitar la posición inicial
try:
    pos_inicial = float(input('Ingrese la posición inicial: '))
except ValueError:
    print('La posición inicial ingresada no es válida.')
    sys.exit()

# Solicitar la velocidad
try:
    velocidad = float(input('Ingrese la velocidad: '))
except ValueError:
    print('La velocidad ingresada no es válida.')
    sys.exit()

# Declarar la función para la posición
def generar_posicion(tiempo):
    return (tiempo * velocidad) + pos_inicial

# Generar los arreglos:
# - funcion(arreglo) genera un nuevo arreglo con la función aplicada a cada
#   elemento de dicho arreglo.
# - np.full(arreglo.shape, elemento) genera un nuevo arreglo con el mismo
#   elemento repetido tantas veces como dicte el tamaño del arreglo original.
tiempos = np.linspace(0, 20, 21)
posiciones = generar_posicion(tiempos)
velocidades = np.full(tiempos.shape, velocidad)

# Configurar el tamaño del gráfico
plt.figure(figsize=(8, 8))

# Mostrar el subgráfico de posiciones
plt.subplot(211) # 2 filas, 1 columna, 1er subgráfico
plt.plot(tiempos, posiciones, '-o')
plt.title('Movimiento rectilíneo uniforme')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.grid(True)

# Mostrar el subgráfico de velocidades
plt.subplot(212) # 2 filas, 1 columna, 2do subgráfico
plt.plot(tiempos, velocidades, '-o')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)

# Mostrar el gráfico completo
plt.show()
