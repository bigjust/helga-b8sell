from helga import settings
from helga.plugins import command

from random import randint, random

from helga_mimic import generate_sentence

CARAT_RATIO = getattr(settings, 'B8SELL_CARAT_RATIO', 0.15)
NICK = getattr(settings, 'NICK')


@preprocessor
def b8sell(client, channel, nick, message, carat_ratio=CARAT_RATIO):

    if NICK in message:
        resp = generate_sentence(['b8sell'])
        client.msg(channel, resp)

    if nick == 'aineko' and random() < carat_ratio:
        client.msg(channel, randint(1, 4) * '^')

    return channel, nick, message
