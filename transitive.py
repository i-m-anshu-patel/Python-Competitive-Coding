# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 16:49:09 2020

@author: HP
"""
    
    
def transitive(relation):
    temp=1
    for i in range(5):
        for j in range(5):
            if i==j:
                continue
            for k in range(5):
                if j==k or i==k:
                    continue
                if relation[i][k] >= min(relation[i][j], relation[j][k]):
                    temp=1
                else:
                    temp=0
                    break
            if temp==0:
                    break
        if temp==0:
            break
    if temp==1:
        return "Transitive relation"
    else:
        return " Non Transitive relation"
        
print(transitive([[1, 1, 0, 0, 1],
          [1, 1, 0, 0, 1],
          [0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0],
          [1, 1, 0, 0, 1]]))   
print(transitive([[1, 1, 1, 0, 1],
          [1, 1, 0, 0, 1],
          [0, 0, 1, 1, 0],
          [0, 0, 1, 0, 0],
          [1, 1, 0, 0, 1]]))    