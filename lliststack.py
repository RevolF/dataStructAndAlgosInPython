# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 13:57:46 2017

@author: thor
"""

# implementation of the stack ADT using a simple linked list

class Stack:
	def __init__(self):
		self._top=None
		self._size=0
	def isEmpth(self):
		return self._top is None
	def __len__(self):
		return self._size
	def peek(self):
		assert not self.isEmpth(), 'cannot peek at an empty stack'
		return self._top.item
	def pop(self):
		assert not self.isEmpth(), 'can not pop from an empty stack'
		node=self._top
		self._top=self._top.next
		self._size-=1
		return node.item
	def push(self,item):
		self._top=_StackNode(item,self._top)
		self._size+=1

class _StackNode:
	def __init__(self,item,link):
		self.item=item
		self.next=link


