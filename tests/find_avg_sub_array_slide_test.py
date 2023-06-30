"""
test find_avg_sub_array_slide function
"""

from unittest import TestCase, main
from sliding_window.contiguous_subarrays_size import find_avg_sub_array_slide


class TestFindAvgSubArraySlide(TestCase):

    def test_empty_array(self):
        # Test case for an empty array
        arr = []
        k = 5

        # with self.assertRaises(ValueError) as context:
        #     print(f'test_empty_array --->> {str(context.exception)}')
        #     find_avg_sub_array_slide(arr, k)
        # self.assertEqual(str(context.exception), "arr must not be empty")
        with self.assertRaises(ValueError):
            find_avg_sub_array_slide(arr, k)

    def test_normal_case(self):
        """Test a normal case with valid inputs and outputs."""
        arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
        k = 5
        expected = [2.2, 2.8, 2.4, 3.6, 2.8]
        actual = find_avg_sub_array_slide(arr, k)
        self.assertEqual(expected, actual)

    def test_zero_k(self):
        """Test a case with zero as k."""
        arr = [1, 2, 3]
        k = 0
        # with self.assertRaises(ValueError) as context:
        #     find_avg_sub_array_slide(arr, k)
        # self.assertEqual(str(context.exception), "k must be positive")
        with self.assertRaises(ValueError):
            find_avg_sub_array_slide(arr, k)

    def test_k_larger_than_length(self):
        """Test a case with k larger than the length of the array."""
        arr = [1, 2, 3]
        k = 4
        # with self.assertRaises(ValueError) as context:
        #     find_avg_sub_array_slide(arr, k)
        # self.assertEqual(str(context.exception),
        #                  "k must not be larger than the length of the array")
        with self.assertRaises(ValueError):
            find_avg_sub_array_slide(arr, k)

    def test_k_equal_to_array_length(self):
        # Test case for k equal to the array length
        arr = [1, 2, 3, 4, 5]
        k = 5
        expected = [3.0]
        actual = find_avg_sub_array_slide(arr, k)
        self.assertEqual(expected, actual)

    def test_k_smaller_than_array_length(self):
        # Test case for k smaller than the array length
        arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
        k = 5
        expected = [2.2, 2.8, 2.4, 3.6, 2.8]
        actual = find_avg_sub_array_slide(arr, k)
        self.assertEqual(expected, actual)

    def test_negative_k(self):
        """Test a case with a negative k."""
        arr = [1, 2, 3]
        k = -1
        # with self.assertRaises(ValueError) as context:
        #     find_avg_sub_array_slide(arr, k)
        # self.assertEqual(str(context.exception), "k must be positive")
        with self.assertRaises(ValueError):
            find_avg_sub_array_slide(arr, k)

# ---------------------

    def test_single_element_array(self):
        """ A test method that checks if the function returns the correct 
        average for a single element array and k = 1"""
        arr = [5]
        k = 1
        actual = find_avg_sub_array_slide(arr, k)
        expected = [5.0]
        self.assertEqual(actual, expected)

    def test_array_equal_to_k(self):
        """ A test method that checks if the function returns the correct 
        averages for an array of length k"""
        arr = [1, 2, 3, 4, 5]
        k = 5
        actual = find_avg_sub_array_slide(arr, k)
        expected = [3.0]
        self.assertEqual(actual, expected)

    def test_array_with_negative_numbers(self):
        """ A test method that checks if the function returns the correct 
        averages for an array with negative numbers"""
        arr = [-1, -2, -3, -4, -5]
        k = 3
        actual = find_avg_sub_array_slide(arr, k)
        expected = [-2.0, -3.0, -4.0]

        self.assertEqual(actual, expected)

    def test_array_with_floats(self):
        """A test method that checks if the function returns the correct 
        averages for an array with floating point numbers"""
        arr = [1.5, 2.5, 3.5, 4.5, 5.5]
        k = 4
        actual = find_avg_sub_array_slide(arr, k)
        expected = [3.0, 4.0]

        self.assertEqual(actual, expected)


# ------------------
if __name__ == '__main__':
    main()
