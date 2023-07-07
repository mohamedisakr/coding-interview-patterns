from unittest import TestCase, main
from fast_slow_pointers.happy_number import is_happy_number


class TestHappyNumber(TestCase):

    def test_happy_number(self):
        # Test if the function returns True for a happy number
        self.assertTrue(is_happy_number(19))
        self.assertTrue(is_happy_number(7))
        self.assertTrue(is_happy_number(1))

    def test_not_happy_number(self):
        # Test if the function returns False for a not happy number
        self.assertFalse(is_happy_number(18))
        self.assertFalse(is_happy_number(4))
        self.assertFalse(is_happy_number(0))

    def test_invalid_input(self):
        # Test if the function raises an exception for an invalid input
        with self.assertRaises(TypeError):
            is_happy_number("a")
        with self.assertRaises(TypeError):
            is_happy_number([1, 2, 3])
        with self.assertRaises(TypeError):
            is_happy_number(None)


# if __name__ == "__main__":
#     main()
