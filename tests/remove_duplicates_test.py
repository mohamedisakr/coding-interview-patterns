from unittest import TestCase, main
from two_pointers.remove_duplicates import remove_duplicates


class TestRemoveDuplicates(TestCase):

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


# This is the code that runs the tests
if __name__ == '__main__':
    main()
