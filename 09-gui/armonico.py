# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 18:42:03 2019

@author: Agutierrez
"""

import numpy as np
import matplotlib.pyplot as plt

amplitud = 5
tiempo = 20
periodo = 1

def calcular_amplitud(frame):
    if frame <= (tiempo / 2):
        return 2 * amplitud * frame / tiempo
    else:
        return 2 * amplitud * (tiempo - frame) / tiempo

def calcular_armonico(frame):
    return calcular_amplitud(frame) * np.cos(2 * np.pi * frame / periodo)

frames = np.linspace(0, tiempo, 201)
valores = []
for frame in frames:
    valores.append(calcular_armonico(frame))

plt.figure()
plt.plot(frames, valores, '-b')
plt.show()
