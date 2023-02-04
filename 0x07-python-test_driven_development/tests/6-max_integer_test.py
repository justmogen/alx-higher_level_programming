import unittest
max_integer = __import__('6-max_integer').max_integer

class findMaxInteger(unittest.TestCase):
    def test_empty_lis(self):
        self.assertEqual(max_integer([]), None)

    def test_negative_int(self):
        self.assertEqual(max_integer([-9, -6, -22, -80, -2]), -2)

    def test_multiple_ints(self):
        self.assertEqual(max_integer([332, 32, 90, 24, 33, 60]), 332)
        self.assertEqual(max_integer([32, 3, 9, 124, 33, 60]), 124)

    def test_single_element(self):
        self.assertEqual(max_integer([1]), 1)

if __name__ == '__main__':
    unittest.main()
