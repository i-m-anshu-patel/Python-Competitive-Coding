# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 16:07:11 2020

@author: HP
"""
def convert_to_roman(num):
    ones = {1:'I',2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX',0:''}
    tens = {10:'X',20:'XX', 30:'XXX', 40:'XL', 50:'L', 60:'LX', 70:'LXX', 80:'LXXX', 90:'XC',0:''}
    hund = {100:'C',200:'CC', 300:'CCC', 400:'CD', 500:'D', 600:'DC', 70:'DCC', 80:'DCCC', 900:'CM',0:''}
    thou = {1000:'M',2000:'MM', 3000:'MMM'}
    roman = []
    
    temp = num
    i = 0
    while(temp>0):
        n = (temp % 10)*(10**i)
        print(n)
        if i == 0:
            roman.append(ones[n])
            
        elif i == 1:
            roman.append(tens[n])
            
        elif i == 2:
            roman.append(hund[n])
            
        else:
            roman.append(thou[n])
        
        temp = temp // 10
        i = i+1
    roman= roman[::-1] 
    m= ''.join(roman)
    return m
        
        
n = int(input('Enter an integer:'))
if n>0 and n <4000:
    print(convert_to_roman(n))
else:
    print('Invalid Input')
	
    # a=str(ones)
    # b=str(tens)
    # c=str(hunds)
    # d=str(thou)
    # print(a)
    # print(b)
    # print(c)
    # print(d)
    # x=re.sub('2','II', a)
    # y=re.sub("50", "L", b)
    # z=re.sub("500", "D", c)
    # m=re.sub("1000", "M", d)
    # print(m+z+y+x)
