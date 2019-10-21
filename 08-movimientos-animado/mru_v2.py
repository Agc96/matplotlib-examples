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

# Declarar la función para calcular la posición del objeto
def calcular_posicion(tiempo):
    return (tiempo * velocidad) + pos_inicial

# Configurar el gráfico principal
fig = plt.figure(figsize=(6, 6))
fig.suptitle('Movimiento rectilíneo uniforme')

# Configurar el subgráfico del MRU.
# - 211 indica que queremos dividir el gráfico en 2 filas y 1 columna, y que
#   queremos que este sea el 1er subgráfico. Vendría a ocupar el mismo espacio
#   que los subgráficos 1 y 2 de un gráfico de 2 filas x 2 columnas.
# - xlim y ylim determinan el rango visible de los ejes X e Y, respectivamente.
ax_movimiento = plt.subplot(211, xlim=(-100, 500), ylim=(-1, 1))
ln_movimiento, = plt.plot([], [], '-ro')
plt.xlabel('Posición (m)')
plt.grid(True)

# Configurar el subgráfico de posición.
# - 223 indica que queremos dividir el gráfico en 2 filas x 2 columnas, y que
#   queremos que este sea el 3er subgráfico (inferior izquierdo).
ax_posicion = plt.subplot(223, xlim=(0, 50), ylim=(0, 500))
ln_posicion, = plt.plot([], [], '-b')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.grid(True)

# Configurar el subgráfico de velocidad.
# - 224 indica que queremos dividir el gráfico en 2 filas x 2 columnas, y que
#   queremos que este sea el 4to subgráfico (inferior derecho).
ax_velocidad = plt.subplot(224, xlim=(0, 50), ylim=(0, 50))
ax_velocidad.yaxis.set_label_position("right")
ln_velocidad, = plt.plot([], [], '-b')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)

# Declarar la función de inicialización, que se ejecutará al principio de la
# animación, en la cual limpiamos los arreglos.
def init():
    frames.clear()
    posiciones.clear()
    velocidades.clear()
    return ln_movimiento, ln_posicion, ln_velocidad

# Declarar la función de animación, que se ejecutará repetidamente en cada
# cuadro (frame = 50ms), en la cual añadimos los siguientes valores del MRU.
def animate(frame):
    # Mover el objeto
    posicion = calcular_posicion(frame)
    ln_movimiento.set_data(posicion, 0)
    # Añadir valores de los arreglos
    frames.append(frame)
    posiciones.append(posicion)
    velocidades.append(velocidad)
    # Actualizar los gráficos
    ln_posicion.set_data(frames, posiciones)
    ln_velocidad.set_data(frames, velocidades)
    return ln_movimiento, ln_posicion, ln_velocidad

# Iniciar la animación
anim = FuncAnimation(fig, animate, frames=np.linspace(0, 50, 101), interval=50,
                     blit=True, init_func=init)
