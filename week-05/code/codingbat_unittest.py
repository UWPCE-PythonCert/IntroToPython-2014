#!/usr/bin/env python

"""
test file for codingbat module

This version used unittest
"""

import unittest
from codingbat import sleep_in

class Test_sleep_in(unittest.TestCase):
    
    def test_false_false(self):
        self.assertTrue( sleep_in(False, False) )
    
    def test_true_false(self):
        self.assertFalse( sleep_in(True, False) )

    def test_false_true(self):
        self.assertTrue( sleep_in(False, True) )

    def test_true_true(self):
        self.assertTrue( sleep_in(True, True) )

if __name__ == "__main__":
    unittest.main()
    
    