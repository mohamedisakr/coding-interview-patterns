from unittest import TestCase, main
from two_pointers.pair_with_target_sum import pair_with_target_sum_2_pointers


class TestPairWithTargetSum(TestCase):

    def test_pair_with_target_sum_empty_array(self):
        with self.assertRaises(ValueError):
            pair_with_target_sum_2_pointers([], 7)

    def test_pair_with_target_sum_equal_first_last(self):
        self.assertEqual(pair_with_target_sum_2_pointers(
            [1, 2, 3, 4, 6], 7), [0, 4])
        self.assertEqual(pair_with_target_sum_2_pointers(
            [3, 5, 12, 17], 20), [0, 3])

    def test_pair_with_target_sum_exists(self):
        self.assertEqual(pair_with_target_sum_2_pointers(
            [1, 2, 3, 4, 6], 6), [1, 3])
        self.assertEqual(pair_with_target_sum_2_pointers(
            [2, 5, 9, 11], 11), [0, 2])
        self.assertEqual(pair_with_target_sum_2_pointers([4, 4], 8), [0, 1])

    def test_pair_with_target_sum_not_exists(self):
        # self.assertEqual(pair_with_target_sum([], 10), [-1, -1])
        with self.assertRaises(ValueError):
            pair_with_target_sum_2_pointers([], 10)

    def test_pair_with_target_sum_invalid_input(self):
        with self.assertRaises(TypeError):
            pair_with_target_sum_2_pointers([1, 2, 3], "a")
            # self.assertEqual(pair_with_target_sum([1, 2, 3], "a"), [-1, -1])

    def test_pair_with_target_sum_float_input(self):
        self.assertEqual(pair_with_target_sum_2_pointers(
            [1.5, 2.5, 3.5], 4), [0, 1])

    # TODO
    '''
    def test_pair_with_target_sum_invalid_input_none_type(self):
        self.assertEqual(pair_with_target_sum(None, 5), [-1, -1])
        self.assertEqual(pair_with_target_sum([1, 2, 3], None), [-1, -1])
    '''

    '''
    def setUp(self):
        self.test_cases = [
            ([1, 2, 3, 4, 6], 6, [1, 3]),
            ([2, 5, 9, 11], 11, [0, 2]),
            ([4, 4], 8, [0, 1]),
            ([3, 5, 12, 17], 20, [-1, -1]),
            ([], 10, [-1, -1]),
            (None, 5, [-1, -1]),
            ([1, 2, 3], None, [-1, -1]),
            ([1, 2, 3], "a", [-1, -1]),
            ([1.5, 2.5, 3.5], 4, [0, 1])
        ]

    def test_all_cases(self):
        for arr, target_sum, expected in self.test_cases:
            actual = pair_with_target_sum(arr, target_sum)
            self.assertEqual(actual, expected)
        
    '''

    '''
    def test_case_1(self):
        arr = [1, 2, 3, 4, 6]
        self.assertEqual(pair_with_target_sum(, 6), [1, 3])

    def test_case_2(self):
        self.assertEqual(pair_with_target_sum([2, 5, 9, 11], 11), [0, 2])

    def test_case_3(self):
        self.assertEqual(pair_with_target_sum([4, 4], 8), [0, 1])

    def test_case_4(self):
        self.assertEqual(pair_with_target_sum([3, 5, 12, 17], 20), [-1, -1])

    def test_case_5(self):
        self.assertEqual(pair_with_target_sum([], 10), [-1, -1])
    '''


if __name__ == '__main__':
    main()
