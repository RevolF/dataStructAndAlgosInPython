# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 09:07:24 2017

@author: thor
"""

# implementation of the priority queue

class PriorityQueue:
	def __init__(self):
		self._qList=list()
	def isEmpty(self):
		return len(self)==0
	def __len__(self):
		return len(self._qList)
	def enqueue(self,item,priority):
		entry=_PriorityQEntry(item,priority)
		self._qList.append(entry)
	def dequeue(self):
		assert not self.isEmpty(), 'can not dequeue from an empty queue'
		for i in range(len(self)):
			if self._qList[i].priority<highest:
				highest=self._qList[i].priority
		entry=self._qList.pop(highest)
		return entry.item

class _PriorityQEntry(self,item,priority):
	def __init__(self,item,priority):
		self.item=item
		self.priority=priority
