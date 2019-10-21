# -*- coding: utf-8 -*-

"""
Crear una columna que se mueve de forma oscilatoria.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.transforms import Affine2D

# Configurar la figura y el eje
fig = plt.figure(figsize=(8, 4))
ax = plt.axes(xlim=(-120, 120), ylim=(-130, 130))

# Configurar el rectángulo y su borde
pendulo = plt.Rectangle((0, 0), 1, 12, fill=False, color='blue')
borde = plt.Rectangle((0, 0), 1, 12, fill=False, color='red', linestyle='--')

# Añadir rectángulos al eje, el pendulo debe resaltar antes que el borde por
# lo que se coloca al último
ax.add_patch(borde)
ax.add_patch(pendulo)

# Función de animación, que debe ser llamada secuencialmente. Limpiamos el eje
# para crear y mostrar un rectangulo nuevo con la posición y ángulo cambiados
def update(frame):
    # Calcular nueva posición
    """
    amplitud = 3
    velangular = np.pi / 50
    posicion = amplitud * np.sin(velangular * frame)
    pendulo.set_x(posicion)
    """
    # Calcular nuevo ángulo
    """
    amplitud = 20
    velangular = np.pi / 5
    angulo = amplitud * np.sin(velangular * frame)
    pendulo.angle = angulo
    """
    # TODO: Quitar esto
    # coords = ax.transData.transform([0, 0])
    transform = Affine2D().rotate_around(0, 0, 1)
    # pendulo.set_transform(transform)
    print(transform)
    # Devolver una tupla con ambos rectángulos
    return borde, pendulo

# Crear la animación. blit=True indica que solo debemos redibujar las partes
# que han sido cambiadas.
anim = FuncAnimation(fig, update, frames=200, interval=20, blit=True)
