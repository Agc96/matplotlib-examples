# -*- coding: utf-8 -*-

"""
Crear un rectángulo que se mueve de forma oscilatoria.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.transforms import Affine2D

# Configurar la figura y el eje
fig = plt.figure(figsize=(8, 4))
ax = plt.axes(xlim=(-12, 12), ylim=(0, 13))

# Configurar el rectángulo y su borde
rect = plt.Rectangle((0, 0), 1, 12, fill=False, color='blue')
borde = plt.Rectangle((0, 0), 1, 12, fill=False, color='red', linestyle='--')

# Añadir rectángulos al eje, el rectángulo principal debe resaltar antes que
# el borde, por lo que se coloca al último
ax.add_patch(borde)
ax.add_patch(rect)

# Función de animación, que debe ser llamada secuencialmente. Limpiamos el eje
# para crear y mostrar un rectangulo nuevo con la posición y ángulo cambiados
def update(frame):
    # Calcular nueva posición
    amplitud = 3
    periodo = 200
    posicion = amplitud * np.cos(2 * np.pi * frame / periodo)
    rect.set_x(posicion)
    # Calcular nuevo ángulo
    amplitud = 0.35
    periodo = 20
    angulo = amplitud * np.cos(2 * np.pi * frame / periodo)
    # Calcular transformada para rotar según el ángulo y la parte inferior
    # izquierda o derecha del rectángulo, dependiendo del caso
    trans_original = ax.transData
    punto_rotacion = (posicion, 0) if angulo >= 0 else (posicion + 1, 0)
    coords = trans_original.transform(punto_rotacion)
    trans_rotar = Affine2D().rotate_around(coords[0], coords[1], angulo)
    rect.set_transform(trans_original + trans_rotar)
    # Devolver una tupla con ambos rectángulos
    return borde, rect

# Crear la animación. blit=True indica que solo debemos redibujar las partes
# que han sido cambiadas.
anim = FuncAnimation(fig, update, frames=200, interval=20, blit=True)
