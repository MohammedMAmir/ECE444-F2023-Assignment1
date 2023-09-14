#!/usr/bin/env python3

import unittest
from utils import utils

class utils_test(unittest.TestCase):
    def testReversal(self):
        self.assertEqual(utils.reversed(8005), 5008, "Should be 5008, but got " + str(utils.reversed(8005)))
        self.assertEqual(utils.reversed("bob"), 0, "Should be 0, but got " + str(utils.reversed("bob")))
        self.assertEqual(utils.reversed(5.0), 0, "Should be 0, but got " + str(utils.reversed(5.0)))

    def testFormatter(self):
        value = utils.formatter(8005)
        self.assertEqual(value[0], '0b1111101000101', "8005 in binary should be '0b1111101000101', but got " + str(value[0]))
        value = utils.formatter(8005)
        self.assertEqual(value[1], '0o17505', "8005 in binary should be '0o17505', but got " + value[1])

        value = utils.formatter("bob")
        self.assertEqual(value, 0, "\"bob\" should return 0, but got " + str(value))
        value = utils.formatter("5.0")
        self.assertEqual(value, 0, "5.0 should return 0, but got " + str(value))

if __name__ == '__main__':
    unittest.main()