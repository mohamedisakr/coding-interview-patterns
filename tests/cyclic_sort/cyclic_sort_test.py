from unittest import TestCase, main
from cyclic_sort.cyclic_sort import cyclic_sort


class TestCyclicSort(TestCase):

    def test_empty_array(self):
        self.assertEqual(cyclic_sort([]), [])

    def test_one_element(self):
        self.assertEqual(cyclic_sort([1]), [1])

    def test_already_sorted(self):
        self.assertEqual(cyclic_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_reverse_sorted(self):
        self.assertEqual(cyclic_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_random_order(self):
        self.assertEqual(cyclic_sort([3, 1, 5, 4, 2]), [1, 2, 3, 4, 5])

    def test_random_order_2(self):
        self.assertEqual(cyclic_sort([2, 6, 4, 3, 1, 5]), [1, 2, 3, 4, 5, 6])

    def test_random_order_3(self):
        self.assertEqual(cyclic_sort([1, 5, 6, 4, 3, 2]), [1, 2, 3, 4, 5, 6])

    def test_duplicates(self):
        self.assertEqual(cyclic_sort([2, 6, 4, 3, 2, 5]), [2, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    main()
