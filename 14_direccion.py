# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:37:42 2020

@author: PC-Home
"""
def direccion(calle, sector, codpostal, referencia, numcasa):
    print("Su direccion es: ","Su sector es:", sector, "calle", calle)
    print("su casa es la #: ", numcasa, "Codigo postal #:", codpostal)
    print ("Esta cerca de: ",referencia)
print("Ingrese los datos que solicitan de direccion ")
calle=input("ingrese la calle: ")
sector=input("Ingrese el sector de resisdencia: ")
codpostal=input("Ingrese codigo portal:")
referencia=input("Ingrese una referencia de su domicilio:")
num=input("Ingrese el # de casa:")

direccion(calle,sector,codpostal,referencia,num)