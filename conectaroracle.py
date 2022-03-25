#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 09:27:34 2022
@author: cecustodioc
"""
import cx_Oracle
import pandas as pd
try: 
    dsn = cx_Oracle.makedsn("192.168.2.6", 1521, service_name="escolar")
    conn = cx_Oracle.connect(user="datos", password="datos2019", dsn=dsn,
                               encoding="UTF-8")
    sql = "select * from ciclos order by ciclo desc"
    cursor = conn.cursor()
    cursor.execute(sql)
    # Leer el nombre de la columna del campo
    index = cursor.description
    row = list()
    for i in range(len(index)):
        row.append(index[i][0])
    #  Obtener información de devolución
    data = cursor.fetchall()
    result = pd.DataFrame(list(data), columns = row)
    #Cerrar conexión, liberar recursos
    cursor.close()
except cx_Oracle.Error as error:
    print(error)
finally:
    if conn:
        conn.close()
