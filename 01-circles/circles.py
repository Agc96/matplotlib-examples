# -*- coding: utf-8 -*-
"""Crear y mostrar unos círculos con matplotlib."""

import matplotlib.pyplot as plt

# Configurar el tamaño del lienzo
plt.figure(num=None, figsize=(8, 6))
# Crear círculos
circle1 = plt.Circle((8, 5), radius=5, color='blue', fill=False, label='Círculo azul')
circle2 = plt.Circle((11, 9), radius=5, color='red', fill=False, label='Círculo rojo')
circle3 = plt.Circle((5, 9), radius=5, color='green', fill=False, label='Círculo verde')
# Añadir los círculos al lienzo
ax = plt.gca()
ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)
ax.legend()
# Configurar el lienzo
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
plt.grid()
plt.axis('scaled')
plt.xlabel('Intersección de 3 círculos')
plt.ylabel('Intersección de 3 círculos')
# Guardar y mostrar el lienzo
plt.savefig('circles.png')
plt.savefig('circles.pdf')
plt.show()
