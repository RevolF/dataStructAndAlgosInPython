# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 10:56:41 2017

@author: thor
"""

# implementation of the sparse matrix ADT using an array of linked lists
from arrayRe import Array
class SparseMatrix:
	def __init__(self,numRows,numCols):
		self._numCols=numCols
		self._listOfRows=Array(numRows)
	def numRows(self):
		return len(self._listOfRows)
	def numCols(self):
		return self._numCols
	def __getitem__(self,ndxTuple):
		pass
	def __setitem__(self,ndxTuple,value):
		predNode=None
		row,col=ndxTuple
		curNode=self._listOfRows[row]
		while curNode is not None and curNode.col!=col:
			predNode=curNode
			curNode=curNode.next
		if curNode is not None and curNode.col==col:
			if value==0.0:
				if curNode==self._listOfRows[row]:
					self._listOfRows[row]=curNode.next
				else:
					predNode.next=curNode.next
			else:
				curNode.value=value
		elif value !=0.0:
			newNode=_MatrixElementNode(col,value)
			newNode.next=curNode
			if curNode==self._listOfRows[row]:
				self._listOfRows[row]=newNode
			else:
				predNode.next=newNode
	def scaleBy(self,scalar):
		for row in range(self.numRows()):
			curNode=self._listOfRows[row]
			while curNode is not None:
				curNode.value+=scalar
				curNode=curNode.next
	def transpose(self):
		pass
	def __add__(self,rhsMatrix):
		assert rhsMatrix.numRows()==self.numRows() and \
			rhsMatrix.numCols()==self.numCols(), \
			'matrix sizes not compatable for adding'
		newMatrix=SparseMatrix(self.numRows(),self.numCols())
		for row in range(self.numRows()):
			curNode=self._listOfRows[row]
			while curNode is not None:
				newMatrix[row,curNode.col]=curNode.value
				curNode=curNode.next
		for row in range(rhsMatrix.numRow()):
			curNode=rhsMatrix._listOfRows[row]
			while curNode is not None:
				value=newMatrix[row,curNode.col]
				value+=curNode.value
				newMatrix[row,curNode.col]=value
				curNode=curNode.next
		return newMatrix

class _MatrixElementNode:
	def __init__(self,col,value):
		self.col=col
		self.value=value
		self.next=None



