# -*- coding: utf-8 -*-
"""
Created on Sun May 31 01:21:42 2020

@author: HP
"""


def prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False
    
def filter_primes(lst):
    mylst=[]
    for i in lst:
        x= prime(i)
        if x:
            mylst.append(i)
    return mylst

print(filter_primes([7, 9, 3, 9, 10, 11, 27]))        
print(filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70]))