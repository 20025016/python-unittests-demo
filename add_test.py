"""Testing whether add function passes test cases"""

import unittest

from add import add
from exceptions import InvalidArgumentException


class TestAdd(unittest.TestCase):
    """Testing whether add function passes test cases"""
    def test(self):
        """Performs all of the necessary tests for add function"""
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-3, 4), 1)
        self.assertEqual(add(-3, -3), -6)
        self.assertEqual(add(True, True), 2)
        with self.assertRaises(InvalidArgumentException):
            add("1", "2")
        with self.assertRaises(InvalidArgumentException):
            add([10], [15])


if __name__ == '__main__':
    unittest.main()
