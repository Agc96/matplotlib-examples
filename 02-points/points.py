# -*- coding: utf-8 -*-
"""Mostrar la trayectoria de un objeto usando matplotlib."""

import pandas as pd
import matplotlib.pyplot as plt

# Cargar trayectorias
random = pd.read_csv('random.csv')
sine = pd.read_csv('sine.csv')
# Mostrar trayectorias
# 'o' indica que se deben colocar puntos en forma redonda
# '-' indica que se debe hacer una línea sólida entre los puntos
# 'b' indica que la línea debe ser de color azul (blue)
# 'r' indica que la línea debe ser de color rojo (red)
plt.plot(random['x'], random['y'], 'bo-', label='Mov. aleatorio')
plt.plot(sine['x'], sine['y'], 'ro-', label='Mov. sinusoidal')
plt.legend()
# Mostrar lienzo
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición registrada (m)')
plt.show()
