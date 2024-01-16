#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestInteger(unittest.Testcase):
    """
    Class for the unittest to test our function

    """
    def test_empty_list(self):
        """test if the list is empty"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def max_at_the_end(self):
        """Test a list with max integer at the end"""
        max_at_the_end = [1, 2, 3, 4]
        self.assertEqual(max_integer(max_at_the_end), 4)

    def test_max_beginning(self):
        """Test a list with max integer at the beginning"""
        max_beginning = [4, 1, 2, 3]
        self.asertEqual(max_integer(max_beginning), 4)

    def test ordered_list(self):
        """Test an ordered list"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test unordered_list(self):
        """Test an unordered list"""
        unordered = [1, 4, 3, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_unique(self):
        """Test a list with only one element"""
        unique = [40]
        self.assertEqual(max_integer(unique), 40)

    def test_ints_floats(self):
        """Test a list with a series of integers and floats"""
        list_t = [1.53, 5, 15.9, 15.1, 6.0]
        self.assertEqual(max_integer(list_t), 15.9)

    def test_float(self):
        """Test a list with floats only"""
        floats = [1.1, 2.2, 3.3, 4.4]
        self.assertEqual(max_integer(floats), 4.4)

    def test_datatypes(self):
        """Test a list of ints and strings"""
        with self.assertRaises(TypeError):
            max_integer([1, "1"])

    def test_nested_list(self):
        """Test a nested list"""
        list_t = [[1, 2], [2, 1]]
        self.assertEqual(max_integer(list_t), [2, 1])

    if __name__ == "__main__":
        unittest.main()
