from pynapi import pyNapi
from pynapi.cmdline import cmdline
import unittest

class TestMain(unittest.TestCase):
    def test_init(self):
        napi = pyNapi(
                language = 'en',
                encoding = 'utf-8',
        )

    def test_cmdline(self):
        cmdline()
