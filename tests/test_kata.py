import unittest
from src.kata import range_parser


class TestRangeParser(unittest.TestCase):
    def test_three_params(self):
        self.assertEqual(range_parser('1-10,14, 20-25:2'), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 20, 22, 24])

    def test_range_of_numbers(self):
        self.assertEqual(range_parser('5-10'), [5, 6, 7, 8, 9, 10])

    def test_one_number(self):
        self.assertEqual(range_parser('2'), [2])

if __name__ == '__main__':
    unittest.main()
