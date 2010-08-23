#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
import hashlib
import urllib
import httplib
import urlparse

LOGIN = ''
PASSWORD = ''
APP_NAME = 'qmn' #Register new application!!!
APP_VERSION = '1.2.1'
CHECK_LINE = '#AUDIOSCROBBLER/1.1\n'

def ParseLog(filename):
    try:
        logfile = open( filename , 'r' )
    except IOError:
       print "Cant open file %s" % logfile
       quit()
    if (logfile.readline()!=CHECK_LINE):
        print "Unknown file format."
        logfile.close()
        quit()

def CreateSession():
    timestamp = int(time.time())
    token = hashlib.md5(PASSWORD + str(timestamp)).hexdigest()
    connection = httplib.HTTPConnection("post.audioscrobbler.com") 
    connection.request("GET", "/?hs=true&p=1.2.1&c=%s&v=%s&u=%s&t=%i&a=%s" % (APP_NAME, APP_VERSION, LOGIN, timestamp, token))
    response = connection.getresponse()
    connection.close()

    if (response.status != 200):
        print "Can't connect."
        
        quit()
    data = response.read().split("\n")
    data = [elem for elem in data if len(elem) > 0]
    if (data[0] != "OK"):
        print "Last.fm error: %s" % data[0]
        
        quit()
    url = urlparse(data[3])
    submission_url = url.netloc
    submission_path = url.path
    session_id = data[1]
    return 0;

def Scrobble():
    success = 0
    failure = 0
    

if __name__ == "__main__":
    #ParseLog(".scrobbler.log")
    #CreateSession()
    Scrobble()
