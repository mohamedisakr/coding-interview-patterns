from unittest import TestCase, main
from modified_binary_search.order_agnostic_binary_search import binary_search


class TestBinarySearch(TestCase):

    def test_empty_array(self):
        # Test searching an empty array
        arr = []
        key = 5
        expected = -1
        actual = binary_search(arr, key)
        self.assertEqual(expected, actual)

    def test_single_element_array_pass(self):
        # Test searching a single element array
        arr = [10]
        key = 10
        expected = 0
        actual = binary_search(arr, key)
        self.assertEqual(expected, actual)

    def test_single_element_array_fail(self):
        # Test searching a single element array
        arr = [10]
        key = 1
        expected = -1
        actual = binary_search(arr, key)
        self.assertEqual(expected, actual)

    def test_ascending_array(self):
        # Test searching an ascending array
        arr = [1, 2, 3, 4, 5]
        key = 3
        expected = 2
        actual = binary_search(arr, key)
        self.assertEqual(expected, actual)

    def test_descending_array(self):
        # Test searching a descending array
        arr = [5, 4, 3, 2, 1]
        key = 4
        expected = 1
        actual = binary_search(arr, key)
        self.assertEqual(expected, actual)

    def test_key_not_found(self):
        # Test searching for a key that is not in the array
        arr = [1, 3, 5, 7, 9]
        key = 6
        expected = -1
        actual = binary_search(arr, key)
        self.assertEqual(expected, actual)

    def test_key_at_start(self):
        # Test searching for a key that is at the start of the array
        arr = [1, 2, 3, 4, 5]
        key = 1
        expected = 0
        actual = binary_search(arr, key)
        self.assertEqual(expected, actual)

    def test_key_at_end(self):
        # Test searching for a key that is at the end of the array
        arr = [1, 2, 3, 4, 5]
        key = 5
        expected = 4
        actual = binary_search(arr, key)
        self.assertEqual(expected, actual)

    def test_key_in_middle(self):
        # Test searching for a key that is in the middle of the array
        arr = [1, 2, 3, 4, 5]
        key = 3
        expected = 2
        actual = binary_search(arr, key)
        self.assertEqual(expected, actual)

    def test_duplicate_keys(self):
        # Test searching for a key that has duplicates in the array
        arr = [1, 2, 2, 3, 3, 3, 4, 5]
        key = 3
        expected = [3, 4, 5]  # any of these indices are valid
        actual = binary_search(arr, key)
        self.assertIn(actual, expected)

    def test_key_less_than_lowest(self):
        # Test searching for a key that has duplicates in the array
        arr = [3, 4, 5]
        key = 2
        expected = -1  # any of these indices are valid
        actual = binary_search(arr, key)
        self.assertEqual(actual, expected)

    def test_key_greater_than_highest(self):
        # Test searching for a key that has duplicates in the array
        arr = [3, 4, 5]
        key = 6
        expected = -1  # any of these indices are valid
        actual = binary_search(arr, key)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    main()
