# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 02:47:03 2020

@author: HP
"""


def is_subset(lst1, lst2):
    lst1=set(lst1)
    lst2=set(lst2)
    z= lst1.issubset(lst2)
    return z

print(is_subset([3, 2, 5], [5, 3, 7, 9, 2]))
print(is_subset([8, 9], [7, 1, 9, 8, 4, 5, 6]))
print(is_subset([1, 2], [3, 5, 9, 1]))