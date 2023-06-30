from unittest import TestCase, main
from sliding_window.maximum_sum_sub_array_size_k import max_sum_sub_array


class TestMaxSumSubArray(TestCase):

    def test_max_sum_sub_array(self):
        # Test the function with some sample inputs and expected outputs
        self.assertEqual(max_sum_sub_array([2, 3, 4, 1, 5], 2), 7)
        self.assertEqual(max_sum_sub_array([1, 1, 1, 1, 1], 3), 3)
        # self.assertEqual(max_sum_sub_array([-2, -3, -4, -1, -5], 2), -3)
        # self.assertEqual(max_sum_sub_array([10, -5, 2, -1, 3], 4), 9)

    # TODO
    def test_negative_arr_values(self):
        """Test a case with a negative k."""
        arr = [-2, -3, -4, -1, -5]
        k = -3
        # with self.assertRaises(ValueError) as context:
        #     find_avg_sub_array_slide(arr, k)
        # self.assertEqual(str(context.exception), "k must be positive")
        with self.assertRaises(ValueError):
            max_sum_sub_array(arr, k)

    def test_max_sum_sub_array_empty(self):
        # Test the function with an empty array and expect a ValueError
        with self.assertRaises(ValueError):
            max_sum_sub_array([], 2)

    def test_max_sum_sub_array_invalid_k(self):
        # Test the function with some invalid values of k and expect a ValueError
        with self.assertRaises(ValueError):
            max_sum_sub_array([2, 3, 4, 1, 5], 0)
        with self.assertRaises(ValueError):
            max_sum_sub_array([2, 3, 4, 1, 5], -1)
        with self.assertRaises(ValueError):
            max_sum_sub_array([2, 3, 4, 1, 5], 6)

    def test_max_sum_sub_array_non_integer_k(self):
        # Test the function with a non-integer value of k and expect a TypeError
        with self.assertRaises(TypeError):
            max_sum_sub_array([2, 3, 4, 1, 5], "2")

    def test_max_sum_sub_array_one_element(self):
        # Test the function with an array that contains only one element
        self.assertEqual(max_sum_sub_array([5], 1), 5)

    def test_max_sum_sub_array_all_positive(self):
        # Test the function with an array that contains only positive numbers
        self.assertEqual(max_sum_sub_array([2, 4, 6, 8, 10], 3), 24)

    def test_max_sum_sub_array_all_negative(self):
        # Test the function with an array that contains only negative numbers
        # self.assertEqual(max_sum_sub_array([-2, -4, -6, -8, -10], 3), -12)
        with self.assertRaises(ValueError):
            max_sum_sub_array([-2, -4, -6, -8, -10], 3)

    def test_max_sum_sub_array_duplicates_zeros(self):
        # Test the function with an array that contains some duplicates or zeros
        self.assertEqual(max_sum_sub_array([0, 0, 0, 0, 0], 2), 0)
        self.assertEqual(max_sum_sub_array([1, 2, 3, 2, 1], 2), 5)

    def test_max_sum_sub_array_k_equal_length(self):
        # Test the function with a value of k that is equal to the length of the array
        self.assertEqual(max_sum_sub_array([2, 3, 4, 1, 5], 5), 15)

    def test_max_sum_sub_array_invalid_k_type(self):
        # Test the function with a value of k that is not a valid input type
        with self.assertRaises(TypeError):
            max_sum_sub_array([2, 3, 4, 1, 5], 2.5)
        with self.assertRaises(TypeError):
            max_sum_sub_array([2, 3, 4, 1, 5], [2])


if __name__ == "__main__":
    main()
