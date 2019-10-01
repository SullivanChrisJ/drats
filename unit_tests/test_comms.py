""" test_comms.py Tests the low level communications modules for D-RATS.
    These are: agw.py, ax25.py, (more tbd)
"""

import os

import unittest

class test_utils(unittest.TestCase):

    def test_Python3_syntax(self):
        import d_rats.utils

class test_AGWFrame_class(unittest.TestCase):

    def test_Python3_syntax(self):
        import d_rats.agw

    def test_agw_frame_defs(self):
        """ Test the functions listed in the AGW_FRAMES dictionary directly from the class.
            AGW_FRAMES is defined outside any class and each of the frame types is defined
            in its own class
        """
        import d_rats.agw
        for k, v in d_rats.agw.AGW_FRAMES.items():
            self.assertEqual(v.kind, ord(k), f"{v.__name__}.kind is {v.kind} but should be ord(k)")

    def test_agw_frame_defs(self):
        """ Instantiate object and test the packed method on the default values  """
        import d_rats.agw
        agw_frame = d_rats.agw.AGWFrame()
        self.assertEqual(agw_frame.packed(), 8*b'\x00'+2*10*b' '+8*b'\x00', "'packed' method returned incorrect value")
        
    def test_agw_set_payload(self):
        import d_rats.agw
        agw_frame = d_rats.agw.AGWFrame()
        agw_payload = "FB OM I'm 47 Y.O. ET work as movie*"
        agw_frame.set_payload(agw_payload)
        self.assertEqual(agw_frame.len, len(agw_payload), "AGWFRAME object returns incorrect length after 'set_payload'")
        self.assertEqual(agw_frame.get_payload(), agw_payload, "AGWFRAME 'get_payload' returns incorrect value")

    def test_agw_payload_packing(self):
        """ Tests that when an agw payload is set that correct values are returned by the packed method.
            The packed method will convert strings (call_from, call_to, payload) to a byte object. The
            length field is set and encoded as a 32 bit integer. The encoding of the length field in this
            test is limited to 255 byte strings.
        """
        import d_rats.agw
        agw_frame = d_rats.agw.AGWFrame()
        agw_payload = "FB OM I'm 47 Y.O. ET work as movie*"
        agw_frame.set_payload(agw_payload)
        self.assertEqual(agw_frame.packed(), 
                         8*b'\x00'+2*10*b' '+bytes((len(agw_payload),))+bytes(7)+bytes(agw_payload, 'ascii'),
                         "'packed' method returned incorrect value")        

    def test_agw_call_signs(self):
        import d_rats.agw
        agw_frame = d_rats.agw.AGWFrame()
        agw_frame.set_from('VE3NRT')
        agw_frame.set_to('W1AW/KH6')
        self.assertEqual(agw_frame.get_from(), 'VE3NRT\x00\x00\x00\x00', "agw.py: get_from() call sign is not the same as set_from")
        self.assertEqual(agw_frame.get_to(), 'W1AW/KH6\x00\x00', "agw.py: get_from() call sign is not the same as set_from")

    def test_agw_call_sign_packing(self):
        import d_rats.agw
        agw_frame = d_rats.agw.AGWFrame()
        agw_frame.set_from('VE3NRT')
        agw_frame.set_to('W1AW/KH6')
        self.assertEqual(agw_frame.packed(), 8*b'\x00'+b'VE3NRT\x00\x00\x00\x00W1AW/KH6\x00\x00'+8*b'\x00',
                         "packed call signs returned incorrect values")

    def test_to_the_finish(self):
        assert False, "Finish the tests for agw.py"

class test_AGWConnection_class(unittest.TestCase):

    def test_instantiation(self):
        """ Opens a connection on port 8000. Right now, there's nothing to
            catch it
        """
        from d_rats.agw import AGWConnection
        port = 8000
        agwc = AGWConnection('127.0.0.1', port, timeout=3)
        agwc = AGWConnection('localhost', port, timeout=3)


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


class test_comm(unittest.TestCase):

    def test_Python3_syntax(self):
        import d_rats.comm as comm


if __name__ == '__main__': 
    print(os.path)
    unittest.main(warnings='ignore')
