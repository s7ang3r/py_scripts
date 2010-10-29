#!/usr/bin/python -O
# -*- coding: utf-8 -*-

import optparse
import os
import re
import threading
import urllib


def ParseArgs():
    parser = optparse.OptionParser(usage="%prog [options] tag ",\
                                 version="%prog 1.0")
    parser.add_option('-s',\
                      '--site',\
                      dest='site',\
                      help="Site to use",\
                      default='danbooru.donmai.us')
    parser.add_option('-l',\
                      '--limit',\
                      dest='limit',\
                      help="Posts per page limit",\
                      default=1000)
    parser.add_option('-t',\
                      '--threads',\
                      dest='threads',\
                      help="Downloading threads",\
                      default=5)
    parser.add_option('-p',\
                      '--print',\
                      action='store_false',\
                      dest='download_mode',\
                      help="Print content urls",\
                      default=False)
    parser.add_option('-d',\
                      '--download',\
                      action='store_true',\
                      dest='download_mode',\
                      help="Download content",\
                      default=True)
    optparse.IndentedHelpFormatter().set_long_opt_delimiter = 'z'
    (options, args) = parser.parse_args()
    if not args:
        parser.print_help()
        exit(1)
    return (options, args)


def GenQuery(url, page, params):
    str = '?' + '&'.join('%s=%s' % (par, value)\
                         for par, value in params.iteritems())
    return urllib.urlopen(url + page + str)


def MakeDir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
        print "[!] Directory %s successfully created." % dir
    else:
        print "[!] Directory %s already exists." % dir


def DownloadContent(url, path):
    queue.acquire()
    image = url.split("/")[-1]
    print "[+] Downloading %s" % image
    urllib.urlretrieve(url, path + image)
    queue.release()


def FetchIndex(limit, page, host, tags):
    if host != "http://":
        host = "http://" + host
    connection = GenQuery(host, "/post/index.xml", {'tags': tags,\
                                                    'limit': limit,\
                                                    'page': page})
                                                    #'order': 'count'})
    #connection = GenQuery(host, "/index.php", {'page': 'dapi',\
    #                                               's': 'post',\
    #                                               'q': 'index',\
    #                                               'tags': tags,\
    #                                               'limit': limit,\
    #                                               'pid': page})
    return connection.read()


if __name__ == "__main__":
    (options, tags) = ParseArgs()
    queue = threading.BoundedSemaphore(options.threads)
    data = FetchIndex(options.limit, 1, options.site, tags[0])
    try:
        count = int(re.findall('<posts count="([0-9]+)"', data)[0])
    except:
        print "[-] Could not locate number of posts which match this tag."
        exit(1)
    if count > options.limit:
        for page in range(2, count / options.limit + 2):
            data += FetchIndex(options.limit, page, options.site, tags[0])
    imgs = re.findall('file_url="([^"]+)"', data)
    if not options.download_mode:
        for img in imgs:
            print img
    else:
        print "[!] Found %s images by tag: %s." % (len(imgs), tags[0])
        print "[!] Starting download from: %s." % options.site
        try:
            dirname = '[' + options.site + "][" + tags[0] + ']'
        except OSError:
            pass
        MakeDir(dirname)
        for img in imgs:
            thread = threading.Thread(target=DownloadContent,\
                                      args=(img, dirname + '/'))
            thread.start()
