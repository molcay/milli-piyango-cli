#!/usr/bin/env python3
"""MilliPiyango CLI

Usage:
  mp games
  mp dates <game>
  mp result <game> <date>
  mp piyango <date> <ticketNo>
"""
from docopt import docopt
from milli_piyango import MilliPiyango as mP


class Arguments:
    def __init__(self, args):
    	self.args = args
    	self.games = args['games']
    	self.dates = args['dates']
    	self.result = args['result']
    	self.piyango = args['piyango']

    	self.game = args['<game>']
    	self.date = args['<date>']
    	self.ticket_no = args['<ticketNo>']


def navigate(args):
    if args.games:
    	print(mP.GAME_LIST)
    elif args.dates:
    	print(mP().get_draw_dates(args.game))
    elif args.result:
    	print(mP().get_result(args.game, args.date))
    elif args.piyango:
    	print(mP().get_result_for_piyango(args.date, args.ticket_no))


if __name__ == '__main__':
    arguments = docopt(__doc__)
    navigate(Arguments(arguments))
