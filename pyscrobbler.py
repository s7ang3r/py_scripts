#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
import hashlib
import urllib
import httplib
import urlparse

LOGIN = "login"
PASSWORD = "password"
CHECK_LINE = "#AUDIOSCROBBLER/1.1\n"

def ParseLog(filename):
    try:
        logfile = open( filename , 'r' )
    except IOError:
       print "Cant open file %s" % logfile
       quit()
    if (logfile.readline()!=CHECK_LINE):
        print "Unknown file format"
        logfile.close()
        quit()

def CreateSession():
    timestamp = int(time.time())
    token = hashlib.md5(PASSWORD + str(timestamp)).hexdigest()
    connection = httplib.HTTPConnection("post.audioscrobbler.com") 
    return 0;

def Scrobble():
    return 0;

if __name__ == "__main__":
    ParseLog(".scrobbler.log")
    CreateSession()
    Scrobble()
