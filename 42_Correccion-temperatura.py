# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 16:57:55 2020

@author: PC-Home
"""
temp=[]
n =int(input("Ingrese cantidad de temperaturas[1,10]: "))

for i in range (n):
    num= int(input("Temperatura N* en °C: "))
    temp.append(num)
print(temp)
cgaseoso= 0
cliquido = 0
csolido = 0

for num in temp:
    if (num==100 or num>100) :
        print(num,"Gaseoso", sep="\M")
        cgaseoso+=1
    elif (num<0 or num==0):
        print(num, "Sólido", sep="\M")
        csolido += 1
    elif (num>0 or num<100):
        print(num, "liquido", sep="\M")
        cliquido += 1

print("RESUMEN DEL ANÁLISIS DE MUESTRAS DE AGUA")
print("Cantidad de muestras sólidas: ", csolido)
print("Cantidad de muestras líquidas: ", cliquido)
print("Cantidad de muestras gaseosas: ", cgaseoso)