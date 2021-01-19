# -*- coding: utf-8 -*-
"""
Created on Sun May 24 10:04:14 2020

@author: HP
"""

# n=4
# a=np.array([], dtype='i')
# for i in range(n**2):
#     if i%(n+1)==0: 
#         a=np.append(a,1)
#     else:
#         a=np.append(a,0)   
# new=a.reshape(n,n)
# print(new)
# b=np.flip(new, axis=1)
# print(b)
import numpy as np
def id_mtrx(n):
    m=abs(n)
    a=np.array([], dtype='i')
    for i in range(m**2):
        if i%(m+1)==0: 
            a=np.append(a,1)
        else:
            a=np.append(a,0)   
    new=a.reshape(m,m)
    if n<0:
        b=np.flip(new, axis=1)
        return b
    else:
        return new
    
print(id_mtrx(-3))    
print(id_mtrx(3))  
print(id_mtrx(1))  