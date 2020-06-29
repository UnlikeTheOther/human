#!#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Mon Jun 29 19:05:00 2020

@author: bvignau
'''

import sys
sys.path.append("..")
from src.human import Human
import unittest
import datetime

class TestHuman(unittest.TestCase):
	# Test 1
	def test_human_is_instance_of_human(self):
		time_start = datetime.datetime.now()
		h = Human("Bill", 24, 184, 72)
		if(self.assertIsInstance(h, Human)):
			print("\nTEST 1 -- KO")
		else:
			print("\nTEST 1 -- OK")
		time_end = datetime.datetime.now()
		print(time_end-time_start)



if __name__ == '__main__':
	unittest.main()

