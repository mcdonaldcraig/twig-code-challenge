import unittest
from codechallenge import *


class CodechallengeTestCase(unittest.TestCase):
    def test_check_number(self):
        # Test with positive number
        self.assertEqual(check_number(2), 2)

    def test_check_number_values(self):
        #  Test the number when 0
        self.assertRaises(ValueError, check_number, 0)
        #  Test a negative number
        self.assertRaises(ValueError, check_number, -12)

    def test_check_array(self):
        # Test an array with values
        self.assertEqual(check_array([1, 2]), [1, 2])

    def test_check_array_values(self):
        # Test an empty array
        self.assertRaises(ValueError, check_array, [])

    def test_create_split_array(self):
        # Test the split function is working as expected
        self.assertEqual(list(create_split_array([1, 2, 3, 4, 5], 3)), [[1, 2], [3, 4], [5]])
        self.assertEqual(list(create_split_array([1, 2, 3, 4, 5], 5)), [[1], [2], [3], [4], [5]])


if __name__ == '__main__':
    unittest.main()
