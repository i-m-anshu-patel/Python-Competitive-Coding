# -*- coding: utf-8 -*-
"""
Created on Tue May  5 23:21:32 2020

@author: HP
"""

def greet_people(names):
    mylst=[] 
    if len(names)!=0:
      for i in names: 
        result='Hello '+i
        mylst.append(result)
        u=", ".join(mylst)
    else:
        u='""'
    return u  

print(greet_people(['Hasika',"Hansa","Bandar","Baby" ] ))
print(greet_people([] ))
