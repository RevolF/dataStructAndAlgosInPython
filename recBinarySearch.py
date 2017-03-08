# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 13:59:31 2017

@author: thor
"""

# implementation of a recursive binary search on a sorted sequence
# O(1) - O(log(n))
def recBinarySearch(target,theSeq,first,last):
	if first > last:
		return False
	else:
		mid=(last+first)//2
		if theSeq[mid]==target:
			return True
		elif target< theSeq[mid]:
			return recBinarySearch(target,theSeq,first,mid-1)
		else:
			return recBinarySearch(target,theSeq,mid+1,last)
