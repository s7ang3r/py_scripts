#!/usr/bin/python -O
# -*- coding: utf-8 -*-

import md5
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


def ScanDir(dir):
    duplicate = {}
    checksums = []
    for root, dirs, files in os.walk(dir):
        files = set(files)
        for file in files:
            if file.startswith('.'):
                continue
            name = os.path.join(root, file)
            md5 = Md5File(name)
            checksums.append(md5)
            if duplicate.get(md5):
                print duplicate[md5]
                print name
                print
            duplicate[md5] = name
    return duplicate, checksums


def PrintResults(checksums, duplicate1, duplicate2=None):
    for sums in checksums:
        if duplicate2 != None:
            print duplicate1[sums]
            print duplicate2[sums]
            print
        else:
            print duplicate1[sums]

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print 'Usage: %s dir1 dir2' % sys.argv[0]
        sys.exit(1)
    directory1 = sys.argv[1]
    directory2 = sys.argv[2]
    print 'Duplicates'
    duplicate1, checksums1 = ScanDir(directory1)
    duplicate2, checksums2 = ScanDir(directory2)
    print 'Commons'
    PrintResults(set(checksums1) & set(checksums2), duplicate1, duplicate2)
    print 'Files only in', directory1
    PrintResults(set(checksums1) - set(checksums2), duplicate1)
    print 'Files only in', directory2
    PrintResults(set(checksums2) - set(checksums1), duplicate2)