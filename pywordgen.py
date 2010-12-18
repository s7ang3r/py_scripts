#!/usr/bin/python -O
# -*- coding: utf-8 -*-

import optparse
import os


def ParseArgs():
    parser = optparse.OptionParser(usage="%prog [options] ",\
                                 version="%prog 0.3")
    parser.add_option('--numbers',\
                      action="store_true",\
                      dest='nums',\
                      help="Numbers")
    parser.add_option('--capitals',\
                      action="store_true",\
                      dest='caps',\
                      help="Capital Letters")
    parser.add_option('--lowercase',\
                      action="store_true",\
                      dest='lows',\
                      help="Lowercase Letters")
    parser.add_option('--numscaps',\
                      action="store_true",\
                      dest='numscaps',\
                      help="Numbers + Capital Letters")
    parser.add_option('--numslows',\
                      action="store_true",\
                      dest='numslows',\
                      help="Numbers + Lowercase Letters")
    parser.add_option('--numcapslows',\
                      action="store_true",\
                      dest='numcapslows',\
                      help="Numbers + Capital Letters + Lowercase Letters")
    parser.add_option('--capslows',\
                      action="store_true",\
                      dest='capslows',\
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


def Selection(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for x in Selection(items, n-1):
                yield [items[i]]+x


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
    if options.nums:
        poss += nums
        print "nums"
    elif options.caps:
        poss += caps
        print "caps"
    elif options.lows:
        poss += lows
        print "lows"
    elif options.numscaps:
        poss += nums
        poss += caps
        print "numscaps"
    elif options.numslows:
        poss += nums
        poss += lows
        print "numslows"
    elif options.numcapslows:
        poss += nums
        poss += caps
        poss += lows
        print "numcapslows"
    elif options.capslows:
        poss += caps
        poss += lows
        print "capslows"
    for i in poss:
        genlist.append(str(chr(i)))