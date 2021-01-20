# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 15:39:27 2020

@author: HP
"""




               
def super_reduced_string(txt):
    q=[]
    for c in txt:
        if q and c== q[-1]:
            q.pop()
        else:
            q.append(c)
    return "".join(q) if q else 'Empty String'        
    
# print(super_reduced_string(a))
print(super_reduced_string('zhhnnti'))
print(super_reduced_string('aabc'))
    