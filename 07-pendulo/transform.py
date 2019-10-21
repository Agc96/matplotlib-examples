# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 18:31:53 2019

@author: Agutierrez
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot(111)
ax.set_xlim(-15,15)
ax.set_ylim(-1, 13)
plt.grid('on')

#Rotate rectangle patch object
ts = ax.transData
coords = ts.transform([3, 0])
print(coords)
tr = mpl.transforms.Affine2D().rotate_deg_around(coords[0], coords[1], 16)
t= ts + tr

#Rotated rectangle patch
rect1 = patches.Rectangle((3,0),1,12,alpha=0.5,color='blue',transform=t)
ax.add_patch(rect1);

#The (desired) point of rotation

plt.show()
