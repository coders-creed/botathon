# -*- coding: utf-8 -*-
# @Author: chandan
# @Date:   2016-12-11 08:41:51
# @Last Modified by:   chandan
# @Last Modified time: 2016-12-11 12:59:47

from data_helpers import get_company
from stock_data import get_current_price

from models.portfolio import Portfolio
from models.position import Position
from models.transaction import Transaction

from telegram.inlinekeyboardbutton import InlineKeyboardButton
from telegram.inlinekeyboardmarkup import InlineKeyboardMarkup

TRANSACTIONS = []

buy_context = {
	'company': None,
	'n_shares': None,
	'bot': None,
	'update': None,
	'current_price': None
}

# buy shares
def buy_shares(bot, update, args):
	company = get_company(args[0])
	n_shares_to_buy = int(args[1])

	buy_context['company'] = company
	buy_context['n_shares'] = n_shares_to_buy
	buy_context['bot'] = bot
	buy_context['update'] = update

	print "Buying {} shares of {}".format(n_shares_to_buy, company.symbol)

	portfolio = Portfolio.instance 
	current_price = get_current_price(company)
	buy_context['current_price'] = current_price
	buy_value = current_price * n_shares_to_buy

	todays_price_text = 'The current price for {} is {}'.format(company.symbol, current_price)
	bot.sendMessage(chat_id=update.message.chat_id, text=todays_price_text)

	# check if wallet balace sufficient
	if buy_value >= portfolio.wallet_value:
		bot.sendMessage(chat_id=update.message.chat_id, text='Your wallet balance is insufficient to make this trade. Please add more money to it')
		return

	confirm_text = "Are you sure you want to buy {} shares of {} at {} per share, for a total value of {}?".format(n_shares_to_buy, company.symbol, current_price, buy_value)
	# send yes/no confirmation button
	buttons = [[
					InlineKeyboardButton(text="Yes", callback_data='BUY-Y'),
					InlineKeyboardButton(text="No", callback_data='BUY-N')
			]]
	keyboard = InlineKeyboardMarkup(buttons)
	bot.sendMessage(chat_id=update.message.chat_id, text=confirm_text, reply_markup=keyboard)

# finish the buying process after confirmation
def complete_buy():
	company = buy_context['company']
	n_shares_to_buy = buy_context['n_shares']
	bot = buy_context['bot']
	update = buy_context['update']
	current_price = buy_context['current_price']

	buy_value = current_price * n_shares_to_buy
	portfolio = Portfolio.instance 

	# check if position exists
	for position in portfolio.positions:
		if position.company.symbol == company.symbol:
			updated_shares = position.num_shares + n_shares_to_buy

			text = '''Your position with {} has been updated from {} to {} shares.
			'''.format(company.symbol, position.num_shares, updated_shares)
			bot.sendMessage(chat_id=update.message.chat_id, text=text)

			# update position
			position.num_shares = updated_shares
			position_updated = True

	if not position_updated:
		portfolio.add_position(Position(company, n_shares_to_buy, current_price))
		
		text = 'Your new position with {} is {} shares.'.format(company.symbol, n_shares_to_buy)
		bot.sendMessage(chat_id=update.message.chat_id, text=text)

	portfolio.wallet_value -= buy_value
	wallet_text = 'Your updated wallet balance is {}'.format(portfolio.wallet_value)
	bot.sendMessage(chat_id=update.message.chat_id, text=wallet_text)

	TRANSACTIONS.append(
		Transaction(company, n_shares_to_buy, current_price)
		)
