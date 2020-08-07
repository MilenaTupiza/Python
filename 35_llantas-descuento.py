# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:21:29 2020

@author: PC-Home
"""


cantidad= int(input("cantidad de llantas: "))
precio= float(input("Precio unitario:"))
if cantidad >= 4:
   precio=0.9*precio
total=cantidad*precio
print(" El valor a pagar es:", total)


