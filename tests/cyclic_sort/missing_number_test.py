from unittest import TestCase, main
from cyclic_sort.missing_number import find_missing_number


class TestFindMissingNumber(TestCase):

    def test_empty_list(self):
        self.assertEqual(find_missing_number([]), 0)

    def test_no_missing_number(self):
        self.assertEqual(find_missing_number([0, 1, 2, 3]), 4)

    def test_missing_number_at_start(self):
        self.assertEqual(find_missing_number([1, 2, 3]), 0)

    def test_missing_number_at_end(self):
        self.assertEqual(find_missing_number([0, 1, 2]), 3)

    def test_missing_number_in_middle(self):
        self.assertEqual(find_missing_number([0, 1, 3]), 2)

    def test_list_with_duplicates(self):
        self.assertEqual(find_missing_number([0, 0, 1, 2]), 3)

    def test_list_with_negative_numbers(self):
        self.assertEqual(find_missing_number([-1, 0, 1]), 2)

    def test_list_with_unsorted_numbers(self):
        self.assertEqual(find_missing_number([2, 0, 1]), 3)

    def test_list_with_large_numbers(self):
        self.assertEqual(find_missing_number([0, 1000000, 1]), 2)

    def test_leetcode_1(self):
        self.assertEqual(find_missing_number([3, 0, 1]), 2)

    def test_leetcode_2(self):
        self.assertEqual(find_missing_number([0, 1]), 2)

    def test_leetcode_3(self):
        self.assertEqual(find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)


if __name__ == '__main__':
    main()
