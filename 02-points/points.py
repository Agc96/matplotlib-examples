# -*- coding: utf-8 -*-
"""Mostrar la trayectoria de un objeto usando matplotlib."""

import pandas as pd
import matplotlib.pyplot as plt

# Cargar archivo
random = pd.read_csv('random.csv')
sine = pd.read_csv('sine.csv')
# Mostrar puntos
# 'o' indica que se debe pintar los puntos
# '-' indica que se debe hacer una línea sólida entre los puntos
# 'b' indica que la línea debe ser de color azul
# 'r' indica que la línea debe ser de color rojo
plt.plot(random['x'], random['y'], 'bo-', label='Mov. aleatorio')
plt.plot(sine['x'], sine['y'], 'ro-', label='Mov. sinusoidal')
plt.legend()
# Mostrar lienzo
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición registrada (m)')
plt.show()
