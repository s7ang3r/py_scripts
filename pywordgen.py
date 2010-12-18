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
                      default=3)
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
    count = 0
    numfile = 0
    file = open('wordlist-' + str(numfile) + '.txt', 'w')
    minimum = int(options.min)
    maximum = int(options.max)
    genlist = []
    poss = []
    if options.nums:
        poss += nums
    elif options.caps:
        poss += caps
    elif options.lows:
        poss += lows
    elif options.numscaps:
        poss += nums
        poss += caps
    elif options.numslows:
        poss += nums
        poss += lows
    elif options.numcapslows:
        poss += nums
        poss += caps
        poss += lows
    elif options.capslows:
        poss += caps
        poss += lows
    for i in poss:
        genlist.append(str(chr(i)))
    for i in range(minimum,maximum+1):
        for s in Selection(genlist,i):
            count += 1
            file.write(''.join(s) + '\n')
            if count >= 1000:
                size = os.path.getsize('wordlist-' + str(numfile) + '.txt')
                if size > 100 * 1024 * 1024:
                    file.close()
                    numfile += 1
                    file=open('wordlist-' + str(numfile) + '.txt', 'w')
                    count = 0
                    print 'New File. Current word: ', ''.join(s)
    file.close()