# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 11:42:55 2017

@author: thor
"""

# implementation of a polynomial ADT

class Polynomial:
	def __init__(self,degree=None,coefficient=None):
		if degree is None:
			self._polyHead=None
		else:
			self._polyHead=_PolyTermNode(degree,coefficient)
		self._polyTail=self._polyHead
	def degree(self):
		if self._polyHead is None:
			return -1
		else:
			return self._polyHead.degree
	def __getitem__(self,degree):
		assert self.degree() >=0,'operation not permitted on an empty polynomial'
		curNode=self._polyHead
		while curNode is not None and curNode.degree != degree:
			curNode=curNode.next
		if curNode is None or curNode.degree != degree:
			return 0.0
		else:
			return curNode.degree
	def evaluate(self,scalar):
		assert self.degree() >= 0,'only non-empty polynomials can be evaluated'
		result=0.0
		curNode=self._polyHead
		while curNode is not None:
			result+=curNode.coefficient*(scalar**curNode.degree)
			curNode=curNode.next
		return result
	def __add__(self,rhsPoly):
		assert self.degree()>=0 and rhsPoly.degree()>=0,'addition only allowed on non-empty polynomials'
		newPoly=Polynomial()
		nodeA=self._termList
		nodeB=rhsPoly._termList
		while nodeA is not None and nodeB is not None:
			if nodeA.degree>nodeB.degree:
				degree=nodeA.degree
				value=nodeA.coefficient
				nodeA=nodeA.next
			elif nodeA.degree<nodeB.degree:
				degree=nodeB.degree
				value=nodeB.coefficient
				nodeB=nodeB.next
			else:
				degree=nodeA.degree
				value=nodeA.coefficient+nodeB.coefficient
				nodeA=nodeA.next
				nodeB=nodeB.next
			self._appendTerm(degree,value)
		while nodeA is not None:
			self._appendTerm(nodeA.degree,nodeA.coefficient)
			nodeA=nodeA.next
		while nodeB is not None:
			self._appendTerm(nodeB.degree,nodeB.coefficient)
			nodeB=nodeB.next
		return newPoly
	def __sub__(self,rhsPoly):
		pass
	def __mul__(self,rhsPoly):
		pass
	def _appendTerm(self,degree,coefficient):
		if coefficient!=0.0:
			newTerm=_PolyTermNode(degree,coefficient)
			if self._polyHead is None:
				self._polyHead=newTerm
			else:
				self._polyTail.next=newTerm
			self._polyTail=newTerm
			
class _PolyTermNode(object):
	def __init__(self,degree,coefficient):
		self.degree=degree
		self.coefficient=coefficient
		self.next=None




























