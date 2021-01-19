# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:36:57 2021

@author: HP
"""


r = "PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe, notvirus.exe"

import re
def remove_virus(files):
    s = re.sub('antivirus.exe', 'ullu', files)
    t = re.sub('notvirus.exe', 'kallu', s)
    d = re.split(', ', t)
    result= []
    for i in d:
        m = re.sub('.*virus.exe|.*malware.exe', '', i)
        result.append(m)
    result = [i for i in result if len(i)!=0]
    if len(result)==0:
        return "PC Files: Empty"
    res = ", ".join(result)
    u = re.sub('ullu','antivirus.exe',  res)
    t = re.sub('kallu', 'notvirus.exe',  u)
    f = t.strip()
    if f[-1]==',':
        return f[:-1]
    else:
        return f


print(remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg"))
print(remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe "))
print(remove_virus("PC Files: virus.exe, bestmalware.exe, memzvirus.exe"))
    

