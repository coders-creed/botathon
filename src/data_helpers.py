# -*- coding: utf-8 -*-
# @Author: karthik
# @Date:   2016-12-10 23:04:24
# @Last Modified by:   karthik
# @Last Modified time: 2016-12-11 07:11:13

from models.company import Company
import pandas as pd

FILENAME = "resources/cnx500.csv"

# arg parser
def parse_args(args):
	arg_string = ' '.join(args)
	return set(filter(lambda x: x != "", map(lambda x: x.strip().lower(), arg_string.split(','))))

# get symbol, company name and industry
def get_cnx_symbols(filename):
	csv_content =  pd.read_csv(filename)
	# Using the CNX List - get only symbol and company name
	cnx = csv_content.loc[:, ("Company Name", "Symbol", "Industry")]

	return cnx


def get_companies(args):
	companies = []
	for arg in args:
		for comp in Company.companies:
			if arg in comp.name.lower()+" "+comp.symbol.lower():
				companies.append(comp)
	return companies

def create_companies():
	cnx = get_cnx_symbols(FILENAME)
	for record in cnx.to_records(index = False):
		Company(*record)
