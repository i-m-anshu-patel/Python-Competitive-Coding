# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:41:54 2020

@author: HP
"""

import re
def censor_string(txt, lst, char):
    x=re.split('\s',txt)
    for i in x:
        if i in lst:
              n=x.index(i)
              x.remove(i)
              x.insert(n, char*len(i))
    res=" ".join(x)
    return res
            
# def censor_string(txt, lst, character):
#     for word in lst:
#         txt = txt.replace(word, character*len(word))
#     return txt

print(censor_string("Today is a Wednesday!", ["Today", 'a'],"-"))
print(censor_string("The cow jumped over the moon.", ["cow", "over"], "*"))
print(censor_string("Why did the chicken cross the road ?", ["did", "chicken", "road"], "?"))


# a='today is a wednesday!'
# char='*'
# lst=['today','wednesday']
# x=re.split('\s',a)
# for i in x:
#     if i in lst:
#         n=x.index(i)
#         m= x.remove(i)
#         o= x.insert(n, char*len(i))
# res=" ".join(x)
# print(a)        
# print(res)