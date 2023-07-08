from unittest import TestCase, main
from warmup.contains_duplicate import containsDuplicate


class TestContainsDuplicate(TestCase):

    def test_case_1(self):
        self.assertFalse(containsDuplicate([1, 2, 3, 4, 5]))

    def test_case_2(self):
        self.assertTrue(containsDuplicate([1, 2, 3, 4, 1]))

    def test_case_3(self):
        self.assertFalse(containsDuplicate([]))

    def test_case_4(self):
        self.assertFalse(containsDuplicate([1]))

    def test_case_5(self):
        self.assertTrue(containsDuplicate([1, 1, 1, 1, 1]))


if __name__ == '__main__':
    main()
