# -*- coding: utf-8 -*-
# @Author: karthik
# @Date:   2016-12-10
# @Last Modified by:   karthik
# @Last Modified time: 2016-12-10 23:18:30


import pandas as pd
import numpy as np
from pandas_datareader.data import DataReader
from datetime import datetime
from models.company import Company

# get price history for list of companies
def get_price_history(companies, start_date, end_date):
	symbols = [c.symbol for c in companies]
	return get_history(symbols,  start_date, end_date)

# get price history for list of tickr symbols
def get_history(symbols,  start_date, end_date):
	interval_length = (end_date - start_date).days
	num_days = 0
	params = ['Open','High','Low','Close','Volume','Adj Close']
	result_dict = {i:None for i in params}

	for symbol in symbols:
		history = get_history_yahoo(symbol, start_date, end_date)
		if len(history) == 0:
			continue

		# keep history only if there are prices for more
		# than half the interval 
		# then create the result data frame
		for param in params:
			history_param = history[param]
			# print history_param
			if len(history) > interval_length/2 and result_dict[param] is None:
				num_days = len(history_param)
				result_dict[param] = pd.DataFrame(columns=symbols, index=range(num_days))

			# discard if data missing
			if result_dict[param] is not None and len(history_param) == num_days:
				result_dict[param][symbol] = history_param.values

	for param in result_dict:
		# remove columns with missing values
		if result_dict[param] is not None:
			result_dict[param] = result_dict[param].dropna(axis=1, how='any')

	return result_dict

# get price for single symbol
def get_history_yahoo(stock_symbol, start_date, end_date):

	print "Searching for: ", stock_symbol, " ... ", 
	history = []
	# try NSE symbol
	try:
		history = DataReader(stock_symbol+'.NS', 'yahoo', start_date, end_date)
	except IOError:
		try:
			history = DataReader(stock_symbol[:-1]+'.NS', 'yahoo', start_date, end_date)	
		except IOError:
			try:
				history = DataReader(stock_symbol, 'yahoo', start_date, end_date)		
			except IOError:
				try:
					history = DataReader(stock_symbol[:-1], 'yahoo', start_date, end_date)
				except IOError:
					history = []

	print len(history), "days"

	return history
