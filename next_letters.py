# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 14:17:51 2021

@author: HP
"""


def next_letters(s):
    x = [i for i in s]
    if len(s)==0:
        return 'A'
    for i in range(len(x)):
        if (x[len(x)-1-i])=="Z":
            if len(x)-1-i==0:
                x[len(x)-1-i]="AA"
            else:
                x[len(x)-1-i]="A"
        else:
            y = ord(x[len(x)-1-i])
            x[len(x)-1-i]=chr(y+1)
            break
    return "".join(x)

print(next_letters("A"))
print(next_letters("ABC"))
print(next_letters("Z"))
print(next_letters("CAZ"))
print(next_letters(""))