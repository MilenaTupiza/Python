# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 19:02:38 2020

@author: PC-Home
"""


import numpy as np
matrix_aux = [[1,2,3],
     [4,5,6]]

m = np.array(matrix_aux)
l = np.zeros((3, 3))
print(l)
[[ 0.  0.  0.]
 [ 0.  0.  0.]
 [ 0.  0.  0.]]
l = np.ones([3,3])
print(l)
[[ 1.  1.  1.]
 [ 1.  1.  1.]
 [ 1.  1.  1.]]
l = np.diag([1,1,1])
print(l)
[[1 0 0]
 [0 1 0]
 [0 0 1]]
print(m[1,1])
print(m[:,2])
print(m[0,:])
print(m[0,::-1])
