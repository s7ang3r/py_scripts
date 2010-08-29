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
    return 0

def FetchIndex(limit, page):
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: %s tag" % sys.argv[0]
        exit(1)