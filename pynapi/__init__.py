# -*- coding: utf-8 -*-
from . import services
import pkgutil
import codecs
import logging

# TODO logging

def list_services():
    """ returns list of available services """
    for importer, modname, ispkg in pkgutil.iter_modules(services.__path__):
        if ispkg is False:
            importer.find_module(modname).load_module(modname)

    services_list = list()
    for s in services.serviceBase.__subclasses__():
        services_list.append(s.__name__.lower())

    return services_list

class pyNapi(object):
    def __init__(self, language='pl', encoding='utf-8'):
        self.services = dict()
        self.language = language
        self.encoding = encoding

        self.load_services()

    def load_services(self):
        for importer, modname, ispkg in pkgutil.iter_modules(services.__path__):
            if ispkg is False:
                importer.find_module(modname).load_module(modname)

        for s in services.serviceBase.__subclasses__():
            self.services[s.__name__.lower()] = s(language=self.language)

    def get_subs(self, filename):
        #print "Gettings subtitles for '%s'" % filename
        for servicename, servicecallable in self.services.items():
            #print "using: %s" % servicename
            subs = servicecallable.get(filename)
            # TODO first wins, prioritize services somehow
            if subs:
                return self.reencode(subs)

    def reencode(self, subs):
        return codecs.encode(subs, self.encoding)

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
