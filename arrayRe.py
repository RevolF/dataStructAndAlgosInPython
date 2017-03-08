# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:39:40 2017

@author: thor
"""

# implements the Array ADT using array capabilities of the ctype module
# os.chdir(u'D:\\thor\\documents\\learning_resource\\PYTHON\\data_struct_algo_using_python')
# use reload(arrayRe) for reloading module after modification

import ctypes

class Array:
	def __init__(self,size):
		assert size>0, 'Array size must be >0'
		self._size=size
		PyArrayType=ctypes.py_object*size
		self._elements=PyArrayType()
		self.clear(None)
		self._curIndex=0
	def __len__(self):
		return self._size
	def __getitem__(self,index):
		assert index>=0 and index < len(self), 'Array subscript out of range'
		return self._elements[index]
	def __setitem__(self,index,value):
		assert index>=0 and index<len(self), 'Array subscript out of range'
		self._elements[index]=value
	def clear(self,value):
		for i in range(len(self)):
			self._elements[i]=value
	'''
	def __iter__(self):
		return _ArrayIterator(self._elements)
	'''
	def __iter__(self):
		return self
	def next(self):
		if self._curIndex==len(self._elements):
			raise StopIteration
		else:
			self._curIndex+=1
			return self._elements[self._curIndex-1]
	
#==============================================================================
# class _ArrayIterator:
# 	def __init__(self,theArray):
# 		self._arrayRef=theArray
# 		self._curNdx=0
# 	def __iter__(self):
# 		return self
# 	def __next__(self):
# 		if self._curNdx<len(self._arrayRef):
# 			entry=self._arrayRef[self._curNdx]
# 			self._curNdx+=1
# 			return entry
# 		else:
# 			raise StopIteration
#==============================================================================

class Array2D:
	def __init__(self,numRows,numCols):
		self._theRows=Array(numRows)
		for i in range(numRows):
			self._theRows[i]=Array(numCols)
	def numRows(self):
		return len(self._theRows)
	def numCols(self):
		return len(self._theRows[0])
	def clear(self,value):
		for row in range(self.numRows()):
			row.clear(value)
	def __getitem(self,ndxTuple):
		assert len(ndxTuple)==2,'Invalid number of array subscripts'
		row=ndxTuple[0]
		col=ndxTuple[1]
		assert row >=0 and row <self.numRows() and col>=0 and col<self.numCols(), 'ARRAY SUBSCRIPT OUT OF RANGE'
		theIdArray=self._theRows[row]
		return theIdArray[col]
	def __setitem__(self,ndxTuple,value):
		assert len(ndxTuple)==2, 'invalid number of array subscripts'
		row=ndxTuple[0]
		col=ndxTuple[1]
		assert row>=0 and row<self.numRows() and col>=0 and col<self.numCols(),'array subscript out of range'
		theIdArray=self._theRows[row]
		theIdArray[col]=value

