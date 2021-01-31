# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 00:33:27 2021

@author: HP
"""


a= "10#11#12"


def decrypt(s):
    diction = {}
    for i in range(1,27):
        diction[str(i)]= chr(96+i)
    r=''
    result=[]
    for i in s:
        if i=='#':
            if len(r)<2:
                result.append(diction[r])
                r=""
            else:
                for k in r[0:-2]:
                    result.append(diction[k])
                result.append(diction[r[-2]+r[-1]])
                r=""
        else:
            r+=i
    for j in r:
        result.append(diction[j])
    
    return "".join(result)

print(decrypt(a))
print(decrypt("1326#"))
print(decrypt("25#"))
    
