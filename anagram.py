# -*- coding: utf-8 -*-
"""
Created on Wed May  6 06:02:09 2020

@author: HP
"""

def is_anagram(s1, s2):
    a=s1.lower()
    b=sorted(a)
    x=s2.lower()
    y=sorted(x)
    if b==y:
        return True
    else:
        return False
    
print(is_anagram("cristian", "Cristina"))
print(is_anagram("Nope", "Note"))    