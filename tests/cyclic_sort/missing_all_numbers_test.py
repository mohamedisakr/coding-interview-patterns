from unittest import TestCase, main
from cyclic_sort.missing_all_numbers import find_all_missing_numbers


class TestFindAllMissingNumbers(TestCase):

    def test_empty_list(self):
        self.assertEqual(find_all_missing_numbers([]), [])

    def test_no_missing_numbers(self):
        self.assertEqual(find_all_missing_numbers([1, 2, 3, 4, 5]), [])

    def test_multiple_missing_numbers(self):
        self.assertEqual(find_all_missing_numbers(
            [4, 3, 2, 7, 8, 2, 3, 1]), [5, 6])

    def test_duplicate_numbers(self):
        self.assertEqual(find_all_missing_numbers([2, 3, 2, 1]), [4])

    # def test_one_missing_number(self):
    #     self.assertEqual(find_all_missing_numbers([2, 3, 1, 5]), [4])

    def test_leetcode_1(self):
        self.assertEqual(find_all_missing_numbers(
            [4, 3, 2, 7, 8, 2, 3, 1]), [5, 6])

    def test_leetcode_2(self):
        self.assertEqual(find_all_missing_numbers([1, 1]), [2])

    # def test_negative_numbers(self):
    #     self.assertEqual(find_all_missing_numbers([-3, -1, -2]), [])

    def test_zero(self):
        self.assertEqual(find_all_missing_numbers([0, 1, 2]), [3])

    def test_non_integer_values(self):
        with self.assertRaises(TypeError):
            find_all_missing_numbers([1, 2, 'a', 4])

    def test_unsorted_list(self):
        self.assertEqual(find_all_missing_numbers([3, 1, 4, 2]), [])

    def test_large_list(self):
        self.assertEqual(find_all_missing_numbers(list(range(1, 10001))), [])

    def test_small_list(self):
        self.assertEqual(find_all_missing_numbers([1]), [])

    def test_same_numbers(self):
        self.assertEqual(find_all_missing_numbers([2, 2, 2, 2]), [1, 3, 4])


if __name__ == '__main__':
    main()
