# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
def añobisiesto (año) :
  if año % 4 != 0:
    return False
  elif año % 100 != 0:
    return True 
  elif año % 400 != 0:
    return False 
  else:
    return True 

def diasmes(year,month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and añobisiesto(year):
		res = 29
	return res

datosaño= [1900, 2000, 2016, 1987]
datosmes = [ 2, 2, 1, 11]
datosrespuestas = [28, 29, 31, 30]
for i in range(len(datosaño)):
	años = datosaño[i]
	mes = datosmes[i]
	print(años,mes,"-> ",end="")
	result = diasmes(años)
	if result == datosrespuestas[i]:
		print("OK")
	else:
		print("Fail")