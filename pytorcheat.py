#!/usr/bin/env python
# -*- coding: utf-8 -*-

PORT = 6999
PEER_ID_PREFIX = '-UT1850-'
USER_AGENT = 'uTorrent/1850'
UPLOAD_SPEED = 10000

import bencode
import cgi
import datetime
import hashlib
import random
import string
import sys
import time
import urllib
import urllib2
import urlparse

def ReadTorrent(filename):
    return bencode.bdecode(open(filename).read())

def GetInfoHash(torrent_info):
    return hashlib.sha1(bencode.bencode(torrent_info)).digest()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: %s <filename.torrent>' % sys.argv[0]
        sys.exit(1)
