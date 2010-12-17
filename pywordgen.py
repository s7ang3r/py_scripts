#!/usr/bin/python -O
# -*- coding: utf-8 -*-

import optparse
import os


def ParseArgs():
    parser = optparse.OptionParser(usage="%prog [options] ",\
                                 version="%prog 0.3")
    parser.add_option('--numbers',\
                      dest='numb',\
                      help="",\
                      default='')
    parser.add_option('--capitals',\
                      dest='caps',\
                      help="",\
                      default='')
    parser.add_option('--lowercase',\
                      dest='lows',\
                      help="",\
                      default='')
    parser.add_option('--numcaps',\
                      dest='numcaps',\
                      help="",\
                      default='')
    parser.add_option('--numlow',\
                      dest='numlowlows',\
                      help="",\
                      default='')
    parser.add_option('--numcapslow',\
                      dest='numcapslow',\
                      help="",\
                      default='')
    
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