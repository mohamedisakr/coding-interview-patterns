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

    # test cases from leetcode
    # 395. Longest Substring with At Least K Repeating Characters
    # https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
    def test_leetcode_case_2(self):
        text = "ababbc"
        k = 2
        actual = longest_substring_with_k_distinct(text, k)
        self.assertEqual(actual, 5)

    def test_leetcode_case_1(self):
        text = "aaabb"
        k = 3
        actual = longest_substring_with_k_distinct(text, k)
        self.assertEqual(actual, 5)

    # test cases from geeksforgeeks
    # Find the longest substring with k unique characters in a given string
    # https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/
    def test_geeks_case_1(self):
        text = "aabbcc"
        k = 1
        actual = longest_substring_with_k_distinct(text, k)
        self.assertEqual(actual, 2)

    def test_geeks_case_2(self):
        text = "aabbcc"
        k = 2
        actual = longest_substring_with_k_distinct(text, k)
        self.assertEqual(actual, 4)

    def test_geeks_case_3(self):
        text = "aabbcc"
        k = 3
        actual = longest_substring_with_k_distinct(text, k)
        self.assertEqual(actual, 6)

    # test cases from stackoverflow
    # Longest Substring Containing K Distinct Characters
    # https://stackoverflow.com/questions/69282557/longest-substring-containing-k-distinct-characters
    def test_stackoverflow_case_1(self):
        text = "bdbdbbd"
        k = 2
        actual = longest_substring_with_k_distinct(text, k)
        self.assertEqual(actual, 7)

    def test_stackoverflow_case_2(self):
        text = "bcbdbdbbdcd"
        k = 3
        actual = longest_substring_with_k_distinct(text, k)
        self.assertEqual(actual, 11)

    def test_stackoverflow_case_3(self):
        text = "abcbdbdbbdcdabd"
        k = 5
        actual = longest_substring_with_k_distinct(text, k)
        self.assertEqual(actual, 15)


if __name__ == "__main__":
    main()
