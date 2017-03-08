# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 15:05:08 2017

@author: thor
"""

# implementation of a maze
# remains to be finished using stack and recursion

from arrayRe import Array2D
from lliststack import Stack

class Maze:
	MAZE_WALL='*'
	PATH_TOKEN='x'
	TRIED_TOKEN='o'
	def __init__(self,numRows,numCols):
		self._mazeCells=Array2D(numRows,numCols)
		self._startCell=None
		self._exitCell=None
	def numRows(self):
		return self._mazeCells.numRows()
	def numCols(self):
		return self._mazeCells.numCols()
	def setWall(self,row,col):
		assert row>=0 and row<self.numRows() and \
			col>=0 and col<self.numCols(),'cell index ut of range'
		self._mazeCells.set(row,col,self.MAZE_WALL)
	def setStart(self,row,col):
		assert row>=0 and row<self.numRows() and \
			col>=0 and col<self.numCols(),'cell index out of range'
		self._startCell=_CellPosition(row,col)
	def setExit(self,row,col):
		assert row>=0 and row<self.numRows() and \
			col>=0 and col<self.numCols(),'cell index out of range'
		self._exitCell=_CellPosition(row,col)
	def findPath(self):
		
		return
	def reset(self):
		
		return
	def draw(self):
		
		return
	def _validMove(self,row,col):
		return row>=0 and row<self.numRows() \
			and col>=0 and col<self.numCols() \
			and self._mazeCells(row,col) is None
	def _exitFound(self,row,col):
		return row==self._exitCell.row and \
			col==self._exitCell.col
	def _markTried(self,row,col):
		self._mazeCells.set(row,col,self.TRIED_TOKEN)
	def _markPath(self,row,col):
		self._mazeCells.set(row,col,self.PATH_TOKEN)
		
class _CellPosition(object):
	def __init__(self,row,col):
		self.row=row
		self.col=col























