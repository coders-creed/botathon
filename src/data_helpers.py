# -*- coding: utf-8 -*-
# @Author: karthik
# @Date:   2016-12-10 23:04:24
# @Last Modified by:   karthik
# @Last Modified time: 2016-12-10 23:12:29

from models/

def get_companies(args):
	companies = []
	for arg in args:
		for comp in Company.companies:
			if arg in comp.name+" "+comp.symbol:
				companies.append(comp)
	return companies
