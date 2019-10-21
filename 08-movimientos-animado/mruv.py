# -*- coding: utf-8 -*-
"""
Mostrar la trayectoria, velocidad y aceleración de un movimiento rectilíneo
uniformemente variado.
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

# Solicitar la velocidad inicial
print('Ingrese la velocidad del objeto:')
while True:
    try:
        vel_inicial = float(input())
        break
    except:
        print('La velocidad ingresada no es válida, inténtelo nuevamente.')

# Solicitar la aceleración
print('Ingrese la aceleración del objeto:')
while True:
    try:
        aceleracion = float(input())
        break
    except:
        print('La aceleración ingresada no es válida, inténtelo nuevamente.')

# Declarar la función para la posición
def calcular_posicion(tiempo):
    return 0.5*aceleracion*(tiempo**2) + vel_inicial*tiempo + pos_inicial

# Declarar la función para la velocidad
def calcular_velocidad(tiempo):
    return aceleracion*tiempo + vel_inicial

# Inicializar los arreglos
frames = []
posiciones = []
velocidades = []
aceleraciones = []

# Configurar el gráfico principal
fig = plt.figure(figsize=(12, 6))
fig.suptitle('Movimiento rectilíneo uniformemente variado')

# Configurar el subgráfico del MRUV.
# - 235 indica que queremos dividir el gráfico en 2 filas x 1 columna, y que
#   queremos que este sea el 1er subgráfico. Vendría a ocupar el mismo espacio
#   que los subgráficos 1, 2 y 3 de un gráfico de 2 filas x 3 columnas.
# - xlim y ylim determinan el rango visible de los ejes X e Y, respectivamente.
ax_movimiento = plt.subplot(211, xlim=(-4000, 4000), ylim=(-1, 1))
ln_movimiento, = plt.plot([], [], '-ro')
plt.xlabel('Posición (m)')
plt.grid(True)

# Configurar el subgráfico de posición.
# - 234 indica que queremos dividir el gráfico en 2 filas x 3 columnas, y que
#   queremos que este sea el 4to subgráfico (inferior izquierdo).
ax_posicion = plt.subplot(234, xlim=(0, 50), ylim=(-4000, 4000))
ln_posicion, = plt.plot([], [], '-b')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.grid(True)

# Configurar el subgráfico de velocidad.
# - 235 indica que queremos dividir el gráfico en 2 filas x 3 columnas, y que
#   queremos que este sea el 5to subgráfico (inferior medio).
ax_velocidad = plt.subplot(235, xlim=(0, 50), ylim=(-200, 200))
ln_velocidad, = plt.plot([], [], '-b')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)

# Configurar el subgráfico de aceleración.
# - 236 indica que queremos dividir el gráfico en 2 filas x 3 columnas, y que
#   queremos que este sea el 6to subgráfico (inferior derecho).
ax_aceleracion = plt.subplot(236, xlim=(0, 50), ylim=(-10, 10))
ln_aceleracion, = plt.plot([], [], '-b')
plt.xlabel('Tiempo (s)')
plt.ylabel('Aceleración (m/s²)')
plt.grid(True)

# Declarar la función de inicialización, que se ejecutará al principio de la
# animación, en la cual limpiamos los arreglos.
def init():
    frames.clear()
    posiciones.clear()
    velocidades.clear()
    aceleraciones.clear()
    return ln_movimiento, ln_posicion, ln_velocidad, ln_aceleracion

# Declarar la función de animación, que se ejecutará repetidamente en cada
# cuadro (frame = 50ms), en la cual añadimos los siguientes valores del MRU.
def animate(frame):
    # Mover el objeto en la posición especificada
    posicion = calcular_posicion(frame)
    ln_movimiento.set_data(posicion, 0)
    # Añadir valores de los arreglos
    frames.append(frame)
    posiciones.append(posicion)
    velocidades.append(calcular_velocidad(frame))
    aceleraciones.append(aceleracion)
    # Actualizar los gráficos
    ln_posicion.set_data(frames, posiciones)
    ln_velocidad.set_data(frames, velocidades)
    ln_aceleracion.set_data(frames, aceleraciones)
    return ln_movimiento, ln_posicion, ln_velocidad, ln_aceleracion

# Iniciar la animación
anim = FuncAnimation(fig, animate, frames=np.linspace(0, 50, 101), interval=50,
                     blit=True, init_func=init)
