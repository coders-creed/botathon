# -*- coding: utf-8 -*-
# @Author: karthik
# @Date:   2016-12-11 08:41:49
# @Last Modified by:   karthik
# @Last Modified time: 2016-12-11 09:02:22

from api.ai import Agent

DEVELOPER_ACCESS_TOKEN = "3f4bc676dfb04ecba1d42f3f8a6ffe54"

ai = agent = Agent(
     '',
     '',
     DEVELOPER_ACCESS_TOKEN,
)

response = agent.query("Hello there")
print response	