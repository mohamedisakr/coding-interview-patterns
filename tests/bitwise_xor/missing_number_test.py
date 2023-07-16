from unittest import TestCase, main
from bitwise_xor.missing_number import find_missing_number_sort, find_missing_number_hashset

'''
class TestFindMissingNumberSort(TestCase):

    def test_empty_list(self):
        self.assertEqual(find_missing_number_sort([]), 0)

    def test_one_missing_number(self):
        self.assertEqual(find_missing_number_sort([0, 1, 3]), 2)

    def test_multiple_missing_numbers(self):
        self.assertEqual(find_missing_number_sort([0, 2, 4]), 1)

    def test_negative_numbers(self):
        self.assertEqual(find_missing_number_sort([-1, -2, -3]), 0)

    def test_zero_missing_number(self):
        self.assertEqual(find_missing_number_sort([1, 2, 3, 4]), 0)

    def test_large_numbers(self):
        self.assertEqual(find_missing_number_sort([0, 1000000, 2000000]), 1)

    def test_unsorted_list(self):
        self.assertEqual(find_missing_number_sort([3, 1, 0, 4]), 2)

    def test_unsorted_list_2(self):
        self.assertEqual(find_missing_number_sort([3, 0, 1]), 2)

    def test_unsorted_list_3(self):
        self.assertEqual(find_missing_number_sort(
            [9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)

    def test_sorted_list(self):
        self.assertEqual(find_missing_number_sort([0, 1]), 2)

    def test_leetcode_1(self):
        self.assertEqual(find_missing_number_sort([3, 0, 1]), 2)

    # def test_no_missing_number(self):
    #     self.assertEqual(find_missing_number_sort([1, 2, 3]), 3)

    # def test_duplicate_numbers(self):
    #     self.assertEqual(find_missing_number_sort([0, 0, 1, 2]), 3)
'''


class TestFindMissingNumberHashset(TestCase):

    def test_empty_list(self):
        self.assertEqual(find_missing_number_hashset([]), 0)

    def test_one_missing_number(self):
        self.assertEqual(find_missing_number_hashset([0, 1, 3]), 2)

    def test_multiple_missing_numbers(self):
        self.assertEqual(find_missing_number_hashset([0, 2, 4]), 1)

    # def test_negative_numbers(self):
    #     self.assertEqual(find_missing_number_hashset([-1, -2, -3]), 0)

    # def test_zero_missing_number(self):
    #     self.assertEqual(find_missing_number_hashset([1, 2, 3, 4]), 0)

    def test_large_numbers(self):
        self.assertEqual(find_missing_number_hashset([0, 1000000, 2000000]), 1)

    def test_unsorted_list(self):
        self.assertEqual(find_missing_number_hashset([3, 1, 0, 4]), 2)

    def test_unsorted_list_2(self):
        self.assertEqual(find_missing_number_hashset([3, 0, 1]), 2)

    def test_unsorted_list_3(self):
        self.assertEqual(find_missing_number_hashset(
            [9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)

    def test_sorted_list(self):
        self.assertEqual(find_missing_number_hashset([0, 1]), 2)

    def test_one_element_array_leetcode(self):
        self.assertEqual(find_missing_number_hashset([1]), 0)

    def test_one_element_array_leetcode_2(self):
        self.assertEqual(find_missing_number_hashset([0]), 1)


if __name__ == '__main__':
    main()
