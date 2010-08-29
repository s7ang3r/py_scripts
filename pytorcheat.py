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

__author__ = "Rodion Brodetsky"
__copyright__ = "Copyright 2010"
__credits__ = ["Rodion Brodetsky"]
__license__ = "GPL"
__version__ = "0.0.2"
__maintainer__ = "Rodion Brodetsky"
__email__ = "s7ang3r@gmail.com"
__status__ = "Production"

def ReadTorrent(filename):
    return bencode.bdecode(open(filename).read())

def GetInfoHash(torrent_info):
    return hashlib.sha1(bencode.bencode(torrent_info)).digest()

def GetFileSize(torrent_info):
    try:
        return torrent_info['length']
    except KeyError:
        return sum(file['length'] for file in torrent_info['files'])

def MakePeerId():
    num_random_chars = 20 - len(PEER_ID_PREFIX)
    alphabet = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(alphabet) for i in range(num_random_chars))
    return PEER_ID_PREFIX + random_string

def MakeAnnounceUrl(torrent_data, peer_id, uploaded):
    base_url = torrent_data['announce']
    scheme, netloc, path, base_query, fragment = urlparse.urlsplit(base_url)
    base_query_list = cgi.parse_qsl(base_query)
    query_list = base_query_list + [
            ('info_hash', GetInfoHash(torrent_data['info'])),
            ('peer_id', peer_id),
            ('port', PORT),
            ('uploaded', uploaded),
            ('downloaded', GetFileSize(torrent_data['info'])),
            ('left', 0),
    ]
    query = urllib.urlencode(query_list)
    return urlparse.urlunsplit((scheme, netloc, path, query, fragment))

def FakeUpload(torrent_data):
    peer_id = MakePeerId()
    uploaded = 0
    while True:
        url = MakeAnnounceUrl(torrent_data, peer_id, uploaded)
        request = urllib2.Request(url, None, {'User-Agent': USER_AGENT})
        response = bencode.bdecode(urllib2.urlopen(request).read())
        if 'failure' in response:
            print 'Announce failed: %s' % response['failure']
            time.sleep(60)
        else:
            interval = response['interval']
            will_sleep_until = (datetime.datetime.now() + datetime.timedelta(seconds=interval)).strftime('%H:%M:%S')
            print 'Uploaded %s bytes, next request at %s.' % (uploaded, will_sleep_until)
            uploaded += UPLOAD_SPEED * interval
            time.sleep(interval)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: %s <filename.torrent>' % sys.argv[0]
        sys.exit(1)
    torrent_data = ReadTorrent(sys.argv[1])
    FakeUpload(torrent_data)
