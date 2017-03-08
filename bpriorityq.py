# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 16:42:18 2017

@author: thor
"""

# implementation of the bounded Priority Queue ADT using a array of queues in which the queues are implemented using a
# linked list

from arrayRe import Array
from llistqueue import Queue

class BPriorityQueue:
	def __init__(self,numLevels):
		self._qSize=0
		self._qLevels=Array(numLevels)
		for i in range(numLevels):
			self._qLevels[i]=Queue()
	def isEmpty(self):
		return len(self)==0
	def __len__(self):
		return len(self._qSize)
	def enqueue(self,item,priority):
		assert priority>=0 and priority<len(self._qLevels), \
			'invalid proority level'
		self._qLevels[priority].enqueue(item)
	def dequeue(self):
		assert not self.isEmpty(),'cannot dequeue from an empty queue'
		i=0
		p=len(self._qLevels)
		while i<p and self._qLevels[i].isEmpty():
			i+=1
		return self._qLevels[i].dequeue()





