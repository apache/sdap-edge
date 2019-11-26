import logging
import urllib.request, urllib.parse, urllib.error

from edge.writer.genericproxywriter import GenericProxyWriter

class Writer(GenericProxyWriter):
    def __init__(self, configFilePath):
        super(Writer, self).__init__(configFilePath)
