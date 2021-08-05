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
ax  = plt.axes()
ax.set(xlim=(-H, H), ylim=(0, H))
ax.axis('scaled')

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
    n = frame
    ang = thet[n]
    if ang > 0:
        x = ug[n] - B/2
        y = 0
    elif ang < 0:
        x = ug[n] + B/2 - B*np.cos(abs(ang))
        y = B*np.sin(abs(ang))

    plt.plot([x-B, x+B], [0, 0], 'g')
    # Actualizar columna
    colu.set_x(x)
    colu.set_y(y)
    # Actualizar ángulo
    # colu.angle = ang # TODO: Moverlo a transformadas
    return colu,

# call the animator.  blit=True means only re-draw the parts that have changed
anim = FuncAnimation(fig, update,frames=200,interval=20, repeat = False, blit=True)

# save the animation
# anim.save('colu.gif', writer='imagemagick')

