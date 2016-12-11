# -*- coding: utf-8 -*-
# @Author: karthik
# @Date:   2016-12-10 21:11:06
# @Last Modified by:   chandan
# @Last Modified time: 2016-12-11 12:57:47

class Company(object):
	companies = []
	def __init__(self, name, symbol, industry):
		self.name = name
		self.symbol = symbol
		self.industry = industry
		Company.companies.append(self)

