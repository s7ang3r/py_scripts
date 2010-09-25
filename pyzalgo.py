#!/usr/bin/python -O
# -*- coding: utf-8 -*-

import sys
import random
import itertools

zalgo_up = [u'\u030d', u'\u030e', u'\u0304', u'\u0305', u'\u033f', u'\u0311',
            u'\u0306', u'\u0310', u'\u0352', u'\u0357', u'\u0351', u'\u0307',
            u'\u0308', u'\u030a', u'\u0342', u'\u0343', u'\u0344', u'\u034a',
            u'\u034b', u'\u034c', u'\u0303', u'\u0302', u'\u030c', u'\u0300',
            u'\u0301', u'\u030b', u'\u030f', u'\u0312', u'\u0313', u'\u0314',
            u'\u033d', u'\u0309', u'\u033e', u'\u0346', u'\u031a']
zalgo_mid = [u'\u0315', u'\u031b', u'\u0340', u'\u0341', u'\u0358', u'\u0321',
             u'\u0322', u'\u0327', u'\u0328', u'\u0334', u'\u0335', u'\u0336',
             u'\u034f', u'\u035c', u'\u035d', u'\u035e', u'\u035f', u'\u0360',
             u'\u0362', u'\u0338', u'\u0337', u'\u0361', u'\u0489']
zalgo_down = [u'\u0316', u'\u0317', u'\u0318', u'\u0319', u'\u031c', u'\u031d',
              u'\u031e', u'\u031f', u'\u0320', u'\u0324', u'\u0325', u'\u0326',
              u'\u0329', u'\u032a', u'\u032b', u'\u032c', u'\u032d', u'\u032e',
              u'\u032f', u'\u0330', u'\u0331', u'\u0332', u'\u0333', u'\u0339',
              u'\u033a', u'\u033b', u'\u033c', u'\u0345', u'\u0347', u'\u0348',
              u'\u0349', u'\u034d', u'\u034e', u'\u0353', u'\u0323']


def Merge(lst, output=[]):
    for el in lst:
        Merge(el) if isinstance(el, list) else output.append(el)
    return output


def ZalgoChars(text, high=True, mid=False, low=True, zalgo_text=[]):
    zalgo_chars = [char for char in
              [zalgo_mid  if mid else None,
               zalgo_up  if high else None,
               zalgo_down if low else None]
              if char]    
    for i in xrange(len(text)):
        zalgo_text.append(text[i])
        for j in xrange(random.randint(1, 30)):
            zalgo_text.append((random.choice(Merge(zalgo_chars))))
    return u''.join(zalgo_text)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print 'Usage: %s <some text>' % sys.argv[0]
        exit(1)
    print ZalgoChars(sys.argv[1])
    exit(1)
