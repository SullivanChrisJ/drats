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

    def test_agw_frame_defs(self):
        """ Test the functions listed in the AGW_FRAMES dictionary directly from the class """
        import d_rats.agw
        for k, v in d_rats.agw.AGW_FRAMES.items():
            self.assertEqual(v.kind, ord(k), f"{v.__name__}.kind is {v.kind} but should be ord(k)")

    def test_agw_frame_defs(self):
        """ Instantiate object and test the packed method on the default values  """
        import d_rats.agw
        agw_frame = d_rats.agw.AGWFrame()
        self.assertEqual(agw_frame.packed(), 8*b'\x00'+2*10*b' '+8*b'\x00', "'packed; method returned incorrect value")

    def test_agw_set_payload(self):
        import d_rats.agw
        agw_frame = d_rats.agw.AGWFrame()
        agw_payload = "FB OM I'm 47 Y.O. ET work as movie*"
        agw_frame.set_payload(agw_payload)
        self.assertEqual(agw_frame.len, len(agw_payload), "AGWFRAME object returns incorrect length after 'set_payload'")
        self.assertEqual(agw_frame.get_payload(), bytes(agw_payload, 'ascii'), 
                         "AGWFRAME 'get_payload' returns incorrect value")

class test_ax25(unittest.TestCase):
    """ Test ax25.py. ax.25.py is dependent on utils.py for the hexprint function,
        which is only used for its stand-alone test in __main__.
    """ 

    def test_Python3_syntax(self):
        import d_rats.ax25 as ax25
        from d_rats.utils import hexprint

    def test_function_bitstuff(self):
        import d_rats.ax25 as ax25
        # This test is included in ax25.py
        self.assertEqual(ax25.bitstuff("\xFF\xFF\xFF"), "\xfb\xfb\xfb\xe0")
        # All zeroes, nothing should change
        self.assertEqual(ax25.bitstuff("\x00\x00"), "\x00\x00")
        # No runs of more than 5 ones, but bits are reversed in each byte
        self.assertEqual(ax25.bitstuff("\xAB\xCD"), "\xD5\xB3")
        # The following test fails - bitstuff returns 80 in the last byte 
        self.assertEqual(ax25.bitstuff("\xFE\xFD"), "\x7D\xDF\x40")


if __name__ == '__main__': 
    print(os.path)
    unittest.main(warnings='ignore')