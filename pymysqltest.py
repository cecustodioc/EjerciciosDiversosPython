# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 16:51:12 2021

@author: cecustodioc
"""

import pymysql
try:
    conexion = pymysql.connect(host = 'localhost',
        user='root',
        password='',
        db='test')
    print('conexion correcta')
except (pymysql.err.OperationalError, pymysql.InternalError) as e:
    print('ocurrio un error al conectar:',e)