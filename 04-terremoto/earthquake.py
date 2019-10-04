# -*- coding: utf-8 -*-

"""
Simula el movimiento de un edificio (rectángulo) con un movimiento sinusoidal.
"""

import os

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def clear():
    """
    Para poder ver las animaciones, debemos ejecutar `%matplotlib qt`.
    """
    clear_command = 'cls' if os.name == 'nt' else 'clear'
    try:
        from IPython import get_ipython
        get_ipython().magic('matplotlib qt')
        get_ipython().magic(clear_command)
    except ImportError:
        os.system(clear_command)

def basic_animation():
    """
    Una animación básica de puntos que 
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

def earthquake():
    rectangle = plt.Rectangle((1, 0), 1, 5)
    figure, ax = plt.subplots()
    ax.add_patch(rectangle)

    def init():
        print(f"{'Frame':10} {'Position':10}")
        return rectangle,

    def update(frame):
        new_y = 0.05*(np.sin(frame - np.pi/2) + 1)
        print(f"{frame:10.4f} {new_y:10.4f}")
        rectangle.set_y(new_y)
        return rectangle,
    
    # Generar la animación
    ani = FuncAnimation(figure, update, frames=np.linspace(0, 200, 500),
                        init_func=init, blit=True)
    # Mostrar el lienzo
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 6)
    plt.show()

def main():
    clear()
    earthquake()

if __name__ == '__main__':
    main()
