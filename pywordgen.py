#!/usr/bin/python -O
# -*- coding: utf-8 -*-

import optparse
import os
import time


def ParseArgs():
    parser = optparse.OptionParser(usage="%prog [options] ",\
                                 version="%prog 0.3")


if __name__ == "__main__":
    numFile = 0
    f=open('wordlist-' + str(numFile) + '.txt', 'w')