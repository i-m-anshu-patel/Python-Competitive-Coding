# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 14:04:18 2020

@author: HP
"""


# import numpy as np     
# def can_see_stage(seats):
#     if(len(seats)==0):
#         return True
#     arr = np.array(seats)
#     arr= arr.reshape(-1)
#     for i in range(len(seats[0])):
#         for j in range(0,(len(seats[0]*len(seats))),len(seats[0])):
#             if (arr[i]>arr[i+j]):
#                 return False
#     seats.pop(0)
#     return can_see_stage(seats)

import numpy as np     
def can_see_stage(seats):
    arr = np.array(seats)
    ar= arr.T
    for i in range(len(ar)):
        if len(set(ar[i]))!=len(ar[i]):
            return False
        else:
            b= np.sort(ar[i])
            if not np.array_equal(ar[i],b):
                return False
    return True
            
        
a=[[1, 2, 3, 2, 1, 1], 
[2, 4, 4, 3, 2, 2], 
[5, 5, 5, 5, 4, 4], 
[6, 6, 7, 6, 5, 5]]

# a=[ [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]]
print(can_see_stage([[1, 1, 2], 
[5, 2, 3], 
[4, 4, 4]]))
print(can_see_stage([[1, 1, 2], 
[5, 2, 3], 
[6, 4, 4]]))
print(can_see_stage([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]))
print(can_see_stage([[1, 2, 2], 
[1, 2, 3], 
[4, 4, 4]]))
print(can_see_stage([
  [0, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]))
print(can_see_stage([
  [2, 0, 0], 
  [1, 1, 1], 
  [2, 2, 2]
]))
print(can_see_stage(a))
print(can_see_stage([[1, 2, 3, 2, 1, 1], 
[2, 4, 4, 3, 2, 2], 
[5, 5, 5, 10, 4, 4], 
[6, 6, 7, 6, 5, 5]]))