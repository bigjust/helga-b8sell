from helga import settings
from helga.plugins import command

from random import randint, random

CARAT_RATIO = getattr(settings, 'B8SELL_CARAT_RATIO', 0.15)

@command('b8sell', help='basically b8sell')
def b8sell(client, channel, nick, message, cmd, args, carat_ratio=CARAT_RATIO):

    if nick == 'aineko' and random() < carat_ratio:
        return randint(1, 4) * '^'
