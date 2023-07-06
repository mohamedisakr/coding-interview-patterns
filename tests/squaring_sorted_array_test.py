from unittest import TestCase, main
from two_pointers.squaring_sorted_array import squaring_sorted_array


class TestSortedSquares(TestCase):
    # Define a method that tests the function with different inputs and expected outputs
    # def test_sorted_squares(self):
    #     # Use self.assertEqual to compare the function output with the expected output
    #     self.assertEqual(squaring_sorted_array(
    #         [-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])

    #     self.assertEqual(squaring_sorted_array(
    #         [-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])

    #     self.assertEqual(squaring_sorted_array(
    #         [-5, -4, -3, -2, -1]), [1, 4, 9, 16, 25])

    #     self.assertEqual(squaring_sorted_array(
    #         [1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])

    #     self.assertEqual(squaring_sorted_array([0]), [0])

    def test_leetcode_1(self):
        # Use self.assertEqual to compare the function output with the expected output
        self.assertEqual(squaring_sorted_array(
            [-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])

    def test_leetcode_2(self):
        # Use self.assertEqual to compare the function output with the expected output
        self.assertEqual(squaring_sorted_array(
            [-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])


# Run the tests
if __name__ == "__main__":
    main()
