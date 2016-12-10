# -*- coding: utf-8 -*-
# @Author: karthik
# @Date:   2016-12-10 21:11:06
# @Last Modified by:   karthik
# @Last Modified time: 2016-12-10 22:50:28

class Company(object):

	companies = []
	"""docstring for Company"""
	def __init__(self, name, industry, symbol):
		super(Company).__init__()
		self.name = name
		self.industry = industry
		self.symbol = symbol
		Company.companies.append(self)

	def get_current_price(self):
		return -1
		