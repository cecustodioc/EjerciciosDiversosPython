# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 21:13:33 2021

@author: cecustodioc

Este programa cálcula una sucesión del 
tipo 1 + 1/2 + 1/3 + ... + 1/n
para valores desde 1 hasta 40
y posteriormente crea con ellos una gráfica
que compara los valores de 1/n con su acumulado.

"""

def sucesion (n):
    return 1/n

def graficar(num, val, fra):
    import matplotlib.pyplot as plt
    x = num
    y = val
    z = fra
    plt.plot(x, y, color='blue', marker='x', label='acumulado')
    plt.plot(x, z, color='red', marker='o', label='1/n')
    plt.ylabel('incremento')
    plt.xlabel('valor de n')
    plt.title('1 + 1/2 + ... + 1/n + m para n = 1 hasta 20')
    plt.xticks(x, rotation = 270)
    plt.legend(loc='right')
    plt.grid(True)
    plt.show()

def limite ():
    num=[]  # cantidad de incrementos eje X
    val=[]  # valor acumulado
    fra=[]  # valor sumado
    n = 1
    a = 0
    inc = 2
    while inc > 0.05:
        inc = sucesion(n)
        a = a + inc
        #print('Para 1/{0} acumula {1} incrementa {2}'.format(n, a, inc))
        print('Para 1/{0:2d} acumula {1:.2f} incrementa {2:.3f}'.format(n, a, inc))
        # Almacenar los valores en arreglos para graficarlos
        num.append(n)
        val.append(a)
        fra.append(inc)
        n = n + 1
    graficar(num, val, fra)  # Se crea un gráfico a partir de los valores calculados

limite()  # Manda a llamar todas las funciones y presenta el gráfico
