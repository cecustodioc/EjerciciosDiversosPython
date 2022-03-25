# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 14:58:13 2021

@author: cecustodioc
"""

import numpy as np
import matplotlib.pyplot as plt
v0 = 5
g = 9.81
t = np.linspace(0,1,1001)
y=v0*t-0.5*g*t**2
plt.plot(t,y)
plt.xlabel('tiempo (s)')
plt.ylabel('altura (m)')
plt.plot()