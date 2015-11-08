# -*- coding: utf-8 -*-
from pynapi.services import serviceBase
import os, sys, urllib
from hashlib import md5
import codecs

from pynapi.exc import PynapiException
class NapiprojektException(PynapiException):
    pass

# TODO logging

class Napiprojekt(serviceBase):
    priority = 10

    url_base = "http://napiprojekt.pl/unit_napisy/dl.php?"

    def __init__(self, language='pl'):
        self.language = language

    def get(self, filename):
        """ returns subtitles as string """
        params = {
            "v": 'dreambox',
            "kolejka": "false",

            "nick": "",
            "pass": "",

            "napios": sys.platform,
            "l": self.language.upper(),

            "f": self.prepareHash(filename),
        }
        params['t'] = self.discombobulate(params['f'])

        url = self.url_base + urllib.urlencode(params)

        subs = urllib.urlopen(url).read()

        if subs.startswith('brak pliku tymczasowego'):
            raise NapiprojektException('napiprojekt.pl API error')

        if subs[0:4] != 'NPc0':
            # napiprojekt keeps subtitles in cp1250
            # ... but, sometimes they are in utf8
            for cdc in ['cp1250', 'utf8']:
                try:
                    return codecs.decode(subs, cdc)
                except:
                    pass

    def discombobulate(self, filehash):
        """ prepare napiprojekt scrambled hash """

        idx = [0xe, 0x3, 0x6, 0x8, 0x2]
        mul = [2, 2, 5, 4, 3]
        add = [0, 0xd, 0x10, 0xb, 0x5]

        b = []
        for i in xrange(len(idx)):
            a = add[i]
            m = mul[i]
            i = idx[i]

            t = a + int(filehash[i], 16)
            v = int(filehash[t:t + 2], 16)
            b.append(("%x" % (v * m))[-1])

        return ''.join(b)

    def prepareHash(self, filename):
        if not os.path.isfile(filename):
            raise Exception('Not found')
        h = md5()
        h.update(open(filename, 'r').read(1024*1024*10))
        return h.hexdigest()

class Dummy(serviceBase):
    priority = 5
