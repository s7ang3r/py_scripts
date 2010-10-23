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
#HOST = 'danbooru.donmai.us'
#HOST = 'konachan.com'
#HOST = 'chan.sankakucomplex.com'
#HOST = 'moe.imouto.org'


def ParseArgs():
    parser = optparse.OptionParser(usage="%prog [options] tag ",\
                                 version="%prog 1.0")
    parser.add_option('-e',\
                      '--enginee',\
                      dest="engine",\
                      help="Engine to use",\
                      default='danbooru.donmai.us')
    parser.add_option('-l',\
                      '--limit',\
                      dest='limit',\
                      help='Posts per page limit',\
                      default=1000)
    parser.add_option('-t',\
                      '--threads',\
                      dest='threads',\
                      help='Downloading threads',\
                      default=10)
    parser.add_option('-p',\
                      '--print',\
                      action='store_false',\
                      dest="download_mode",\
                      help="Print content urls",\
                      default=False)
    parser.add_option('-d',\
                      '--download',\
                      action='store_true',\
                      dest="download_mode",\
                      help="Download content",\
                      default=True)
    optparse.IndentedHelpFormatter().set_long_opt_delimiter = 'z'
    (options, args) = parser.parse_args()
    if not args:
        parser.print_help()
        exit(1)
    return (options, args)


def MakeDir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def DownloadContent(url, path):
    image = url.split("/")[-1]
    print "[+] Downloading %s" % image
    urllib.urlretrieve(url, path + image)


def FetchIndex(limit, page, host, tags):
    connection = httplib.HTTPConnection(host)
    args = urllib.urlencode({'tags': tags,\
                             'limit': limit,\
                             'page': page})
    connection.request('GET', '/post/index.xml' + '?' + args)
    response = connection.getresponse()
    if response.status != 200:
        print '[-] Unable to fetch index: HTTP%d' % response.status
        exit(1)
    return response.read()


if __name__ == "__main__":
    (options, tags) = ParseArgs()
    data = FetchIndex(options.limit, 1, options.engine, tags[0])
    try:
        count = int(re.findall('<posts count="([0-9]+)"', data)[0])
    except:
        print "[-] Could not locate number of posts which match this tag."
        exit(1)
    if count > options.limit:
        for page in range(2, count / options.limit + 2):
            data += FetchIndex(options.limit, page, options.engine, tags[0])
    imgs = re.findall('file_url="([^"]+)"', data)
    if not options.download_mode:
        for img in imgs:
            print img
    else:
        print "[!] Found %s images by tag: %s." % (len(imgs), tags[0])
        print "[!] Starting download from: %s." % options.engine
        try:
            dirname = '[' + options.engine + "][" + tags[0] + ']'
        except OSError:
            pass
        MakeDir(dirname)
        for img in imgs:
            thread = threading.Thread(target=DownloadContent,\
                                      args=(img, dirname + '/'))
            if (threading.activeCount() > options.threads):
                time.sleep(0.5)
            else:
                thread.start()