#!/usr/bin/env python

import bisect
'''
if i use bisect 
which is bisect.bisect = bisect.bisect <= 
it means that
standard = 50
inputs = [49 50 51]
bisect.bisect(standard,49) = 0
bisect.bisect(standard,50) = 1
bisect.bisect(standard,50) = 1

'''

class practice :
	def __init__(self):
		self._score = [50]
		self._level = ['Fail','Pass']


	def _bisect(self):
		print("_bisect")
		print(self._level[bisect.bisect(self._score,49) ] )
		print(self._level[bisect.bisect(self._score,50) ] )
		print(self._level[bisect.bisect(self._score,51) ] )
		self._print()

	def _bisect_right(self):
		print("_bisect_right")
		print(self._level[bisect.bisect_right(self._score,49) ] )
		print(self._level[bisect.bisect_right(self._score,50) ] )
		print(self._level[bisect.bisect_right(self._score,51) ] )
		self._print()

	def _bisect_left(self):
		print("_bisect_left")
		print(self._level[bisect.bisect_left(self._score,49) ] )
		print(self._level[bisect.bisect_left(self._score,50) ] )
		print(self._level[bisect.bisect_left(self._score,51) ] )
		self._print()

	def _print(self):
		print("--------------------")

if __name__ == "__main__":
	_practice = practice()
	_practice._bisect()
	_practice._bisect_right()
	_practice._bisect_left()
