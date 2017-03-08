# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 15:25:32 2017

@author: thor
"""

# solving the n-queues problem using the recursive function

def solveNQueens(board,col):
	if board.numQueens()==board.size():
		return True
	else:
		for row in range(board.size()):
			if board.unguarded(row,col):
				board.placeQueen(row,col)
				if board.solveNQueens(board,col+1):
					return True
				else:
					board.removeQueen(row,col)
		return False

