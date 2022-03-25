# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 01:14:50 2021

@author: cecustodioc
"""

# Programa para calcular la altura de un balòn en movimiento vertical
# v0 es la velocidad inicial, g es la aceleración de la gravedad, t es el tiempo

v0 = 5; g = 9.81; t = 0.6
y= v0*t - 0.5*g*t**2
print(y)

# Calcular el angulo del objeto dadas sus posiciones
from math import atan, pi, cos, tan, sin
x = 10.0
y = 10.0
angle = atan(y/x)
print((angle/pi)*180)
b = cos(6)
c = tan (6)
d = sin(6)
print (b, c, d)

from numpy import exp
a = exp([1, 2, 3])
print(a)

