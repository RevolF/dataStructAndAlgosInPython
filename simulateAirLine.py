# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 17:08:36 2017

@author: thor
"""

# implementation of the main simulatio class

from arrayRe import Array
from llistqueue import Queue
from people import TicketAgent,Passneger

class TicketCounterSimulation:
	def __init__(self,numAgents,numMinutes,betweenTime,serviceTime):
		self._arriveProb=1.0/betweenTime
		self._serviceTime=serviceTime
		self._numMinutes=numMinutes
		self._passengerQ=Queue()
		self._theAgents=Array(numAgents)
		for i in range(numAgents):
			self._theAgents[i]=TicketAgent(i+1)
		self._totalWaitTime=0
		self._numPassengers=0
	def run(self):
		for curTime in range(self._numMinutes+1):
			self._handleArriva(curTime)
			self._handleBeginService(curTime)
			self._handleEndServeice(curTime)
	def printResults(self):
		numServed=self._numPassengers-len(self._passengerQ)
		avgWait=float(self._totalWaitTime)/numServed
		print numServed,avgWait
	def _handleArrive(curTime):
		return
	def _handleBeginService(curTime):
		return
	def _handleEndService(curTime):
		return
	
