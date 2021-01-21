# -*- coding: utf-8 -*-
"""
Created on Fri May  1 10:09:45 2020

@author: HP
"""

def hamming_distance(txt1, txt2):
  m=0
  for i in range(len(txt1)):
      if (txt1[i]!=txt2[i]):
          m+=1
  return m			

print(hamming_distance("abcde", "bcdef"))
print(hamming_distance("abcde", "abcde"))
print(hamming_distance("strong", "strung"))