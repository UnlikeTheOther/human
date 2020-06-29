#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on Mon Jun 29 14:53:00 2020

@author: bvignau
'''

class Human :
	'''
		Human class contains name, age, size and weight parameters
	'''
	def __init__(self, name, age, size, weight):
		# Assert methods
		assert name.isalnum(), "Attribut 'name' : doit être alphanumérique"

		# Instance variable
		self.name = name
		self.age = age
		self.size = size
		self.weight = weight
		self.hunger = 50

	def __str__(self):
		'''
			Display the content of the Human object.
		'''
		return("Name: {0}, \nAge; {1} years-old, \nSize; {2} cm, \n Weight: {3} cm, \n".format(self.name, self.age, self.size, self.weight))
		#return ("Name: {self.name}, \nAge: {self.age} years-old, \nSize: {self.size} cm, \nWeight: {self.weight} kg, \n Hungry: {self.hunger}/100 \n")

	def eat(self, food_point):
		'''
		Parameters
		----------
		food_point : int
			Add the food_point value to self.hunger, while it doesn't equal to 100.
			Display a message when it worths 100
		Returns
		-------
		None.
		'''
		assert isinstance(food_point, int), "Attribut 'food_point' : doit être un entier (instance de 'int')"
		if self.hunger >= 100:
			print("{self.name} has already eat as well (hunger: {self.hunger})")
		else:
			self.hunger += food_point
			if self.hunger > 100:
				print("That is a fabulous meal!")
				self.hunger = 100
			print("{0} has eat (hunger: {1})".format(self.name, self.hunger))
