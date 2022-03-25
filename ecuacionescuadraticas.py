#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 11:54:13 2021

Este programa encuentra el o los valores posibles de X
en una ecuación cuadrática de la forma estándar ax²+bx+c,
proporcionando los valores a, b, y c

@author: cecustodioc
"""

import math

def valordiscriminante (a, b, c):
    return b**2-4*a*c # El valor del discriminante determina la forma en que se encuantra la solución.

def soluciones (disc, a, b, c):
    disc = valordiscriminante(a, b, c)
    print ('Valor del discriminante: ', disc)
    if disc > 0:
        return 2  # X tiene un valor positivo y uno negativo
    else:
        if disc == 0:
            return 1  # X tiene un solo valor
        else:
            return 0  # X tiene una solución irreal

def normal(a, b, c, disc, x1, x2):
    solucion = soluciones(disc, a, b, c)
    print ('Numero de soluciones:', solucion)
    if solucion == 0:
        print ('solucion irreal')
    else:
        if solucion == 1:
            x1 = (-b + math.sqrt(disc))/(2*a)
            print ('Valor de x: ', x1)
        else:
            x1 = (-b + math.sqrt(disc))/(2*a)
            x2 = (-b - math.sqrt(disc))/(2*a)
            print ('Valor de x1: ', x1, 'Valor de x2: ', x2)

def conceros(a, b, c, disc, x1, x2):
    if a == 0:
        print('No es una ecuación cuadrática, A no puede ser cero')
    else:
        if b == 0:
            if c == 0:
                print ('Valor de x = 0')
            else:
                tmp = (c/a)
                x1 = math.sqrt(tmp)
                x2 = math.sqrt(tmp)
                print ('Valor de x1: ', x1, 'Valor de x2: -', x2)
        else:
            if c != 0:
                x1 = -(b/a)
                print ('Valor de x: ', x1)
            else:
                normal(a, b, c, disc, x1, x2)



a = 3.0
b = 2.0
c = -8.0
disc = 0.0
x1 = 0.0
x2 = 0.0
solucion=0

conceros (a, b, c, disc, x1, x2)
