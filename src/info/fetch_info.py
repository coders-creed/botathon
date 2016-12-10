# -*- coding: utf-8 -*-
# @Author: karthik
# @Date:   2016-12-10 21:40:07
# @Last Modified by:   karthik
# @Last Modified time: 2016-12-11 00:29:09

from models.portfolio import Portfolio
from models.company import Company
from models.position import Position
import tenjin
#tenjin.set_template_encoding('cp932')
from tenjin.helpers import *
from data_helpers import *

import plotly.plotly as py
import plotly.graph_objs as go
import datetime.date as dt

data = [go.Scatter(
          x=['2013-10-04 22:23:00', '2013-11-04 22:23:00', '2013-12-04 22:23:00'],
          y=[1, 3, 6])]
py.iplot(data)

engine = tenjin.Engine(path=['templates'])

# info fetch handler
def send_info_handler(bot, update, args):
	args = list(parse_args(args))
	if len(args) == 0 or "portfolio" in [arg.lower() for arg in args] :
		send_portfolio_info(bot, update)
	else:
		info_companies = get_companies(args)
		send_companies_info(bot, update, info_companies)


# get portfolio function
def send_portfolio_info(bot, update):
	print "Userid: %d requested portfolio information" %(update.message.chat_id)
	context = {
	'positions': Portfolio.instance.positions,
    'wallet_value': Portfolio.instance.wallet_value,
	}
	html_str = engine.render('portfolio_info.pyhtml', context)
	bot.sendMessage(parse_mode="HTML", chat_id=update.message.chat_id, text=html_str)

# get companies information
def send_companies_info(bot, update, companies):
	print "Userid: requested information for following companies %s" %','.join([c.name for c in companies])
	for company in companies:
		context = {
		'company': company,
		}
		html_str = engine.render('company_template.pyhtml', context)
	if len(companies) < 4:
		create_graph(companies, 40)
		bot.(parse_mode="HTML", chat_id=update.message.chat_id, text="hey")

# create graph