#!/usr/bin/python -O
# -*- coding: utf-8 -*-

import crypt
import re
import string
import sys


def TripCode(expression):
    expression = expression.decode('utf8', 'ignore')\
        .encode('shift_jis', 'ignore')\
        .replace("'", '')\
        .replace(',', ',')\
        .replace('<', '&lt;')\
        .replace('>', '&gt;')\
        .replace('"', '&quot;')
    e_expression = (expression + '...')[1:3]
    e_expression = re.compile('[^\.-z]').sub('.', e_expression)
    e_expression = e_expression.translate(string.maketrans(':;<=>?@[\\]^_`',\
                                                           'ABCDEFGabcdef'))
    tripcode = crypt.crypt(expression, e_expression)[-10:]
    return tripcode


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Program requires arguments.\n"
        sys.exit(0)
    try:
        iterator = int(sys.argv[2])
    except IndexError:
        iterator = 0
    while True:
        if re.search(sys.argv[1], string.lower(TripCode(str(iterator)))) > -1:
            print iterator, ":", TripCode(str(iterator))
        elif iterator % 100000 == 0:
            print iterator
        iterator += 1
