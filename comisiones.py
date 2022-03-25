# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 18:20:41 2021

@author: cecustodioc

Una compañía de cosméticos tiene n vendedores y paga sus comisiones como sigue:
149 o menos 25%
De 150 a 499 40%
De 500 a más 50%
Calcule la comisión por cada vendedor y el total a pagar por concepto de comisiones.

"""

def comision (sal, com):
    return sal * com

def porcentaje (sal):
    pct = .0
    if sal >= 500:
        pct = .5
    else: 
        if sal >=499:
            pct = .4
        else:
            pct = .25
    return pct

def empleado(nom, sal, com):
    com = porcentaje(sal)
    return comision(sal, com)
    
r = 'N'
while r !='S':
    nom = 0
    sal = 0
    com = 0
    pago = 0
    pago = empleado(nom,sal,com)
    print(pago)
    r = 'S'
    