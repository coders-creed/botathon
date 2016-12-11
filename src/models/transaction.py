# -*- coding: utf-8 -*-
# @Author: chandan
# @Date:   2016-12-11 12:49:53
# @Last Modified by:   chandan
# @Last Modified time: 2016-12-11 12:51:58

import datetime

class Transaction(object):
	"""docstring for Transaction"""
	def __init__(self, company, n_units, price):
		super(Transaction, self).__init__()
		self.company = company
		self.price = price
		self.n_units = n_units
		self.buying_time = datetime.datetime.now()
		