#!/usr/bin/python
import unittest
from basicfunction import BasicFunction
 
class TestBasicFunction(unittest.TestCase):
    def setUp(self):
        self.func = BasicFunction()
 
    def test_1(self):
        self.assertTrue(True)
 
    def test_2(self):
        self.assertTrue(True)
 
    def test_3(self):
        self.assertEqual(self.func.state, 0)
 
if __name__ == '__main__':
    unittest.main()