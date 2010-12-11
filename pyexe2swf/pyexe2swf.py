#!/usr/bin/python -O
# -*- coding: utf-8 -*-

import os
import sys


def SwfPosition(filename):
    filename.seek()
    pass


def ExtractSwf(filein, fileout, position):
    pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print 'Usage: %s file.exe' % sys.argv[0]
        sys.exit(1)
    file = open(sys.argv[1], "rb+")
    position = SwfPosition(file)