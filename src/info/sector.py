# -*- coding: utf-8 -*-
# @Author: chandan
# @Date:   2016-12-11 12:55:08
# @Last Modified by:   chandan
# @Last Modified time: 2016-12-11 13:52:12

from models.company import Company
import wikipedia
import random

def sector_main(bot, update, args):
	print "Getting sector info"

	display_names = [" ".join(map(lambda x: x.capitalize(), c.industry.split())) for c in Company.companies]
	sectors = set(display_names)

	if len(args) == 0:

		sector_text = """You can trade in these sectors: {}.
			\tInterested in a sector? Ask me using /sector <sector>
					""".format(", ".join(sectors)
			)
		bot.sendMessage(chat_id=update.message.chat_id, text=sector_text)
	else:
		for sector in args:
			for name in display_names:
				if sector in name:
					sector_summary = wikipedia.summary(name+'industry', sentences=2)

					sector_companies = []
					limit = 10

					for company in Company.companies:
						if sector in company.industry.lower():
							sector_companies.append(Company)

					companies_text = """
						Here are some companies in these sector:
						\t{} 
					""".format(' ').join(
						random.sample([c.name for c in top_companies], limit)
						)

					text = """
						{}
						{}
					""".format(sector_summary, companies_text)

					bot.sendMessage(chat_id=update.message.chat_id, text=text)
					break			


