# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 14:23:09 2017

@author: thor
"""

# implementation of exp using recursion
def exp(x,n):
	if n==0:
		return 1
	result=exp(x*x,n//2)
	if n%2==0:
		return result
	else:
		return x*result