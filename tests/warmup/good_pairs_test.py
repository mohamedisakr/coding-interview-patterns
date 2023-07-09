from unittest import TestCase, main
from warmup.good_pairs import num_good_pairs


class TestNumGoodPairs(TestCase):

    def test_empty_array(self):
        # test case for an empty array
        self.assertEqual(num_good_pairs([]), 0)

    def test_single_element(self):
        # test case for an array with one element
        self.assertEqual(num_good_pairs([5]), 0)

    def test_no_good_pairs(self):
        # test case for an array with no good pairs
        self.assertEqual(num_good_pairs([1, 2, 3, 4]), 0)

    def test_no_good_pairs_2(self):
        # test case for an array with no good pairs
        self.assertEqual(num_good_pairs([1, 2, 3]), 0)

    def test_all_good_pairs(self):
        # test case for an array where all elements are equal
        self.assertEqual(num_good_pairs([7, 7, 7, 7]), 6)

    def test_all_good_pairs_2(self):
        # test case for an array where all elements are equal
        self.assertEqual(num_good_pairs([1, 1, 1, 1]), 6)

    def test_some_good_pairs(self):
        # test case for an array with some good pairs
        self.assertEqual(num_good_pairs([1, 2, 3, 1, 1, 3]), 4)


if __name__ == '__main__':
    main()
