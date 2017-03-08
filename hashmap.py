# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 17:25:15 2017

@author: thor
"""

# implementation of hash map

from arrayRe import Array

class HashMap:
	UNUSED=None
	EMPTY=_MapEntry(None,None)
	def __init__(self):
		self._table=Array(7)
		self._count=0
		self._maxCount=len(self._table)-len(self._table)//3
	def __len__(self):
		return self._count
	def __contains__(self,key):
		slot=self._findSlot(key,False)
		return slot is not None
	def add(self,key,value):
		if key in self:
			slot=self._findSlot(key,True)
			self._table[slot].value=value
			














class _MapEntry:
	def __init__(self,key,value):
		self.key=key
		self.value=value


