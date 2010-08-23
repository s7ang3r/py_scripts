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
TZ = 0

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

def Scrobble(filename):
    success = 0
    failure = 0
    timedelay = -3600*TZ
    logfile = open( filename , 'r' )
    print "Scrobbling started."
    for line in logfile.xreadlines():
        data = line.split("\t")
        if (data[5] == "L"):
            params = urllib.urlencode({'s': SESSION_ID,\
                    'a[0]': data[0],\
                    't[0]': data[2],\
                    'i[0]': int(data[6])+timedelay,\
                    'o[0]': 'P',\
                    'r[0]': '',\
                    'l[0]': data[4],\
                    'b[0]': data[1],\
                    'n[0]': data[3],\
                    'm[0]': data[7]})
            conn.request("POST", SUBMISSION_PATH, params, {"Content-type": "application/x-www-form-urlencoded"})
            response = conn.getresponse().read()[:-1]
            if (response == "OK"):
                success+=1
            else:
                failure+=1
            print "%s - %s [%s]" % (data[0], data[2], response)
    conn.close();
    logfile.close()
    print "%i tracks submitted.\n%i failed" % (success, failure)

if __name__ == "__main__":
    #ParseLog(".scrobbler.log")
    #CreateSession()
    Scrobble('.scrobbler.log')
