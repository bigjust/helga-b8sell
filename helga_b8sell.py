from helga.plugins import command

@command('b8sell', help='basically b8sell')
def b8sell(client, channel, nick, message, cmd, args):
    return 'Success!'
