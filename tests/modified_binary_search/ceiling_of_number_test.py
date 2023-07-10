from unittest import TestCase, main
from modified_binary_search.ceiling_of_number import search_ceiling_of_number


class TestSearchCeilingOfNumber(TestCase):

    def test_empty_array(self):
        # Test case for an empty array
        self.assertEqual(search_ceiling_of_number([], 5), -1)

    def test_key_greater_than_max(self):
        # Test case for a key greater than the maximum element in the array
        self.assertEqual(search_ceiling_of_number([1, 3, 8, 10, 15], 20), -1)

    def test_key_equal_to_element(self):
        # Test case for a key equal to an element in the array
        self.assertEqual(search_ceiling_of_number([1, 3, 8, 10, 15], 10), 3)

    def test_key_less_than_min(self):
        # Test case for a key less than the minimum element in the array
        self.assertEqual(search_ceiling_of_number([1, 3, 8, 10, 15], -5), 0)

    def test_key_between_elements(self):
        # Test case for a key between two elements in the array
        self.assertEqual(search_ceiling_of_number([1, 3, 8, 10, 15], 6), 2)

    def test_single_element_array(self):
        # Test case for a single element array
        self.assertEqual(search_ceiling_of_number([5], 5), 0)
        self.assertEqual(search_ceiling_of_number([5], 4), 0)
        self.assertEqual(search_ceiling_of_number([5], 6), -1)

    def test_duplicate_elements_array(self):
        # Test case for an array with duplicate elements
        self.assertEqual(search_ceiling_of_number([1, 3, 3, 8, 10, 15], 4), 3)
        self.assertEqual(search_ceiling_of_number([1, 3, 3, 8, 10, 15], 8), 3)

    def test_duplicate_elements_array_1(self):
        # Test case for an array with duplicate elements
        arr = [1, 3, 3, 8, 10, 15]
        key = 3
        expected = [1, 2]
        actual = search_ceiling_of_number(arr, key)
        self.assertIn(actual, expected)

    def test_negative_elements_array(self):
        # Test case for an array with negative elements
        self.assertEqual(search_ceiling_of_number([-5, -3, -1, 0, 2], -4), 1)
        self.assertEqual(search_ceiling_of_number([-5, -3, -1, 0, 2], 1), 4)
        self.assertEqual(search_ceiling_of_number([-5, -3, -1, 0, 2], 3), -1)

    def test_large_elements_array(self):
        # Test case for an array with large elements
        self.assertEqual(search_ceiling_of_number(
            [1000, 2000, 3000, 4000, 5000], 4500), 4)
        # self.assertEqual(search_ceiling_of_number(
        #     [1000, 2000, 3000, 4000, 5000], 2500), 2)
        # self.assertEqual(search_ceiling_of_number(
        #     [1000, 2000, 3000, 4000, 5000], 6000), -1)


if __name__ == '__main__':
    main()
