# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:34:01 2020

@author: PC-Home
"""


vector=int(input())
nombre=input()
numeros=input()
print("trabajara con números o con caracteres?.")
if vector >=3 and vector <=30:
    auxiliar= str()
    nombre= str()
    vector = [str() for ind0 in range(100)]
    print("ingrese el tamaño del vector")
    tamanovector =int(input())
    for i in range(1,tamanovector+1):
        print("ingre un nombre",i)
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
else:
    from random import randint
    from time import sleep
    auxiliar = int()
    vector = [int()for ind0 in range(100)]
    print("ingrese tamaño vertor")
    tamanovector = int(input())
    for i in range(1,tamanovector+1):
        vector[i-1] = randint(0,99)
        print("el valor de la posicion ",i,"es",vector[i-1])
        sleep(1)
    sleep(1)
    for j in range(1, tamanovector+1):
        for l in range(1,tamanovector):
            if vector[l-1]> vector[l]:
                auxiliar= vector[l-1]
                vector[l-1]= vector[l]
                vector[l]= auxiliar
    for k in range (1, tamanovector+1):
        print("el vector ordenaado en la posicion",k,"es",vector[k-1])
        sleep(1)