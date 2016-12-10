# -*- coding: utf-8 -*-
# @Author: karthik
# @Date:   2016-12-10 21:06:13
# @Last Modified by:   karthik
# @Last Modified time: 2016-12-10 21:10:49

class Position(object):
	"""docstring for Position"""
	def __init__(self, company, num_shares, buying_price ):
		super(Position, self).__init__()
		# set values
		self.company = company
		self.num_shares =  num_shares
		self.buying_price = buying_price
		
	def get_value(self):
		return self.num_shares*self.buying_price