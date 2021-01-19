# -*- coding: utf-8 -*-
"""
Created on Mon May 11 22:54:02 2020

@author: HP
"""
#Make a function that encrypts a given input with these steps:

# x='banana'
# a=x[::-1]
# print(a)
# mylst=[]
# for i in a:
#     if i=='a':
#         mylst.append('0')
#     elif i=='e':
#         mylst.append('1')
#     elif  i=='o':
#         mylst.append('2')
#     elif  i=='u':
#         mylst.append('3')
#     else:
#         mylst.append(i)
# mylst.append("aca")
# b=''.join(mylst)
# print(b)
def encrypt(word):
    a=word[::-1]
    print(a)
    mylst=[]
    for i in a:
        if i=='a':
            mylst.append('0')
        elif i=='e':
            mylst.append('1')
        elif  i=='o':
            mylst.append('2')
        elif  i=='u':
            mylst.append('3')
        else:
            mylst.append(i)
    mylst.append("aca")
    b=''.join(mylst)
    return b
print(encrypt("banana"))
print(encrypt("karaca"))
print(encrypt("alpaca"))
##Alternate
#def encrypt(word):
# 	word = word[::-1]
# 	for r in (("a", "0"), ("e", "1"), ("o", "2"), ("u", "3")):
# 		word = word.replace(*r)
		
#	return word+'aca'