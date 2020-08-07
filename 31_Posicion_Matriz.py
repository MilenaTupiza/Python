# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:34:39 2020

@author: PC-Home
"""


matrix=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
for i in range (0,5):
    for j in range (0,6):
        print ("Ingrese el numero de la posicion: ",i,j)
        matrix[i][j]=int(input())
print(matrix)