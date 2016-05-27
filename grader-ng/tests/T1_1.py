import unittest

from lab import my_email


class Test_1_1(unittest.TestCase):
    
    def test_my_email(self):
        self.assertEqual(1, my_email().count('@'))
        self.assertTrue(my_email().endswith('uclm.es'))

