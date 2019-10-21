# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:35:18 2019

@author: Agutierrez
"""

import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv("angle.csv", header=None)
plt.plot(file.index, file[0])
plt.show()
