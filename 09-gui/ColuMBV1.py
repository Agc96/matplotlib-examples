# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16
ColuMB0: grafica rectangulo usando plot.Rectangle
mb 18 oct 2019
@author: mblon
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.transforms import Affine2D

#
# Datos de la columna y de los movimientos
pi = np.pi

B  = 1.0
H  = 12.0
ug0  = 3.0
tet0 = 20*pi/180
fg = 1.0
fp = 5.0
wg = 2*pi*fg
wp = 2*pi*fp
dt = 0.01
Dur = 5.0
Np  = int(Dur/dt)

# Genera ug y angulo
ug   = np.zeros((Np,1))
thet = np.zeros((Np,1))
t    = np.zeros((Np,1))
for n in range(Np-1):
    tn    = n*dt
    ug[n]   = ug0*np.sin(wg*tn)
    thet[n] = tet0*np.cos(wp*tn)

# inicializa gráficos
fig = plt.figure()
ax  = plt.axes(xlim=(-H, H), ylim=(0, H+1))
# ax.axis('scaled') # No va, ya que esto limitará el rango de visión a las
# líneas dibujadas con plt.plot, en vez del rectángulo

# plotea en rojo rectangulo inicial y en verde suelo inicial
angle = 0
colu   = plt.Rectangle((-B/2, 0), B, H, angle, fill=False, color='b')
shadow = plt.Rectangle((-B/2, 0), B, H, angle, fill=False, color='r', ls='--')
ax.add_patch(colu)
ax.add_patch(shadow)

xy = np.zeros((5,2))
xy[0] = [-B, 0]
xy[1] = [B, 0]
plt.plot(xy[:,0], xy[:,1], 'g')

# Animacion
def update(frame):
    global colu
    
    n = frame
    ang = thet[n]
    sig = np.sign(ang)
    if (sig == 1):
        x = ug[n] - B/2
        y = 0
    elif (sig == -1):
        x = ug[n] + B/2 - B*np.cos(abs(ang))
        y = B*np.sin(abs(ang))

    plt.plot([x-B, x+B], [0, 0], 'g')
    # Actualizar coordenadas de la columna
    colu.set_x(x)
    colu.set_y(y)
    # Actualizar ángulo de la columna
    trans_original = ax.transData
    punto_rotacion = (-B/2, 0) if ang >= 0 else (B/2, 0)
    coords = trans_original.transform(punto_rotacion)
    trans_rotar = Affine2D().rotate_around(coords[0], coords[1], ang)
    colu.set_transform(trans_original + trans_rotar)
    # Devolver tupla con la columna actualizada
    return colu,

# call the animator.  blit=True means only re-draw the parts that have changed
anim = FuncAnimation(fig, update, frames=200, interval=20, repeat=False,
                     blit=True)

# save the animation
# anim.save('colu.gif', writer='imagemagick')

