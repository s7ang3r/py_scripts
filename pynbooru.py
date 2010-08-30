#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import httplib
import re
import urllib
import threading
import time

HOST = 'danbooru.donmai.us'
#HOST='konachan.com'
#HOST='chan.sankakucomplex.com'
URL = '/post/index.xml'
LIMIT = 1000

def Download(url, path):
    os.chdir(path)
    webFile = urllib.urlopen(url)
    localFile = open(url.split('/')[-1], 'wb+')
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
        sys.stderr.write('Could not locate number of posts which match this tag.')
        exit(1)
    if count > LIMIT:
        for page in range(2, count / LIMIT + 2):
            data += FetchIndex(LIMIT, page)
    imgs = re.findall('file_url="([^"]+)"', data)
    print len(imgs)
    for img in imgs:
        print(img)
        thread = threading.Thread(target=Download, args=(img,dirname,))
        if threading.activeCount() >= 10:
            time.sleep(5)
            thread.start()
        else:
            thread.start()