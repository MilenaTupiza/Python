# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:33:49 2020

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

def diasmes(year, month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and añobisiesto(year):
		res = 29
	return res

def diaño(year, month, day):
	days = 0
	for m in range(1, month):
		md = diasmes(year, m)
		if md == None:
			return None
		days += md
	md = diasmes(year, month)
	if day >= 1 and day <= md:
		return days + day
	else:
		return None

print(diaño(2000, 12, 31))