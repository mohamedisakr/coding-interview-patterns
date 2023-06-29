from unittest import TestCase, main
from sliding_window.contiguous_subarrays_size import find_avg_sub_array_slide


class TestFindAvgSubArray(TestCase):

    def test_empty_array(self):
        # Test case for an empty array
        arr = []
        k = 5
        expected = []
        actual = find_avg_sub_array_slide(arr, k)
        self.assertEqual(expected, actual)

    def test_k_larger_than_array_length(self):
        # Test case for k larger than the array length
        arr = [1, 2, 3]
        k = 5
        expected = []
        actual = find_avg_sub_array_slide(arr, k)
        self.assertEqual(expected, actual)

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


if __name__ == '__main__':
    main()
