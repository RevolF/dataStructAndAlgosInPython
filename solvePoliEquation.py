# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 08:28:36 2017

@author: thor
"""

# implementation of using dict to solve a polynominal equation:
# a1x1^3+a2x2^3+...+a5x5^3=0, which -50<=x1,...,x5<50

class solvePoliEq:
	def __init__(self,a1,a2,a3,a4,a5):
		self._a1=a1
		self._a2=a2
		self._a3=a3
		self._a4=a4
		self._a5=a5
		self._resDct={}
		self._resLst=[]
	def leftRes(self):
		for i in range(-50,50):
			for j in range(-50,50):
				for k in range(-50,50):
					leftVal=self._a1*i^3+self._a2*j^3+self._a3*k^3
					if self._resDct.has_key(leftVal):
						self._resDct[leftVal].append([i,j,k])
					else:
						self._resDct[leftVal]=[i,j,k]
	def printRes(self):
		for i in range(-50,50):
			for j in range(-50,50):
				rightVal=self._a4*i^3+self._a5*j^3
				if self._resDct.has_key(-rightVal):
					self._resLst.append([[i,j],self._resDct[-rightVal]])
		for item in self._resLst:
			for subItem in item[1]:
				print item[0],subItem
		
if __name__=='__main__':
	myPoly=solvePoliEq(11,2,13,21,3)
	myPoly.leftRes()
	myPoly.printRes()







