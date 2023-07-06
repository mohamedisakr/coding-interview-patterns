from unittest import TestCase, main
from two_pointers.remove_all_key_instances import remove_all_key_instances


class TestRemoveAllKeyInstances(TestCase):

    def test_empty_arr(self):
        # test case for empty array
        arr = []
        key = 5
        with self.assertRaises(ValueError):
            remove_all_key_instances(arr, key)

    def test_no_key_in_arr(self):
        # test case for array with no key
        arr = [1, 2, 3, 4]
        key = 5
        expected_length = 4
        actual_length = remove_all_key_instances(arr, key)
        self.assertEqual(expected_length, actual_length)

    def test_all_key_in_arr(self):
        # test case for array with all key
        arr = [5, 5, 5, 5]
        key = 5
        expected_length = 0
        actual_length = remove_all_key_instances(arr, key)
        self.assertEqual(expected_length, actual_length)

    def test_some_key_in_arr(self):
        # test case for array with some key
        arr = [3, 2, 3, 6, 3, 10, 9, 3]
        key = 3
        expected_length = 4
        expected_arr = [2, 6, 10, 9]
        actual_length = remove_all_key_instances(arr, key)
        self.assertEqual(expected_length, actual_length)
        self.assertListEqual(expected_arr, arr[:actual_length])

    def test_negative_key_in_arr(self):
        # test case for array with negative key
        arr = [-1, -2, -3, -4]
        key = -3
        expected_length = 3
        expected_arr = [-1, -2, -4]
        actual_length = remove_all_key_instances(arr, key)
        self.assertEqual(expected_length, actual_length)
        self.assertListEqual(expected_arr, arr[:actual_length])

    def test_key_as_first_element_in_arr(self):
        # test case for array with key as first element
        arr = [5, 1, 2, 3, 4]
        key = 5
        expected_length = 4
        expected_arr = [1, 2, 3, 4]
        actual_length = remove_all_key_instances(arr, key)
        self.assertEqual(expected_length, actual_length)
        self.assertListEqual(expected_arr, arr[:actual_length])

    def test_key_as_last_element_in_arr(self):
        # test case for array with key as last element
        arr = [1, 2, 3, 4, 5]
        key = 5
        expected_length = 4
        expected_arr = [1, 2, 3, 4]
        actual_length = remove_all_key_instances(arr, key)
        self.assertEqual(expected_length, actual_length)
        self.assertListEqual(expected_arr, arr[:actual_length])


if __name__ == "__main__":
    main()
