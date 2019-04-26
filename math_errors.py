#!/bin/env python

import unittest

class TestMathErrors(unittest.TestCase):
    """
      For each test, make an adjustment so that the value of 'x' will
      equal the value of 'answer'
    """
    
    def test_00(self):
        x = 2 - 1
        answer = 1
        self.assertEqual(x, answer)

    def test_01(self):
        x = 100 * 2
        answer = 200
        self.assertEqual(x, answer)

    def test_02(self):
        x = 0
        for i in range(10):
            x += i
        answer = 55
        self.assertEqual(x, answer)
        
    def test_03(self):
        x = 3 + 2 + 3 * 4.
        answer = 17
        self.assertEqual(x, answer)

    def test_04(self):
        x = 2 ** 4
        answer = 16
        self.assertEqual(x, answer)

    def test_05(self):
        grocery_list = {
            'eggs': 17.10,
            'bread': 0.00,
            'cheese': 0.00,
        }
        x = sum(grocery_list.values())
        answer = 17.10
        self.assertEqual(x, answer)
            
if __name__ == '__main__':
    unittest.main()
