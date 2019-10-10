# -*- coding: utf-8 -*-
"""
Mostrar la trayectoria, velocidad y aceleración de un movimiento rectilíneo
uniformemente variado.
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

# Solicitar la velocidad inicial
try:
    vel_inicial = float(input('Ingrese la velocidad inicial: '))
except ValueError:
    print('La velocidad inicial ingresada no es válida.')
    sys.exit()

# Solicitar la aceleración
try:
    aceleracion = float(input('Ingrese la aceleración: '))
except ValueError:
    print('La aceleración ingresada no es válida.')
    sys.exit()

# Declarar la función para la posición
def generar_posicion(tiempo):
    return tiempo * generar_velocidad(tiempo) + pos_inicial

# Declarar la función para la velocidad
def generar_velocidad(tiempo):
    return tiempo * aceleracion + vel_inicial

# Generar los arreglos:
# - funcion(arreglo) genera un nuevo arreglo con la función aplicada a cada
#   elemento de dicho arreglo.
# - np.full(arreglo.shape, elemento) genera un nuevo arreglo con el mismo
#   elemento repetido tantas veces como dicte el tamaño del arreglo original.
tiempos = np.linspace(0, 20, 21)
posiciones = generar_posicion(tiempos)
velocidades = generar_velocidad(tiempos)
aceleraciones = np.full(tiempos.shape, aceleracion)

# Configurar el tamaño del gráfico
plt.figure(figsize=(8, 12))

# Mostrar el subgráfico de posición
plt.subplot(311) # 3 filas, 1 columna, 1er subgráfico
plt.plot(tiempos, posiciones, '-o')
plt.title('Movimiento rectilíneo uniformemente variado')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.grid(True)

# Mostrar el subgráfico de velocidad
plt.subplot(312) # 3 filas, 1 columna, 2do subgráfico
plt.plot(tiempos, velocidades, '-o')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)

# Mostrar el subgráfico de aceleración
plt.subplot(313) # 3 filas, 1 columna, 3er subgráfico
plt.plot(tiempos, aceleraciones, '-o')
plt.xlabel('Tiempo (s)')
plt.ylabel('Aceleración (m/s²)')
plt.grid(True)

# Mostrar el gráfico completo
plt.show()
