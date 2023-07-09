from unittest import TestCase, main
from warmup.shortest_word_distance import shortestDistance


class TestShortestDistance(TestCase):

    def test_example_1(self):
        words = ["practice", "makes", "perfect", "coding", "makes"]
        word1 = "coding"
        word2 = "practice"
        expected = 3
        actual = shortestDistance(words, word1, word2)
        self.assertEqual(expected, actual)

    def test_example_2(self):
        words = ["the", "quick", "brown", "fox",
                 "jumped", "over", "the", "lazy", "dog"]
        word1 = "fox"
        word2 = "dog"
        expected = 4
        actual = shortestDistance(words, word1, word2)
        print(actual)  # add this line
        self.assertEqual(expected, actual)

    # def test_example_2(self):
    #     words = ["the", "quick", "brown", "fox",
    #              "jumped", "over", "the", "lazy", "dog"]
    #     word1 = "fox"
    #     word2 = "dog"
    #     expected = 4
    #     actual = shortestDistance(words, word1, word2)
    #     self.assertEqual(expected, actual)

    def test_leetcode_1(self):
        words = ["practice", "makes", "perfect", "coding", "makes"]
        word1 = "coding"
        word2 = "practice"
        expected = 3
        actual = shortestDistance(words, word1, word2)
        self.assertEqual(expected, actual)

    def test_leetcode_2(self):
        words = ["practice", "makes", "perfect", "coding", "makes"]
        word1 = "makes"
        word2 = "coding"
        expected = 1
        actual = shortestDistance(words, word1, word2)
        self.assertEqual(expected, actual)

    def test_empty_words(self):
        words = []
        word1 = "hello"
        word2 = "world"
        expected = len(words)
        actual = shortestDistance(words, word1, word2)
        self.assertEqual(expected, actual)

    def test_same_word(self):
        words = ["apple", "banana", "orange", "apple", "grape"]
        word1 = "apple"
        word2 = "apple"
        expected = 0
        actual = shortestDistance(words, word1, word2)
        self.assertEqual(expected, actual)

    def test_word_not_found(self):
        words = ["cat", "dog", "bird", "fish"]
        word1 = "cat"
        word2 = "lion"
        expected = len(words)
        actual = shortestDistance(words, word1, word2)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
