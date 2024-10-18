import unittest
from test import add_num, process_input

class TestAddNum(unittest.TestCase):
    def test_add_positive_numbers(self):
        """Test that the sum of positive numbers is correctly calculated."""
        result = add_num([1, 2, 3, 4])
        self.assertEqual(result, 'Sum is 10')
    
    def test_add_mixed_numbers(self):
        """Test that negative numbers are flagged and excluded from the sum."""
        result = add_num([1, -2, 3, 4])
        self.assertEqual(result, 'negative numbers not allowed -2')

    def test_add_negative_numbers(self):
        """Test that all negative numbers are reported."""
        result = add_num([-1, -2, -3])
        self.assertEqual(result, 'negative numbers not allowed -1, -2, -3')

    def test_add_empty_list(self):
        """Test that the sum of an empty list is zero."""
        result = add_num([])
        self.assertEqual(result, 'Sum is 0')


class TestProcessInput(unittest.TestCase):
    def test_empty_input(self):
        """Test that empty input returns the appropriate error message."""
        result = process_input('')
        self.assertEqual(result, 'Input cannot be empty')

    def test_positive_input(self):
        """Test that positive input strings are processed correctly."""
        result = process_input('1, 2, 3')
        self.assertEqual(result, 'Sum is 6')

    def test_mixed_input(self):
        """Test that input strings containing both positive and negative numbers are processed correctly."""
        result = process_input('1, -2, 3, 4')
        self.assertEqual(result, 'negative numbers not allowed -2')

    def test_negative_input(self):
        """Test that input strings containing only negative numbers are processed correctly."""
        result = process_input('-1, -2, -3')
        self.assertEqual(result, 'negative numbers not allowed -1, -2, -3')


if __name__ == '__main__':
    unittest.main()

