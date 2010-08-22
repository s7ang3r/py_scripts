#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os.path
import hashlib
import urllib
import httplib
import urlparse

CHECK_LINE = "#AUDIOSCROBBLER/1.1\n"

def ParseLog(filename):
    try:
        logfile = open(filename,'r')
    except IOError:
       print "Cant open file %s" % logfile
       quit()
    if (logfile.readline()!=CHECK_LINE):
        print "Unknown file format"
        logfile.close()
        quit()
    return 0

def CreateSession():
    return 0;

def Scrobble():
    return 0;

if __name__ == "__main__":
    #ParseLog(".scrobbler.log")
    CreateSession()
    Scrobble()
