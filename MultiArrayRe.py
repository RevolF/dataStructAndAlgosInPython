# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:53:25 2017

@author: thor
"""

# implementation of the multiarray ADT using a 1-D array
from arrayRe import Array

class MultiArray:
	def __init__(self,*dimensions):
		assert len(dimensions)>1,'the array must have 2 or more dimensions'
		self._dims=dimensions
		size=1
		for d in dimensions:
			assert d>0,'dimensions must be >0'
			size+=d
		self._elements=Array(size)
		self._factors=Array(len(dimensions))
		self._computeFactors()
	def numDims(self):
		return len(self._dims)
	def length(self,dim):
		assert dim>=1 and dim<len(self._dims),'dimension component out of range'
		return self._dims[dim-1]
	def clear(self,value):
		self._elements.clear(value)
	def __getitem__(self,ndxTuple):
		assert len(ndxTuple)==self.numDims(),'invalid # of array subscript'
		index=self._computIndex(ndxTuple)
		assert index is not None,'array subscript out of range'
		return self._elements[index]
	def __setitem(self,ndxTuple,value):
		assert len(ndxTuple)==self.numDims(),'invalid # of array subscript'
		index=self._computeIndex(ndxTuple)
		assert index is not None,'array subscript out of range'
		self._elements[index]=value
	def _computeIndex(self,idx):
		offset=0
		for j in range(len(idx)):
			if idx[j]<0 or idx[j]>=self._dims[j]:
				return None
			else:
				offset+=idx[j]*self._factors[j]
		return offset
	def _compiteFactors(self):
		pass





























