# -*- coding: utf-8 -*-

"""
Simula el movimiento de un edificio (rectángulo) con un movimiento sinusoidal.
"""

import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython
from matplotlib.animation import FuncAnimation

# Para poder ver las animaciones, debemos cambiar el backend de Matplotlib
# a Qt5 o Qt4, dependiendo de cuál de los 2 tenga nuestro sistema operativo
try:
    get_ipython().magic('matplotlib qt5')
except ImportError:
    get_ipython().magic('matplotlib qt')

rectangle = plt.Rectangle((1, 0), 1, 5)
fig, ax = plt.subplots()
ax.add_patch(rectangle)

def init():
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 6)
    return rectangle,

def update(frame):
    position = 0.05*(np.sin(frame - np.pi/2) + 1)
    print("{0:10.4f} {1:10.4f}".format(frame, position))
    rectangle.set_y(position)
    return rectangle,

# Generar la animación
print("Frame      Position")
ani = FuncAnimation(fig, update, frames=np.linspace(0, 200, 501),
                    init_func=init, blit=True)
