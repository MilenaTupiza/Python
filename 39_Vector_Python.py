# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:00:52 2020

@author: PC-Home
"""
segunda=str()
auxiliar= int()
vector= [int() for ind0 in range(3,29)]
print("ingrese tamaño vector")
tamanovector=int(input())
print("Va trabajar con numeros o caracter: ")
print( "a. caracter  b. numero ")
respuesta=input(" caracter o numero")
if primera=="a":
    print("caracter")
print("ingrese el tamaño del vector")
tamanovector =int(input())
for i in range(1,tamanovector+1):
    print("ingrese un nombre",i)
    nombre=input()
    print("\n")
    vector[i-1]= nombre
for j in range(1, tamanovector+1):
     for l in range(1,tamanovector):
        if vector[l-1]> vector[l]:
            auxiliar= vector[l-1]
            vector[l-1]= vector[l]
            vector[l]= auxiliar
for k in range (1, tamanovector+1):
    print("el vector ordenaado en la posicion",k,"es",vector[k-1])
 if segunda=="b":
     print("numero")
print("ingrese tamaño vector")
tamanovector=int(input())

for i in range(1, tamanovector+1):
    vector[i-1]=randint(0,99)
    print("El valor de la posicion ",i,"es",vector[i-1])
    sleep(1)
sleep(1)
for j in range(1, tamanovector+1):
    for l in range(1, tamanovector):
        if vector[l-1]<vector[l]:
            auxiliar=vector[l-1]
            vector[l-1]=vector[l]
            vector[l]=auxiliar
for k in range(1,tamanovector+1):
    print("el vector ordenado en la posicion ",k,"es",vector[k-1])
    sleep(1)
    