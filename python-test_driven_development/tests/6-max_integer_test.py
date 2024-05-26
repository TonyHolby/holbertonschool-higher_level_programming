""" Tests with the Unittests module. """

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMyFunction(unittest.TestCase):
    """ Defines unittests for the function max_integer()."""

    def test_list_of_int(self):
        """ Tests a list of integers. """
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(my_list), 5)

    def test_max_at_the_beginning(self):
        """ Tests a list the max value at the beginning. """
        my_list = [10, 3, 2, 1]
        self.assertEqual(max_integer(my_list), 10)

    def test_list_with_negative_int(self):
        """ Tests a list of integers. """
        my_list = [1, 90, 2, 13, 34, 5, -13, 3]
        self.assertEqual(max_integer(my_list), 90)

    def test_empty_list(self):
        """ Tests an empty list. """
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def test_one_element(self):
        """ Tests a list with one integer. """
        my_list = [23]
        self.assertEqual(max_integer(my_list), 23)

    def test_only_floats(self):
        """ Tests a list of floats. """
        my_list = [1.23, 4.56, -1.007, 78.9, 8.0]
        self.assertEqual(max_integer(my_list), 78.9)

    def test_integers_and_floats(self):
        """ Tests a list of integers and floats. """
        my_list = [1.23, 4.56, -1, 79, 8]
        self.assertEqual(max_integer(my_list), 79)

    def test_list_of_strings(self):
        """ Tests a list of strings. """
        my_list = ["Holberton", "is", "my", "school"]
        self.assertEqual(max_integer(my_list), "school")

    def test_empty_string(self):
        """ Tests an empty string. """
        my_string = ""
        self.assertEqual(max_integer(my_string), None)

    def test_string(self):
        """ Tests a string. """
        my_string = "Best School"
        self.assertEqual(max_integer(my_string), 't')

if __name__ == '__main__':
    unittest.main()