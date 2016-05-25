import unittest

from L1_1 import my_email


class Test_1_1(unittest.TestCase):
    
    def test_my_email(self):
        self.assertEqual(1, my_email().count('@'))
        self.assertTrue(my_email().endswith('uclm.es'))

