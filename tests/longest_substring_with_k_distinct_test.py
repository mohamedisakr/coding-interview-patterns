from unittest import TestCase, main

from sliding_window.longest_substring_with_k_distinct import longest_substring_with_k_distinct


class TestLongestSubstringKDistinct(TestCase):

    def test_empty_string(self):
        # Test case for empty string input
        text = ""
        k = 2
        with self.assertRaises(ValueError):
            longest_substring_with_k_distinct(text, k)

    def test_zero_k(self):
        # Test case for zero k input
        text = "abc"
        k = 0
        with self.assertRaises(ValueError):
            longest_substring_with_k_distinct(text, k)

    def test_valid_input(self):
        # Test case for valid input
        text = "araaci"
        k = 2
        actual = longest_substring_with_k_distinct(text, k)
        self.assertEqual(actual, 4)

    def test_larger_k(self):
        # Test case for k larger than the length of the string
        text = "araaci"
        k = 10
        with self.assertRaises(ValueError):
            longest_substring_with_k_distinct(text, k)

    def test_one_distinct_character(self):
        # Test case for a string with only one distinct character
        text = "aaaaa"
        k = 2
        actual = longest_substring_with_k_distinct(text, k)
        self.assertEqual(actual, 5)

    def test_all_distinct_characters(self):
        # Test case for a string with all distinct characters
        text = "abcdef"
        k = 3
        actual = longest_substring_with_k_distinct(text, k)
        self.assertEqual(actual, 3)

    def test_repeated_characters(self):
        # Test case for a string with repeated characters
        text = "ababac"
        k = 3
        actual = longest_substring_with_k_distinct(text, k)
        self.assertEqual(actual, 6)
        # self.assertEqual(longest_substring_k_distinct("ababac", 2), 4)

    def test_non_string_input_number(self):
        # Test case for a non-string input
        text = 123
        k = 2
        with self.assertRaises(TypeError):
            longest_substring_with_k_distinct(text, k)

    def test_non_string_input_array(self):
        # Test case for a non-string input
        text = ["a", "b", "c"]
        k = 2
        with self.assertRaises(TypeError):
            longest_substring_with_k_distinct(text, k)

    def test_invalid_k_input_k_negative(self):
        # Test case for a negative or non-integer k input
        text = "abc"
        k = -1
        with self.assertRaises(ValueError):
            longest_substring_with_k_distinct(text, k)

    def test_invalid_k_input_k_float(self):
        # Test case for a negative or non-integer k input
        text = "abc"
        k = 1.5
        with self.assertRaises(TypeError):
            longest_substring_with_k_distinct(text, k)


if __name__ == "__main__":
    main()
