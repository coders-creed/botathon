# -*- coding: utf-8 -*-
# @Author: karthik
# @Date:   2016-12-10 21:40:07
# @Last Modified by:   karthik
# @Last Modified time: 2016-12-10 23:05:23

from models.portfolio import Portfolio
from models.company import Company
from models.position import Position
import tenjin
#tenjin.set_template_encoding('cp932')
from tenjin.helpers import *
from data_helpers import *

engine = tenjin.Engine(path=['templates'])

# info fetch handler
def fetch_info_handler(bot, update, args):
	if len(args) == 0 or "portfolio" in [arg.lower() for arg in args] :
		fetch_portfolio_info(bot, update)
	else:
		info_companies = get_companies(args)
		fetch_companies_info(bot, update, info_companies)


# get portfolio function
def fetch_portfolio_info(bot, update):
	print "Userid: %d requested portfolio information" %(update.message.chat_id)
	context = {
	'positions': Portfolio.instance.positions,
    'wallet_value': Portfolio.instance.wallet_value,
	}
	html_str = engine.render('portfolio_info.pyhtml', context)
	bot.sendMessage(parse_mode="HTML", chat_id=update.message.chat_id, text=html_str)

# get companies information
def fetch_companies_info(bot, update, companies):
	print "Userid: %d requested information for following companies %s" %','.join([c.name for c in companies])
	bot.sendMessage(parse_mode="HTML", chat_id=update.message.chat_id, text="hey")
