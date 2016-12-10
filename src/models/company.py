# -*- coding: utf-8 -*-
# @Author: karthik
# @Date:   2016-12-10 21:11:06
# @Last Modified by:   karthik
# @Last Modified time: 2016-12-10 23:47:32

class Company(object):

	companies = []
	"""docstring for Company"""
	def __init__(self, name, symbol, industry):
		self.name = name
		self.symbol = symbol
		self.industry = industry
		Company.companies.append(self)

	def get_current_price(self):
		return -1
		