from pynapi import pyNapi
from pynapi.cmdline import cmdline
from pynapi.services import serviceBase
import unittest

class TestMain(unittest.TestCase):
    def test_init(self):
        napi = pyNapi(
                language = 'en',
                encoding = 'utf-8',
        )
        self.assertTrue(napi)

    def test_cmdline(self):
        self.assertTrue(cmdline)
