from unittest import TestCase, main
from sliding_window.smallest_subarray_with_given_sum import smallest_subarray_with_given_sum

# A class for testing your function


class TestSmallestSubarrayWithGivenSum(TestCase):

    # A helper method to run a single test case
    def check(self, arr, s, expected):
        actual = smallest_subarray_with_given_sum(arr, s)
        self.assertEqual(actual, expected)

    # Test cases
    def test_empty_array(self):
        self.check([], 10, 0)

    def test_single_element_equal(self):
        self.check([5], 5, 1)

    def test_single_element_greater(self):
        self.check([5], 6, 0)

    def test_multiple_elements(self):
        self.check([2, 1, 5, 2, 3, 2], 7, 2)
        self.check([2, 1, 5, 2, 8], 7, 1)
        self.check([3, 4, 1, 1, 6], 8, 3)
        self.check([1, 2, 3], 6, 3)
        self.check([1, 2, 3], 7, 0)


# Run the tests
if __name__ == "__main__":
    main()
