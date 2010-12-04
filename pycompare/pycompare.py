#!/usr/bin/python -O
# -*- coding: utf-8 -*-

import hashlib
import os
import sys


def Md5File(filename):
    fh = open(filename)
    digest = hashlib.md5.new()
    while 1:
        buf = fh.read(4096)
        if buf == "":
            break
        digest.update(buf)
    fh.close()
    return digest.hexdigest()


def ScanDir(dir):
    duplicate = {}
    checksums = []
    for root, dirs, files in os.walk(dir):
        files = set(files) - set(IGNORE_FILES)
        for file in files:
            if IGNORE_HIDDEN and file.startswith('.'):
                continue
            name = os.path.join(root, file)
            md5 = md5file(name)
            checksums.append(md5)
            if duplicate.get(md5):
                print duplicate[md5]
                print name
                print
            duplicate[md5] = name
    return duplicate, checksums


def PrintResults():
    pass

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print 'Usage: %s dir1 dir2' % sys.argv[0]
        sys.exit(1)
    directory1 = sys.argv[1]
    directory2 = sys.argv[2]