# -*- coding: utf-8 -*-
"""
Created on Sun May 17 03:45:43 2020

@author: HP
"""


def count_palindromes(num1, num2):
    count=0
    for i in range(num1, num2+1):
        a=str(i)[::-1]
        b=str(i)
        if a==b:
            count+=1
    return count        


print(count_palindromes(1, 10))
print(count_palindromes(878, 898))
print(count_palindromes(555, 556))