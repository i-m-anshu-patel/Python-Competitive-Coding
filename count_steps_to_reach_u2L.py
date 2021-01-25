# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 05:01:48 2020

@author: HP
"""


# a='abc'
# count=0
# if a[0].islower():
#     for i in a:
#         count+=1
#         if i.isupper():
#             break
#         else:
#             print("0")
# else:            
#     for i in a:
#         count+=1
#         if i.isupper():
#             break
#         else:
#             print("0")
        
# print(count-1)   

def steps_to_convert(a):
    count=0
    if a[0].islower():
        for i in a:
            count+=1
            if i.isupper():
                return count-1
        return 0
    elif a[0].isupper():
         for i in a:
            count+=1
            if i.islower():
                return count-1
         return 0
        
print(steps_to_convert("abadsCERGFD"))        
print(steps_to_convert('abc'))
print(steps_to_convert('ABC'))
print(steps_to_convert("CERGFDabads"))    
    