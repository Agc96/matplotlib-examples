# -*- coding: utf-8 -*-

"""
Ejemplo básico de animación de puntos con Matplotlib.
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
