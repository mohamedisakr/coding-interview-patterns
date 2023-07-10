from unittest import TestCase, main
from top_k_elements.kth_smallest_number import find_kth_smallest_number


class TestFindKthSmallestNumber(TestCase):

    # Test case 1: normal input
    def test_normal_input(self):
        nums = [7, 10, 4, 3, 20, 15]
        k = 3
        expected = 7
        actual = find_kth_smallest_number(nums, k)
        self.assertEqual(expected, actual)

    # Test case 2: empty input
    def test_empty_input(self):
        nums = []
        k = 1
        expected = None
        actual = find_kth_smallest_number(nums, k)
        self.assertEqual(expected, actual)

    # Test case 3: invalid k
    def test_invalid_k(self):
        nums = [5, 2, 9, 6, 1]
        k = 6
        expected = None
        actual = find_kth_smallest_number(nums, k)
        self.assertEqual(expected, actual)

    # Test case 4: negative numbers
    def test_negative_numbers(self):
        nums = [-5, -2, -9, -6, -1]
        k = 2
        expected = 2
        actual = find_kth_smallest_number(nums, k)
        self.assertEqual(expected, actual)

    # Test case 5: duplicate numbers
    def test_duplicate_numbers(self):
        nums = [3, 3, 3, 3, 3]
        k = 1
        expected = 3
        actual = find_kth_smallest_number(nums, k)
        self.assertEqual(expected, actual)

    # Test case 6: sorted numbers
    def test_sorted_numbers(self):
        nums = [1, 2, 3, 4, 5]
        k = 4
        expected = 4
        actual = find_kth_smallest_number(nums, k)
        self.assertEqual(expected, actual)


# Run the tests
if __name__ == '__main__':
    main()
