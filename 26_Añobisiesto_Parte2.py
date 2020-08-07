# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:25:59 2020

@author: PC-Home
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

datoaño= [1900, 2000, 2016, 1987]
datosmes = [ 2, 2, 1, 11]
datorespuesta = [28, 29, 31, 30]
for i in range(len(datoaño)):
	years = datoaño[i]
	month= datosmes[i]
	print(years,month,"-> ",end="")
	result = diasmes(years, month)
	if result == datorespuesta[i]:
		print("OK")
	else:
		print("Fail")