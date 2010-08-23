#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string
import re
import crypt

__author__ = "Rodion Brodetsky"
__copyright__ = "Copyright 2010"
__credits__ = ["Rodion Brodetsky"]
__license__ = "GPL"
__version__ = "0.0.5"
__maintainer__ = "Rodion Brodetsky"
__email__ = "s7ang3r@gmail.com"
__status__ = "Production"

def MakeTripCode (expression):
    expression = expression.decode('utf8','ignore')\
        .encode('shift_jis','ignore')\
        .replace("'",'')\
        .replace(',',',')\
        .replace('<','&lt;')\
        .replace('>','&gt;')\
        .replace('"','&quot;')
    e_expression = (expression + '...')[1:3]
    e_expression = re.compile('[^\.-z]').sub('.', e_expression)
    e_expression = e_expression.translate(string.maketrans(':;<=>?@[\\]^_`', 'ABCDEFGabcdef'))
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
        if re.search(sys.argv[1],string.lower(MakeTripCode(str(iterator))))>-1:
            print iterator, ":", MakeTripCode(str(iterator))
        elif iterator % 100000 == 0:
            print iterator
        iterator += 1

