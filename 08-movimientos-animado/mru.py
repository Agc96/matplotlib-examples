# -*- coding: utf-8 -*-
"""
Mostrar la trayectoria y velocidad de un movimiento rectilíneo uniforme.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Limpiar la terminal
from IPython import get_ipython
get_ipython().magic('clear')

# Solicitar la posición inicial
print('Ingrese la posición inicial del objeto:')
while True:
    try:
        pos_inicial = float(input())
        break
    except:
        print('La posición ingresada no es válida, inténtelo nuevamente.')

# Solicitar la velocidad
print('Ingrese la velocidad del objeto:')
while True:
    try:
        velocidad = float(input())
        break
    except:
        print('La velocidad ingresada no es válida, inténtelo nuevamente.')

# Inicializar los arreglos
frames = []
posiciones = []
velocidades = []

# Declarar la función para la posición
def posicion(tiempo):
    return (tiempo * velocidad) + pos_inicial

# Configurar el gráfico principal
fig = plt.figure(figsize=(8, 8))

# Configurar el subgráfico de posiciones. 211 indica que el gráfico tendrá 2
# filas y 1 columna, y este es el primer subgráfico
ax_posicion = plt.subplot(211)
ln_posicion, = plt.plot(frames, posiciones, '-ro')
plt.title('Movimiento rectilíneo uniforme')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.grid(True)

# Configurar el subgráfico de velocidades. 211 indica que el gráfico tendrá 2
# filas y 1 columna, y este es el segundo subgráfico
ax_velocidad = plt.subplot(212)
ln_velocidad, = plt.plot(frames, velocidades)
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)

def animate(frame):
    # Añadir valores de los arreglos
    frames.append(frame)
    posiciones.append(posicion(frame))
    velocidades.append(velocidad)
    # Actualizar los arreglos de datos
    ln_posicion.set_data(frames, posiciones)
    ln_velocidad.set_data(frames, velocidades)
    # Devolver los nuevos datos
    print(posiciones)
    return ln_posicion, ln_velocidad

# Iniciar la animación
anim = FuncAnimation(fig, animate, frames=np.linspace(0, 20, 21), blit=True,
                     repeat=False)
