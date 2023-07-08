from unittest import TestCase, main
from warmup.sqr_root import sqrt


class TestSqrt(TestCase):

    def test_sqrt_zero(self):
        # Test that the square root of zero is zero
        self.assertEqual(sqrt(0), 0)

    def test_sqrt_one(self):
        # Test that the square root of one is one
        self.assertEqual(sqrt(1), 1)

    def test_sqrt_perfect_square(self):
        # Test that the square root of a perfect square is an integer
        self.assertEqual(sqrt(4), 2)
        self.assertEqual(sqrt(9), 3)
        self.assertEqual(sqrt(16), 4)

    def test_sqrt_non_perfect_square(self):
        # Test that the square root of a non-perfect square is rounded down to the nearest integer
        self.assertEqual(sqrt(2), 1)
        self.assertEqual(sqrt(3), 1)
        self.assertEqual(sqrt(5), 2)
        self.assertEqual(sqrt(6), 2)
        self.assertEqual(sqrt(7), 2)
        self.assertEqual(sqrt(8), 2)

    def test_sqrt_large_number(self):
        # Test that the square root of a large number is computed correctly
        self.assertEqual(sqrt(1000000), 1000)
        self.assertEqual(sqrt(123456789), 11111)

    def test_sqrt_design_gurus(self):
        # Test that the square root of a large number is computed correctly
        self.assertEqual(sqrt(8), 2)
        self.assertEqual(sqrt(4), 2)
        self.assertEqual(sqrt(2), 1)

    def test_sqrt_negative(self):
        # Test that the square root of a negative number raises an exception
        self.assertRaises(ValueError, sqrt, -1)
        self.assertRaises(ValueError, sqrt, -4)
        self.assertRaises(ValueError, sqrt, -9)

    def test_sqrt_float(self):
        # Test that the square root of a non-integer converts the input to an integer
        self.assertEqual(sqrt(2.0), 1)
        self.assertEqual(sqrt(3.5), 1)
        self.assertEqual(sqrt(4.9), 2)

    def test_sqrt_string(self):
        # Test that the square root of a non-integer converts the input to an integer
        with self.assertRaises(TypeError):
            sqrt("5")
        with self.assertRaises(TypeError):
            sqrt("6.7")

    def test_sqrt_very_large_number(self):
        # Test that the square root of a very large number returns a reasonable value
        self.assertLessEqual(sqrt(10**100), 10**50)
        self.assertLessEqual(sqrt(10**200), 10**100)
        self.assertLessEqual(sqrt(10**300), 10**150)


if __name__ == '__main__':
    main()
