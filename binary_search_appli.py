# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 16:52:19 2020

@author: HP
"""


prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# print(len(primes))
# print(primes[(len(primes)-1)//2])
# l = [ i for i in primes[0:(len(primes)-1)//2]]
# print(s)
# r = [ i for i in primes[((len(primes)-1)//2)+1:]]
# print(t)

def is_prime(primes, num, left=0, right=None):
	right = len(primes)
	while (left < right):
		mid = (left + right) // 2
		if num == primes[mid]:
			return "yes"
		elif num < primes[mid]:
			right = mid
		else:
			left = mid + 1
	return "no"
    
    
print(is_prime(prime, 5))
print(is_prime(prime, 36))



        