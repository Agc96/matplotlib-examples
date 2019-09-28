# -*- coding: utf-8 -*-
"""
Simula el movimiento de un edificio (rectángulo) con un movimiento sinusoidal.
Para poder ver las animaciones, debe ejecutar `%matplotlib qt` en la consola
antes de ejecutar este código.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True)
plt.show()
"""

rectangle = plt.Rectangle((10, 0), 20, 100)
figure, ax = plt.subplots()
ax.add_patch(rectangle)

# Mostrar el lienzo
ax.set_xlim(-0, 100)
ax.set_ylim(0, 120)
plt.show()
