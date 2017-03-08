# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:27:34 2017

@author: thor
"""

# implementation of map ADT using a single list

class Map:
	def __init__(self):
		self._entryList=list()
		self._curIdx=0
	def __len__(self):
		return len(self._entryList)
	def __contains__(self,key):
		ndx=self._findPosition(key)
		return ndx is not None
	def add(self,key,value):
		ndx=self._findPosition(key)
		if ndx is not None:
			self._entryList[ndx].value=value
			return False
		else:
			entry=_MapEntry(key,value)
			self._entryList.append(entry)
			return True
	def valueOf(self,key):
		ndx=self._findPosition(key)
		assert ndx is not None,'Invalid map key'
		return self._entryList[ndx].value
	def remove(self,key):
		ndx=self._findPosition(key)
		assert ndx is not None,'Invalid map key'
		self._entryList.pop(ndx)
	def __iter__(self):
		return self
	def _findPosition(self,key):
		for i in range(len(self)):
			if self._entryList[i].key==key:
				return i
		return None
	def next(self):
		if self._curIdx>=len(self):
			raise StopIteration
		else:
			self._curIdx+=1
			return self._entryList[self._curIdx-1].key,self._entryList[self._curIdx-1].value
class _MapEntry:
	def __init__(self,key,value):
		self.key=key
		self.value=value




























