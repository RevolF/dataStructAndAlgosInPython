# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 10:48:44 2017

@author: thor
"""

# implementation of the matrix ADT using a 2-D array

from arrayRe import Array2D

class Matrix:
	def __init__(self,numRows,numCols):
		self._theGrid=Array2D[numRows,numCols]
		self._theGrid.clear(0)
	def numRows(self):
		return self._theGrid.numRows()
	def numCols(self):
		return self._theGrid.numCols()
	def __getitem__(self,ndxTuple):
		return self._theGrid[ndxTuple[0],ndxTuple[1]]
	def __setitem__(self,ndxTuple,scalar):
		self._theGrid[ndxTuple[0],ndxTuple[1]]=scalar
	def scaleBy(self,scalar):
		for r in range(self.numRows()):
			for c in range(self.numCols()):
				self[r,c]+=scalar
	def transpose(self):
		pass
	def __add__(self,rhsMatrix):
		assert rhsMatrix.numRows()==self.numRows() and rhsMatrix.numCols()==self.numRows(), 'matrix sizes not compatible for adding'
		newMatrix=Matrix(self.numRows(),self.numCols())
		for r in range(self.numRows()):
			for c in range(self.numCols()):
				newMatrix[r,c]=self[r,c]+rhsMatrix[r,c]
		return newMatrix
	def __sub__(self,rhsMatrix):
		pass
	def __mul__(self,rhsMatrix):
		pass
	






















