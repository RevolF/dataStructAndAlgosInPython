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


# implementation of merge sort
# note that strange value error happens in merge sort
def mergeSort(theSeq):
    n=len(theSeq)
    tmpArray=[0 for i in range(n)]
    recMergeSort(theSeq,0,n-1,tmpArray)

def recMergeSort(theSeq,first,last,tmpArray):
    if first==last:
        return
    else:
        mid=(first+last)//2
        recMergeSort(theSeq,first,mid,tmpArray)
        recMergeSort(theSeq,mid+1,last,tmpArray)
        mergeVirtualSeq(theSeq,first,mid+1,last+1,tmpArray)
        
def mergeVirtualSeq(theSeq,left,right,end,tmpArray):
    a=left
    b=right
    m=0
    while a<right and b<end:
        if theSeq[a]<theSeq[b]:
            tmpArray[m]=theSeq[b]
            a+=1
        else:
            tmpArray[m]=theSeq[b]
            b+=1
        m+=1
        
    while a<right:
        tmpArray[m]=theSeq[a]
        a+=1
        m+=1
        
    while b<end:
        tmpArray[m]=theSeq[b]
        b+=1
        m+=1
    
    for i in range(end-left):
        theSeq[i+left]=tmpArray[i]
        
# implementation of quick sort
# report index error in several cases
def quickSort(theSeq):
    n=len(theSeq)
    recQuickSort(theSeq,0,n-1)
    
def recQuickSort(theSeq,first,last):
    if first==last:
        return
    else:
#        pivot=theSeq[first]
#        print('rec:',first,last)
        pos=partitionSeq(theSeq,first,last)
#        print('rec pos:',pos)
        recQuickSort(theSeq,first,pos-1)
        recQuickSort(theSeq,pos+1,last)
        
def partitionSeq(theSeq,first,last):
    pivot=theSeq[first]
    left=first+1
    right=last
    while left<=right:
        while left<right and theSeq[left]<pivot:
            left+=1
        while right>=left and theSeq[right]>=pivot:
            right-=1
        if left<right:
            tmp=theSeq[left]
            theSeq[left]=theSeq[right]
            theSeq[right]=tmp
    if right!=first:
#        print('partition:',first,right)
#        print('value:',theSeq[first],theSeq[right])
        theSeq[first]=theSeq[right]
        theSeq[right]=pivot
    print(right)
    return right





























