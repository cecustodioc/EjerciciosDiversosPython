# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 23:23:31 2021

Este programa nos enseña como colocar dos gráficos en un mismo lienzo 
utilizando las librerias numpy y el módulo pyplot de la librería
mathplotlib.

@author: cecustodioc
"""
import numpy as np
import matplotlib.pyplot as plt

# 1 división horizontal, 2 divisiones vertical, posición 1
plt.subplot(1,2,1)

# Aquí establecemos los valores para el primer gráfico
v0 = 5  # Velocidad inicial del objeto
g = 9.81 # Constante de la gravedad
t = np.linspace(0,1,15) # Establece el intervalo de valores 
                        # y su separación para el eje X
y=v0*t-0.5*g*t**2  # Fórmula para cálcular los valores de Y

plt.plot(t,y,color='red',marker='o')  # Cálcula los pares de valores
                                      # y establece las características 
                                      # de la línea que se trazar+a en 
                                      # el lienzo para los pares de valores 
                                      # (X,Y)
plt.xlabel('tiempo (s)')  # Pone una etiqueta para el eje X
plt.ylabel('altura (m)')  # Pone una etiqueta para el eje Y
plt.title('movimiento vertical')  # Pone un título al gráfico 1
plt.grid('on')  # dibuja la malla de gráfico

# 1 división horizontal, 2 divisiones vertical, posición 2
plt.subplot(1,2,2)  
t = np.linspace(-2,2,15)  # Intervalo de valores en el eje X
f_values = t**2  # fórmula para calcular los valores de la serie 1 
                 # del eje Y
g_values = np.exp(t) # fórmula para álcular los valores de serie 2 
                     # del eje Y
plt.plot(t,f_values,'r:o',t,g_values,'b--x') # Hráfica las dos series 
                                             # de datos
plt.xlabel('tiempo')  # Etiqueta para el eje X
plt.ylabel('Valor')  # etiqueta para el eje Y
plt.legend(['t^2','e^t'])  # etiqutas para las series de datos
plt.title('Funciones')  # título del gráfico
plt.grid('on')  # dibuja la malla de gráfico
plt.axis([-3,3,-1,10])  # Define los valores máximo y mínimo
                        # de los ejes

plt.tight_layout() # Evita que las etiquetas de los gráficos 
                   # se traslapen
plt.show()  # Dibuja los gráficos en el lienzo