# -*- coding: utf-8 -*-
"""
Mostrar la trayectoria, velocidad y aceleración de una caída libre.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.constants import g as GRAVEDAD

# Limpiar la terminal
from IPython import get_ipython
get_ipython().magic('clear')

# Solicitar la posición inicial
print('Ingrese la posición inicial del objeto:')
while True:
    try:
        alt_inicial = float(input())
        break
    except:
        print('La posición ingresada no es válida, inténtelo nuevamente.')

# Solicitar la velocidad inicial
print('Ingrese la velocidad del objeto:')
while True:
    try:
        vel_inicial = float(input())
        break
    except:
        print('La velocidad ingresada no es válida, inténtelo nuevamente.')

# Declarar la función para la posición
def calcular_altura(tiempo):
    return -0.5*GRAVEDAD*(tiempo**2) + vel_inicial*tiempo + alt_inicial

# Declarar la función para la velocidad
def calcular_velocidad(tiempo):
    return -GRAVEDAD*tiempo + vel_inicial

# Inicializar los arreglos
frames = []
alturas = []
velocidades = []
aceleraciones = []

# Configurar el gráfico principal
fig = plt.figure(figsize=(8, 6))
fig.suptitle('Caída libre')

# Configurar el subgráfico de la caída libre.
# - 235 indica que queremos dividir el gráfico en 1 fila x 2 columnas, y que
#   queremos que este sea el 1er subgráfico. Vendría a ocupar el mismo espacio
#   que los subgráficos 1, 3 y 5 de un gráfico de 3 filas x 2 columnas.
# - xlim y ylim determinan el rango visible de los ejes X e Y, respectivamente.
ax_movimiento = plt.subplot(121, xlim=(-1, 1), ylim=(-15000, 5000))
ln_movimiento, = plt.plot([], [], '-ro')
plt.xlabel('Altura (m)')
plt.grid(True)

# Configurar el subgráfico de altura.
# - 322 indica que queremos dividir el gráfico en 3 filas x 2 columnas, y que
#   queremos que este sea el 2do subgráfico (superior derecho).
ax_altura = plt.subplot(322, xlim=(0, 50), ylim=(-15000, 5000))
ax_altura.yaxis.set_label_position("right")
ln_altura, = plt.plot([], [], '-b')
plt.ylabel('Altura (m)')
plt.grid(True)

# Configurar el subgráfico de velocidad.
# - 324 indica que queremos dividir el gráfico en 2 filas x 3 columnas, y que
#   queremos que este sea el 4to subgráfico (parte media derecha).
ax_velocidad = plt.subplot(324, xlim=(0, 50), ylim=(-500, 50))
ax_velocidad.yaxis.set_label_position("right")
ln_velocidad, = plt.plot([], [], '-b')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)

# Configurar el subgráfico de gravedad.
# - 326 indica que queremos dividir el gráfico en 2 filas x 3 columnas, y que
#   queremos que este sea el 6to subgráfico (inferior derecho).
ax_gravedad = plt.subplot(326, xlim=(0,50), ylim=(-10, -8))
ax_gravedad.yaxis.set_label_position("right")
ln_gravedad, = plt.plot([], [], '-b')
plt.xlabel('Tiempo (s)')
plt.ylabel('Gravedad (m/s²)')
plt.grid(True)

# Declarar la función de inicialización, que se ejecutará al principio de la
# animación, en la cual limpiamos los arreglos.
def init():
    frames.clear()
    alturas.clear()
    velocidades.clear()
    aceleraciones.clear()
    return ln_movimiento, ln_altura, ln_velocidad, ln_gravedad

# Declarar la función de animación, que se ejecutará repetidamente en cada
# cuadro (frame = 50ms), en la cual añadimos los siguientes valores del MRU.
def animate(frame):
    # Mover el objeto en la posición especificada
    altura = calcular_altura(frame)
    ln_movimiento.set_data(0, altura)
    # Añadir valores de los arreglos
    frames.append(frame)
    alturas.append(altura)
    velocidades.append(calcular_velocidad(frame))
    aceleraciones.append(-GRAVEDAD)
    # Actualizar los gráficos
    ln_altura.set_data(frames, alturas)
    ln_velocidad.set_data(frames, velocidades)
    ln_gravedad.set_data(frames, aceleraciones)
    return ln_movimiento, ln_altura, ln_velocidad, ln_gravedad

# Iniciar la animación
anim = FuncAnimation(fig, animate, frames=np.linspace(0, 50, 101), interval=50,
                     blit=True, init_func=init)
