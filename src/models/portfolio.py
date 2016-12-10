# -*- coding: utf-8 -*-
# @Author: karthik
# @Date:   2016-12-10 21:01:05
# @Last Modified by:   karthik
# @Last Modified time: 2016-12-10 22:30:57

from position import Position

class Portfolio(object):
	"""Portfolio class"""
	instance = None
	def __init__(self, list_of_positions, wallet_value):
		if Portfolio.instance == None:
			super(Portfolio, self).__init__()
			self.positions = list_of_positions
			self.value = sum(self.positions)
			self.wallet_value = wallet_value
			Portfolio.instance = self
		else:
			raise("Portfolio already exists")

	def add_position(self, new_pos):
		self.positions.append(new_pos)

	def get_total_value(self):
		return sum([pos.get_value() for pos in self.positions])



