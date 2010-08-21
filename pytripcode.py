#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string
import re
import crypt

def MakeTripCode (expression):
    expression = expression.decode('utf8','ignore')
    return tripcode

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Program requires arguments."
        sys.exit(0)

    while True:
        if re.search(sys.argv[1],string.lower(MakeTripCode(str(iterator))))>-1:
            print iterator, ":", MakeTripCode(str(iterator))
        elif iterator % 100000 == 0:
            print iterator
        iterator += 1

