#!/usr/bin/python -O
# -*- coding: utf-8 -*-

import optparse
import os


def ParseArgs():
    parser = optparse.OptionParser(usage="%prog [options] ",\
                                 version="%prog 0.3")
    parser.add_option('--numbers',\
                      dest='numb',\
                      help="Numbers")
    parser.add_option('--capitals',\
                      dest='caps',\
                      help="Capital Letters")
    parser.add_option('--lowercase',\
                      dest='lows',\
                      help="Lowercase Letters")
    parser.add_option('--numcaps',\
                      dest='numcaps',\
                      help="Numbers + Capital Letters")
    parser.add_option('--numlow',\
                      dest='numlowlows',\
                      help="Numbers + Lowercase Letters")
    parser.add_option('--numcapslow',\
                      dest='numcapslow',\
                      help="Numbers + Capital Letters + Lowercase Letters")
    parser.add_option('--capslow',\
                      dest='capslow',\
                      help="Capital Letters + Lowercase Letters")
    parser.add_option('--min',\
                      dest='min',\
                      help="Minimum size of the word")
    parser.add_option('--max',\
                      dest='max',\
                      help="Maximum size of the word")
    
    optparse.IndentedHelpFormatter().set_long_opt_delimiter = 'z'
    (options, args) = parser.parse_args()
    if not args:
        parser.print_help()
        exit(1)
    return (options, args)


if __name__ == "__main__":
    (options, tags) = ParseArgs()
    nums = range(48,58)
    caps = range(65,91)
    lows = range(97,123)
    numFile = 0
    f=open('wordlist-' + str(numFile) + '.txt', 'w')