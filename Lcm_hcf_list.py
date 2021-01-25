# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 13:42:09 2020

@author: HP
"""



# x= math.gcd(5,4)
# print(x)

import math

def find_gcd(A):
    res = A[0]
    for c in A[1:]:
        res = math.gcd(res , c)
    return res

"""
LCM(a,b)= a*b//(HCF(a,b))
"""
def lcm_of_list(A):
    res = A[0]
    for i in A[1:]:
        res= res*i//(math.gcd(res,i))
    return res    

print(find_gcd([12, 24, 27, 30, 36]))
print(lcm_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# a= [1,2,3,4,5,6,7,8]
# print(a[1:])