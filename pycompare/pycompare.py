#!/usr/bin/python -O
# -*- coding: utf-8 -*-

import hashlib
import os
import sys


def Md5File(filename):
    fh = open(filename)
    digest = md5.new()
    while 1:
        buf = fh.read(4096)
        if buf == "":
            break
        digest.update(buf)
    fh.close()
    return digest.hexdigest()
