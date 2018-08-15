# encoding=utf-8
import random
import re
import sys
import BotArchitecture
reload(sys)
sys.setdefaultencoding('utf-8')

while True:
    user_input=raw_input();
    bot_reply_type=BotArchitecture.categorize_query(user_input)
    print("Category: "+bot_reply_type)