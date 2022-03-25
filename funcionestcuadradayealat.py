# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 23:10:50 2021
Dibuja dos curvas de funciones trigonométricas en el mismo gráfico
@author: cecustodioc
"""

import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(-2,2,100)
f_values = t**2
g_values = np.exp(t)
plt.plot(t,f_values,'r',t,g_values,'b--')
plt.xlabel('t')
plt.ylabel('f , g')
plt.legend(['t^2','e^t'])
plt.title('Gráfico de dos funciones (t^2 y e^t)')
plt.grid('on')
plt.axis([-3,3,-1,10])
plt.show()