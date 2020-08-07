# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 16:56:35 2020

@author: PC-Home
"""


while True:
		print("Contador inicial: ")
		dato1 = float(input())
		print("Contador final: ")
		dato2 = float(input())
		if dato2<dato1:
			print("ERROR: EL VALOR FINAL ES MENOR AL VALOR INICIAL")
			dato2 = float(input())
		print("IMPRESION: BLANCONEGRO O COLOR")
		impresion = input()
		if impresion=="BLANCONEGRO" or impresion=="blanconegro":
			blanconegro = 0.06
			impresiones = dato2-dato1
			print("NUMERO DE IMPRESIONES ES=",impresiones)
			costo = impresiones*0.06
			print("COSTO=","$",costo)
		if impresion=="COLOR" or impresion=="color":
			color = 0.12
			impresiones = dato2-dato1
			print(" IMPRESIONES =",impresiones)
			costo = impresiones*0.12
			print("COSTO=","$",costo)
		
	