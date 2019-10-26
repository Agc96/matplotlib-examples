# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 18:52:36 2019

@author: Agutierrez
"""

import numpy as np
import matplotlib.pyplot as plt

amplitud = 4
tiempo = 20
masa = 200
amort = 0.3
periodo = 1
velang = 2 * np.pi / periodo
assert amort < velang, "No es un movimiento armónico amortiguado"

def calcular_armonico(frame, amplitud, amort, velang):
    velang_amort = np.sqrt(velang**2 - amort**2)
    return amplitud * np.exp(-amort * frame) * np.cos(velang_amort * frame)

frames = np.linspace(0, 10, 501)
valores = []

for frame in frames:
    posicion = calcular_armonico(frame, amplitud, amort, velang)
    valores.append(posicion)

plt.figure()
plt.plot(frames, valores, '-')
plt.show()
