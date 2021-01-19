# -*- coding: utf-8 -*-
"""
Created on Sat May  2 19:24:12 2020

@author: HP
"""
def is_isogram(txt):
  return len(txt) == len(set(txt.lower()))
        
        
print(is_isogram('Abcdefg'))
print(is_isogram('abcdafg'))