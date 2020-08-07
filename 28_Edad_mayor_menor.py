# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:18:12 2020

@author: PC-Home
"""
print("Ingrese su nombre: ")
nombre=input()
print("Ingrese su apellido: ")
apellido=input()
print("Ingrese su ubicacion: ")
ubicacion=input()
print("ingrese su edad: ") 
edad=input()
edad=int(edad)
if edad<15:
    print(nombre+',Es un niño')
if edad>=15 and edad<18:
    print(nombre+',Es un adolescente')
if edad>=18 and edad<25:
    print(nombre+',Es un joven')
 
    
    
    

