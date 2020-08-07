# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:13:18 2020

@author: PC-Home
"""


htrabajadas= int(input("Horas trabajadas: "))
tarifa= int(input("Tarifa por hora:"))
descuento=int(input("E l descuento es: "))
if htrabajadas<=40:
    total=htrabajadas*tarifa - descuento
else: 
total=40*tarifa+1.5*tarifa*(htrabajadas-40)-descuento
       print("El vcalor a pagar es: ", total)