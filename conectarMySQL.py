#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 00:31:24 2021

@author: cecustodioc
"""
import pymysql

conn = pymysql.connect(
    host="localhost", port=3306, user="id14662739_adminsysgc",
    passwd="AlmaEdith_080801", db="id14662739_girlcrush", charset="utf8")

cursor = conn.cursor()
cursor.execute(
    "SELECT idunidad, descripcion FROM unidad"
)
for idunidad, descripcion in cursor.fetchall():
    print("{0} {1}".format(idunidad, descripcion))
cursor.close()

# %s para integrar objetos en la consulta y prevenir inyecciones SQL.
cursor = conn.cursor()
cursor.execute(
    "INSERT INTO unidad VALUES (%s, %s)",
    ("bte", "Bote")
)
# Guardar cambios.
conn.commit()

conn.close()