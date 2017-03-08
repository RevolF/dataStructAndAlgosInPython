# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 10:09:40 2017

@author: thor
"""

# implements of the bag ADT using a simply linked list

class Bag:
	def __init__(self):
		self._head=None
		self._size=0
		self._curIdx=0
	def __len__(self):
		return self._size
	def __contains__(self,target):
		curNode=self._head
		while curNode is not None and curNode.item!=target:
			curNode=curNode.next
		return curNode is not None
	def add(self,item):
		newNode=_BagListNode(item)
		newNode.next=self._head
		self._head=newNode
		self._size+=1
	def remove(self,item):
		preNode=None
		curNode=self._head
		while curNode is not None and curNode.item!=item:
			preNode=curNode
			curNode=curNode.next
		assert curNode is not None,'the item must be in the bag'
		self._size-=1
		if curNode is self._head:
			self._head=curNode.next
		else:
			preNode.next=curNode.next
		return curNode.item
	def __iter__(self):
		return self
	def next(self):
		curNode=self._head
		if self._curIdx>self._size:
			raise StopIteration
		else:
			tmp=curNode.item
			curNode=curNode.next
			self._curIdx+=1
			return tmp

class _BagListNode:
	def __init__(self,item):
		self.item=item
		self.next=None
