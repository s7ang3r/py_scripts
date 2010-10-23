#!/usr/bin/python -O
# -*- coding: utf-8 -*-

import httplib
import os
import re
import sys
import threading
import time
import urllib
import optparse

#HOST = 'e-shuushuu.net'
#HOST = 'gelbooru.com'
#HOST = 'nekobooru.net'
HOST = 'danbooru.donmai.us'
#HOST = 'konachan.com'
#HOST = 'chan.sankakucomplex.com'
#HOST = 'moe.imouto.org'
URL = '/post/index.xml'
LIMIT = 1000


def ParseArgs():
    parser=optparse.OptionParser(usage="%prog [options] tag ", version="%prog 1.0")
    parser.add_option('-e','--enginee',dest="engine",help="Engine to use",default='danbooru.donmai.us')
    parser.add_option('-l','--limit',dest='limit',help='Posts per page limit', default=1000)
    parser.add_option('-p','--print',action='store_false',dest="download_mode",help="Print content urls",default=False)
    parser.add_option('-d','--download',action='store_true',dest="download_mode",help="Download content")
    optparse.IndentedHelpFormatter().set_long_opt_delimiter='z'
    (options, args) = parser.parse_args()
    if not args:
        parser.print_help()
        exit(1)
    print "Options: %s" % options
    print "Args: %s" % args
    return (options, args)    


def MakeDir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def Download(url, path):
    image = url.split("/")[-1]
    print "[+] Downloading %s" % image
    urllib.urlretrieve(url, path + image)


def FetchIndex(limit, page, host):
    connection = httplib.HTTPConnection(HOST)
    args = urllib.urlencode({'tags': sys.argv[1],\
                             'limit': limit,\
                             'page': page})
    connection.request('GET', URL + '?' + args)
    response = connection.getresponse()
    if response.status != 200:
        print '[-] Unable to fetch index: HTTP%d' % response.status
        exit(1)
    return response.read()


if __name__ == "__main__":
    (options, tags)=ParseArgs()
    try:
        dirname = '[' + options.engine + "][" + tags[0] + ']'
    except OSError:
        pass
    MakeDir(dirname)
    data = FetchIndex(LIMIT, 1, options.engine)
    try:
        count = int(re.findall('<posts count="([0-9]+)"', data)[0])
    except:
        print "[-] Could not locate number of posts which match this tag."
        exit(1)
    if count > LIMIT:
        for page in range(2, count / LIMIT + 2):
            data += FetchIndex(LIMIT, page)
    imgs = re.findall('file_url="([^"]+)"', data)
    print "[!] Found %s images by tag: %s." % (len(imgs), tags)
    print "[!] Starting download from: %s." % options.engine
    for img in imgs:
        thread = threading.Thread(target=Download,\
                                  args=(img, dirname + '/'))
        thread.start()
        while threading.activeCount() > 10:
            time.sleep(0.5)
