import os

from slacker import Slacker


BITMEX_BOT_TOKEN = os.environ['BITMEX_BOT_TOKEN']


bitmex_bot = Slacker(BITMEX_BOT_TOKEN)
bitmex_bot.chat.post_message('#general', 'Test')


