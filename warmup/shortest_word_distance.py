def shortestDistance(words: list[str], word1: str, word2: str) -> int:
    # if the words are the same, return 0
    if word1 == word2:
        return 0

    # initialize the indices and the minimum distance
    index1 = -1
    index2 = -1
    min_dist = len(words)
    n = len(words)

    # loop through the words array
    for i in range(n):
        # update the index of word1 or word2 if found
        if words[i] == word1:
            index1 = i
        elif words[i] == word2:
            index2 = i

        # if both indices are valid, calculate the distance and update the minimum
        if index1 != -1 and index2 != -1:
            dist = abs(index1 - index2)
            min_dist = min(min_dist, dist)

    # return the minimum distance
    return min_dist


the_words = ["the", "quick", "brown", "fox",
             "jumps", "over", "the", "lazy", "dog"]
word1 = "fox"
word2 = "dog"
expected = 5

actual = shortestDistance(the_words, word1, word2)
print(actual == expected)

'''
# sample input
words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"

# expected output
3

# sample input
words = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
word1 = "fox"
word2 = "dog"

# expected output
4

'''
