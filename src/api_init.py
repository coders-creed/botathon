# -*- coding: utf-8 -*-
# @Author: karthik
# @Date:   2016-12-11 08:52:12
# @Last Modified by:   karthik
# @Last Modified time: 2016-12-11 10:17:05

from api.ai import Agent
import json
from data_helpers import *
from models.company import Company
import os

session_id = 313545295
DEVELOPER_ACCESS_TOKEN = "3f4bc676dfb04ecba1d42f3f8a6ffe54"

ai = Agent(
     str(session_id),
     str(session_id),
     DEVELOPER_ACCESS_TOKEN)

def sanitize(string):
	string = string.replace( '(', ' ')
	string = string.replace( ')', ' ')
	return string

def setup_entities():
	create_companies()
	info = {"name": "Companies", "entries": [{"value": company.symbol, "synonyms": [sanitize(company.name)		, company.symbol]} for company in Company.companies]}
	print json.dumps(info)
	response = ai.post(ai.base_url+"/entities", json = info)
	print response

def setup_contexts():
	create_companies()
	info = [{"name": i.symbol, "lifespan": 3} for i in Company.companies]
	call = '''curl -i -X POST \
	   -H "Accept: application/json" \
	   -H "Content-Type: application/json" \
	   -H "Authorization: Bearer 3f4bc676dfb04ecba1d42f3f8a6ffe54" \
	   -d \\ '''+str(info)+''' \
	 https://api.api.ai/v1/contexts?sessionId='''+str(session_id)
	print call
	# response = ai.post(ai.base_url+"/contexts?sessionID="+str(session_id), json = info)
	# print response

# def setup_intents():
# 	 ["info", "buy", "sell"]:



def main():
	# setup_entities()
	setup_contexts()

if __name__ == '__main__':
	main()



