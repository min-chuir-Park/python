#!/usr/bin/env python

import numpy as np

'''
diagonal matrix = np.diag(x)

'''

class _diag():
	def  __init__(self):
		self.x =0

	def _diag(self):
		x = np.arange(16).reshape(4,4)#3x3 skill
		print(x)
		print("---------------")
		x = np.diag(x)
		print(x)
		print("---------------")
		x = np.diag(x)
		print(x)
if __name__ =="__main__":
	diag = _diag()
	diag._diag()
	
