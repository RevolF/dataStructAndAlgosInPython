# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:00:56 2017

@author: thor
"""

# defines searching and sorting


# implement of binary search
# worst time consuming would be O(log n)
def binarySearch(theValues,target):
	low=0
	high=len(theValues)-1
	while low<=high:
		mid=(high+low)//2
		if theValues[mid]==target:
			return True
		elif target<theValues[mid]:
			high=mid-1
		else:
			low=mid+1
	return False
	

# bubble sort
# O(n2) to O(n)
def bubbleSort(theSeq):
	n=len(theSeq)
	for i in range(n):
		for j in range(i+1,n):
			if theSeq[i]>theSeq[j]:
				theSeq[i],theSeq[j]=theSeq[j],theSeq[i]
	return theSeq

# selection sort O(n2), but reduces swap times to O(n)
def selectionSort(theSeq):
	n=len(theSeq)
	for i in range(n-1):
		smallNdx=i
		for j in range(i+1,n):
			if theSeq[j]<theSeq[smallNdx]:
				smallNdx=j
		if smallNdx!=i:
			theSeq[i],theSeq[smallNdx]=theSeq[smallNdx],theSeq[i]
			
	return theSeq

# insertion sort O(n2)
def insertionSort(theSeq):
	n=len(theSeq)
	for i in range(1,n):
		value=theSeq[i]
		pos=i
		while pos>0 and value<theSeq[pos-1]:
			theSeq[pos]=theSeq[pos-1]
			pos-=1
			theSeq[pos]=value
	return theSeq
	
# shell sort
def shellSort(lists):
	count=len(lists)
	step=2
	group=count//step
	while group>0:
		for i in range(0,group):
			j=i+group
			while j<count:
				k=j-group
				key=lists[j]
				while k>=0:
					if lists[k]>key:
						lists[k+group]=lists[k]
						lists[k]=key
					k-=group
				j+=group
		group //= step
	return lists
	
# quick sort, when runniing falls into a infinite recursion
# remains a question, should refer to algo and struct in C
def quickSort(array,low,high):
	if low<high:
		keyIndex=partion(array,low,high)
		quickSort(array,low,keyIndex)
		quickSort(array,keyIndex,high)
	
def partion(array,low,high):
	key=array[low]
	while low<high:
		while low<high and array[high]>=key:
			high-=1
		if low<high:
			array[low]=array[high]
		while low<high and array[low]<key:
			low+=1
		if low<high:
			array[high]=array[low]
	array[low]=key
	return low
	


ar=[2,5,7,3,4,1,8]
quickSort(ar,0,len(ar)-1)
	


























