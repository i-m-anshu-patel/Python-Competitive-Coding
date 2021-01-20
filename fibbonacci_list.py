# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:37:36 2020

@author: HP
"""


def fib(n):
    lst=[0,1]
    for i in range(1,n):
        sum = lst[i-1]+lst[i]
        lst.append(sum)
    return lst

print(fib(1))
print(fib(2))
print(fib(6))
print(fib(3))