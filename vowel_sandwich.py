# -*- coding: utf-8 -*-
"""
Created on Sun May 17 04:11:26 2020

@author: HP
"""


def is_vowel_sandwich(s):
    vowel='AEIOUaeiou'
    if len(s)==3:
        if s[0] not in vowel and s[2] not in vowel:
            if s[1] in vowel:
                return True
    return False        
print(is_vowel_sandwich("cat"))
print(is_vowel_sandwich("ear"))