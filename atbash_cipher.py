# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 14:14:13 2020

@author: HP
"""
      

def atbash(txt):
    mylst=[]
  
    for i in txt:
        m=ord(i)
        if i.isupper():
            res=90-(m-65)
            mylst.append(chr(res))
        elif i.islower():
            res1=122-(m-97)
            mylst.append(chr(res1))
        else:
            mylst.append(i)
    return "".join(mylst)       
    


print(atbash("Christmas is the 25th of December"))
print(atbash("Hello world!"))