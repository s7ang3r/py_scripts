#!/usr/bin/python
# -*- coding: utf-8 -*-

import httplib
import os
import re
import sys
import threading
import time
import urllib

HOST = 'danbooru.donmai.us'
#HOST='konachan.com'
#HOST='chan.sankakucomplex.com'
URL = '/post/index.xml'
LIMIT = 1000

def Download(url, path):
    image = url.split("/")[-1]
    print "Downloading %s" % url 
    urllib.urlretrieve(url, path+image,)
    print "Downloading of %s complete" % image

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
    dirname = os.getcwd()
    if len(sys.argv) < 2:
        print "Usage: %s tag" % sys.argv[0]
        exit(1)
    try:
        dirname = os.path.abspath(sys.argv[1])
    except OSError:
        pass
    os.mkdir(dirname)
    data = FetchIndex(LIMIT, 1)
    try:
        count = int(re.findall('<posts count="([0-9]+)"', data)[0])
    except:
        print "Could not locate number of posts which match this tag."
        exit(1)
    if count > LIMIT:
        for page in range(2, count / LIMIT + 2):
            data += FetchIndex(LIMIT, page)
    imgs = re.findall('file_url="([^"]+)"', data)
    print "Found %s images by tag: %s." % (len(imgs), sys.argv[1])
    print "Starting download."
    for img in imgs:
        thread = threading.Thread(target=Download, args=(img, dirname+'/',))
        thread.start()
        while threading.activeCount() > 5:
            time.sleep(0.5)
