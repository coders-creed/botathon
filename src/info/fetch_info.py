# -*- coding: utf-8 -*-
# @Author: karthik
# @Date:   2016-12-10 21:40:07
# @Last Modified by:   chandan
# @Last Modified time: 2016-12-11 12:55:27

from models.portfolio import Portfolio
from models.company import Company
from models.position import Position

import tenjin
from tenjin.helpers import *
import wikipedia

import matplotlib.pyplot as plt

from data_helpers import *
from stock_data import *

import BeautifulSoup as bs
import urllib2
import re

from datetime import date as dt

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
		'current_price': get_current_price(company),
		'description': wikipedia.summary(company.name.split()[0], sentences=2)
		}

		wiki_page = wikipedia.page(company.name.split()[0])
		html_page = urllib2.urlopen(wiki_page.url)
		soup = bs.BeautifulSoup(html_page)
		img_url = 'http:' + soup.find('td', { "class" : "logo" }).find('img')['src']
		bot.sendPhoto(chat_id=update.message.chat_id, photo=img_url)

		html_str = engine.render('company_template.pyhtml', context)
		bot.sendMessage(parse_mode="HTML", chat_id=update.message.chat_id, text=html_str)

	symbols = [c.symbol for c in companies]
	if len(symbols) >= 2:
		symbol_string = ", ".join(symbols[:-1]) + " and " + symbols[-1]
	else:
		symbol_string = symbols[0]

	last_n_days = 10

	if len(companies) < 4:
		create_graph(companies, last_n_days)
		history_text = '''
			Here's the price history for {} for the last {} days
		'''.format(symbol_string, last_n_days)

		bot.sendMessage(chat_id=update.message.chat_id, text=history_text)
		bot.sendPhoto(chat_id=update.message.chat_id, photo=open("plots/temp.png",'rb'))

def create_graph(companies, timedel):

	fig, ax = plt.subplots()
	for company in companies:
		dates, lookback_prices = get_lookback_prices(company, timedel)
		# dates = [i.strftime('%d/%m') for i in dates]
		h = ax.plot(dates, lookback_prices, label=company.symbol)

	ax.legend()
	plt.xticks(rotation=45)
	plt.savefig('plots/temp.png')

