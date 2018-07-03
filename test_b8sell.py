import unittest

from helga_b8sell import b8sell


class PluginTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_response(self):
        resp = b8sell(None, None, 'aineko', None, None, None, carat_ratio=1)
        assert '^' in resp
