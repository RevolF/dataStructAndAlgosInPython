# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:01:01 2017

@author: thor
"""

#==============================================================================
# use __str__ and __repr__ for print class
#==============================================================================

class Bag:
	def __init__(self):
		self._theItems=list()
		
	def __len__(self):
		return len(self._theItems)
		
	def __contains__(self,item):
		return item in self._theItems
		
	def __str__(self):
		return str(self._theItems)
		
	def __repr__(self):
		return str(self)
		
	def add(self,item):
		self._theItems.append(item)
		
	def remove(self,item):
		assert item in self._theItems, 'the item must in the bag'
		ndx=self._theItems.index(item)
		return self._theItems.pop(ndx)
		
	def __iter__(self,item):
		return _BagIterator(self._theItems)
	
class _BagIterator:
	def __init__(self,theList):
		self._bagItems=theList
		self._curItem=0
		
	def __iter__(self):
		return self
		
	def __next__(self):
		if self._curItem<len(self._bagItems):
			item=self._bagItems[self._curItem]
			self._curItem+=1
			return item
		else:
			raise StopIteration
			
def test():
	myBag=Bag()
	myBag.add(1)
	iterator=myBag.__iter__()
	while True:
		try:
			item=iterator.__next__()
			print item
		except StopIteration:
			break



