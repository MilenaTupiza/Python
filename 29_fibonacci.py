# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:13:38 2020

@author: PC-Home
"""
def fibonacci(f):
    a =0
    b=1
    while a <= f:
        print(a, end=' ')
        a,b = b, a+b
    print()
fibonacci(8)


