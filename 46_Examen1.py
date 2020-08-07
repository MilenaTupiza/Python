# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:34:17 2020

@author: PC-Home
"""


temperatura=[]
cantidad =int(input("Ingrese cantidad de temperaturas[1,10]: "))

for i in range (n):
    num= int(input("Temperatura en C° %d"%i))
    temp.append(num)
print(temp)
gaseoso= 1
liquido = 2
solido = 3
for num in temp:
    if (num==100 or num>100) :
        print(num,"Gaseoso", sep="\t")
        gaseoso+=1
    elif (num<0 or num==0):
        print(num, "Sólido", sep="\t")
        solido += 1
    elif (num>0 or num<100):
        print(num, "liquido", sep="\t")
        liquido += 1
else:
    print("error de ingreso")

print("El resumen de analisis es: )
print("Cantidad de muestras sólidas: ", solido)
print("Cantidad de muestras líquidas: ", liquido)
print("Cantidad de muestras gaseosas: ", gaseoso


