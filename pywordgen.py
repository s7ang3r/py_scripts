#!/usr/bin/python -O
# -*- coding: utf-8 -*-

import optparse
import os


def ParseArgs():
    parser = optparse.OptionParser(usage="%prog [options] ",\
                                 version="%prog 0.3")
    parser.add_option('--numbers',\
                      action="store_true",\
                      dest='numbs',\
                      help="Numbers")
    parser.add_option('--capitals',\
                      action="store_true",\
                      dest='caps',\
                      help="Capital Letters")
    parser.add_option('--lowercase',\
                      action="store_true",\
                      dest='lows',\
                      help="Lowercase Letters")
    parser.add_option('--numcaps',\
                      action="store_true",\
                      dest='numcaps',\
                      help="Numbers + Capital Letters")
    parser.add_option('--numlow',\
                      action="store_true",\
                      dest='numlow',\
                      help="Numbers + Lowercase Letters")
    parser.add_option('--numcapslow',\
                      action="store_true",\
                      dest='numcapslow',\
                      help="Numbers + Capital Letters + Lowercase Letters")
    parser.add_option('--capslow',\
                      action="store_true",\
                      dest='capslow',\
                      help="Capital Letters + Lowercase Letters")
    parser.add_option('--min',\
                      dest='min',\
                      help="Minimum size of the word",\
                      default=0)
    parser.add_option('--max',\
                      dest='max',\
                      help="Maximum size of the word",\
                      default=5)
    optparse.IndentedHelpFormatter().set_long_opt_delimiter = 'z'
    (options, args) = parser.parse_args()
    return (options, args)


if __name__ == "__main__":
    (options, tags) = ParseArgs()
    nums = range(48, 58)
    caps = range(65, 91)
    lows = range(97, 123)
    maxsize = 100 * 1024 * 1024
    check = 1000
    count = 0
    numFile = 0
    f = open('wordlist-' + str(numFile) + '.txt', 'w')
    minimum = int(options.min)
    maximum = int(options.max)
    genlist = []
    poss = []
    if options.numbs:
        poss += nums
        print "numb"
    elif options.caps:
        poss += caps
        print "caps"
    elif options.lows:
        poss += lows
        print "lows"
    elif options.numcaps:
        poss += nums
        poss += caps
        print "numscaps"
    elif options.numlow:
        poss += nums
        poss += lows
        print "numslows"
    elif options.numcapslow:
        poss += nums
        poss += caps
        poss += lows
        print "numcapslow"
    elif options.capslow:
        poss += caps
        poss += lows
        print "capslow"
    for i in poss:
        genlist.append(str(chr(i)))