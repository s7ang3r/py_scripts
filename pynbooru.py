#!/usr/bin/python
# -*- coding: utf-8 -*-

import httplib
import re
import sys
import urllib

HOST = 'danbooru.donmai.us'
URL = '/post/index.xml'
LIMIT = 1000

def Download(url):
    webFile = urllib.urlopen(url)
    localFile = open(url.split('/')[-1], 'w')
    localFile.write(webFile.read())
    webFile.close()
    localFile.close()

def FetchIndex(limit, page):
    connection = httplib.HTTPConnection(HOST)
    args = urllib.urlencode({'tags': sys.argv[1], 'limit': limit, 'page': page})
    connection.request('GET', URL + '?' + args)
    response = connection.getresponse()
    if response.status != 200:
        print 'Unable to fetch index: HTTP%d' % response.status
        exit(1)
    return response.read()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: %s tag" % sys.argv[0]
        exit(1)