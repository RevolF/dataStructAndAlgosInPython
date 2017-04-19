# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 13:38:38 2017

@author: thor
"""

#==============================================================================
# this is a bizzrd tree, constructed for all directed path tracerse 
# structure looks like:
#	                  0
#		    1	2	3	4
#		 2  3  4  3 4  4
#	    3 4  4     4
#==============================================================================


from operator import attrgetter
from copy import deepcopy

def getAllPath(idxTree):
	pathLst=[]
	
	queue=[deepcopy(idxTree)]
	tmpLst=[]
	while len(queue)>0:
		curNode=queue.pop()
		if curNode.son != []:
			queue.extend(curNode.son)
			tmpLst.append(curNode.rowIdx)
		else:
			candPath=deepcopy(tmpLst)
			candPath.append(curNode.rowIdx)
			pathLst.append(candPath)
			if len(tmpLst)>1 and len(queue)>0:
				while tmpLst[-1] > queue[-1].rowIdx:
					tmpLst.pop()
	return pathLst
	
	
def getIdxTree(depthLen):
	idxLst=sorted(range(depthLen),reverse=True)
	nodeLst=[]
	for i in idxLst:
		if nodeLst == []:
			nodeLst.append(Node(i))
		else:
			sonLst=deepcopy(nodeLst)
#			sonLst=sorted(sonLst,key=lambda x:x.rowIdx)
			sonLst=sorted(sonLst,key=attrgetter('rowIdx'))
			newNode=Node(i,sonLst)
			nodeLst.append(newNode)
	return nodeLst[-1]
	
class Node:
	'''
	use belinked and linked to construct a directed graph
	'''
	def __init__(self,rowIdx,son=[]):
		self.rowIdx=rowIdx
		self.son=son
		
if __name__=='__main__':
	a=getIdxTree(5)
	b=getAllPath(a)
	print b

