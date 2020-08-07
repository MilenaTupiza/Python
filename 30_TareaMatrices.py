# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:15:52 2020

@author: JOEL
"""

import numpy 
import random
filas=int(input('ingrese cuantas filas se requieren:'))
columnas=int(input('ingrese cuantas columnas se requieren:'))
matrix=numpy.zeros((filas,columnas))
diagonal=numpy.zeros((filas,columnas))
diagonal2=numpy.zeros((filas,columnas))

for rangofilas in range (0,filas):
    for rangocolumnas in range (0,columnas):
        matrix[rangofilas][rangocolumnas]=random.randint(1, 100)
print (matrix)

for rangofilas in range (0,filas):
       for rangocolumnas in range (0,columnas):
              if rangofilas == rangocolumnas:
                   diagonal[rangofilas][rangocolumnas]=matrix[rangofilas][rangocolumnas]
print ('El valor de la diagonal principal de la matriz es:')
print (diagonal)
y=columnas-1
for rangofilas in range (0,filas):
    for rangocolumnas in range (0,columnas):
        if rangocolumnas==y:
            diagonal2[rangofilas][rangocolumnas]=matrix[rangofilas][rangocolumnas]
            y=y-1
print ('El valor de la diagonal secundaria de la matriz es:')
print (diagonal2)
            
