""" test_comms.py Tests the low level communications modules for D-RATS.
    These are: agw.py, ax25.py, (more tbd)
"""

import os

import unittest

class test_utils(unittest.TestCase):

    def test_Python3_syntax(self):
        import d_rats.utils

class test_agw(unittest.TestCase):

    def test_Python3_syntax(self):
        import d_rats.agw


class test_ax25(unittest.TestCase):
    """ Test ax25.py. ax.25.py is dependent on utils.py for the hexprint function,
        which is only used for its stand-alone test in __main__.
    """ 

    def test_Python3_syntax(self):
        import d_rats.ax25 as ax25
        from d_rats.utils import hexprint

    def test_function_bitstuff(self):
        import d_rats.ax25 as ax25
        self.assertEqual(ax25.bitstuff("\xFF\xFF\xFF"), "\xfb\xfb\xfb\xe0")


if __name__ == '__main__': 
    print(os.path)
    unittest.main(warnings='ignore')