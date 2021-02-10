# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 12:21:10 2021

@author: HP
"""


def iso_group(lst):
	if len(lst) == 1:
		return lst[0]
	if len(set(lst)) == 1:
		return lst
	if min(lst) != max(lst):
		lst.remove(min(lst))
	return iso_group(lst)


print(iso_group([31, 7, 2, 13, 7, 9, 10, 13]))
print(iso_group([97, 19, -18, 97, 36, 23, -97]))