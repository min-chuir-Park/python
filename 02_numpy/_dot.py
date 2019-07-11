#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
a = [[0 1]
 [2 3]]

different a*a with np.dot(a,a)
'''

import numpy as np

class _dot():
	def __init__(self):
		self.a= np.arange(4).reshape(2,2)

	def _array(self):
		print("a = ")
		print(self.a)

	def _product(self):
		print("a*a = ")
		print(self.a*self.a)

	def _dot_product(self):
		print("np.dot(a,a)")
		print(np.dot(self.a,self.a) )

if __name__ =="__main__":
	dot = _dot()
	dot._array()
	dot._product()
	dot._dot_product()
