""" test for find duplicate using cyclic sort
"""

from unittest import TestCase, main
from cyclic_sort.duplicate_number import find_duplicate


class TestFindDuplicate(TestCase):
    """ test for find duplicate using cyclic sort
    """

    def test_empty_list(self):
        # Test case for an empty list
        nums = []
        expected = -1
        actual = find_duplicate(nums)
        self.assertEqual(expected, actual)

    def test_no_duplicate(self):
        # Test case for a list with no duplicate
        nums = [1, 2, 3, 4, 5]
        expected = -1
        actual = find_duplicate(nums)
        self.assertEqual(expected, actual)

    def test_one_duplicate(self):
        # Test case for a list with one duplicate
        nums = [1, 4, 4, 3, 2]
        expected = 4
        actual = find_duplicate(nums)
        self.assertEqual(expected, actual)

    def test_multiple_duplicates(self):
        # Test case for a list with multiple duplicates
        nums = [1, 2, 3, 3, 4, 4]
        expected = 3  # or 4
        actual = find_duplicate(nums)
        self.assertIn(actual, [3, 4])

    def test_all_duplicates(self):
        # Test case for a list with all duplicates
        nums = [1, 1, 1, 1, 1]
        expected = 1
        actual = find_duplicate(nums)
        self.assertEqual(expected, actual)

    def test_invalid_input(self):
        # Test case for an invalid input
        nums = "abc"
        expected = -1

        # Option 1: use a try-except block
        # try:
        #     actual = find_duplicate(nums)
        # except TypeError:
        #     actual = -1
        # self.assertEqual(expected, actual)

        # Option 2: use assertRaises
        with self.assertRaises(TypeError):
            find_duplicate(nums)

    def test_out_of_range(self):
        # Test case for a list with elements out of range
        nums = [1, 6, 3, 4, 2]
        expected = -1
        # Option 1: use a try-except block
        # try:
        #     actual = find_duplicate(nums)
        # except IndexError:
        #     actual = -1
        # self.assertEqual(expected, actual)

        # Option 2: use assertRaises
        with self.assertRaises(IndexError):
            find_duplicate(nums)

    def test_one_element(self):
        # Test case for a list with one element
        nums = [1]
        expected = -1
        actual = find_duplicate(nums)
        self.assertEqual(expected, actual)
        # try:
        #     actual = find_duplicate(nums)
        # except TypeError:
        #     actual = -1
        # self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()

'''
    # ------------ from anthor duplicate test --------------

    # This is a test method that checks if the function works for an empty array
    def test_empty_array(self):
        arr = []
        # expected_length = 0
        # actual_length = remove_duplicates(arr)
        # self.assertEqual(expected_length, actual_length)
        with self.assertRaises(ValueError):
            remove_duplicates(arr)

    # This is another test method that checks if the function works for an array with no duplicates
    def test_no_duplicates(self):
        arr = [1, 2, 3, 4, 5]
        expected_length = 5
        actual_length = remove_duplicates(arr)
        self.assertEqual(expected_length, actual_length)

    # This is another test method that checks if the function works for an array with some duplicates
    def test_some_duplicates(self):
        arr = [1, 1, 2, 2, 3, 4, 5]
        expected_length = 5
        actual_length = remove_duplicates(arr)
        self.assertEqual(expected_length, actual_length)
        self.assertEqual(arr[:actual_length], [1, 2, 3, 4, 5])

    # This is a test method that checks if the function works for an array with all duplicates
    def test_all_duplicates(self):
        arr = [1, 1, 1, 1, 1]
        expected_length = 1
        actual_length = remove_duplicates(arr)
        self.assertEqual(expected_length, actual_length)
        self.assertEqual(arr[:actual_length], [1])

    # This is a test method that checks if the function works for an array with one element
    def test_one_element(self):
        arr = [5]
        expected_length = 1
        actual_length = remove_duplicates(arr)
        self.assertEqual(expected_length, actual_length)
        self.assertEqual(arr[:actual_length], [5])

    # This is a test method that checks if the function works for a large array with many duplicates
    def test_large_array(self):
        arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4] * 1000
        expected_length = 4
        actual_length = remove_duplicates(arr)
        self.assertEqual(expected_length, actual_length)
        # self.assertEqual(arr[:actual_length], [1, 2, 3, 4])

    # This is a test method that checks if the function raises an exception for an invalid input, such as None or a string
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_duplicates(None)

        with self.assertRaises(TypeError):
            remove_duplicates("hello")

'''
