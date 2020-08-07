# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:42:26 2020

@author: PC-Home
"""
cal1= int(input("Ingrese su primera calificacion: "))
cal2= int(input("Ingrese su segunda calificacion: "))
cal3= int(input("Ingrese su tercera calificacion: "))
if cal1>=cal3 and cal2>=cal3:
    suma=cal1+cal2
    print ("suma")
else:
    if cal1>=cal2 and cal3>=cal2:
            suma= cal1+cal3
            print ("suma")
    else:
                suma=cal2+cal3
                print("suma")
print("La calificacion total es: ",suma)
            