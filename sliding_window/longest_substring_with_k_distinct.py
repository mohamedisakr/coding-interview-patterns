
def longest_substring_with_k_distinct(text, k):
    """find the length of the longest substring in it with no more 
    than K distinct characters.

    This function uses dynamic sliding window.

    Args:
        text: The input string (array of characters). Must not be empty.

        k: The no of distinct characters. Must be positive and 
            not larger than the length of the string.

    Returns:
        the length of the longest substring in it with no more than 
        K distinct characters.

    Raises:
        ValueError: If k is zero or negative
        ValueError: If k is larger than the length of the array.
        ValueError: If text the input string is empty.
        TypeError: If k is not an integer.
    """
    # Check for preconditions

    # check if k is an iteger
    if not isinstance(k, int):
        raise TypeError("k must be an integer")

    if not isinstance(text, str):
        raise TypeError("text must be string")

    # assert text, "text must not be empty"
    if len(text) <= 0:
        raise ValueError("text must not be empty")

    # assert s > 0, "s must be positive"
    if k <= 0:
        raise ValueError("k must be positive")

    # assert k <= len(arr), "k must not be larger than the length of the array"
    if k > len(text):
        raise ValueError("k must not be larger than the length of the string")

    # arr must be array of positive numbers
    # if any(item < 0 for item in arr):
    #     raise ValueError("all elements must be positive")

    start = 0
    max_len = 0
    char_freq = {}

    for end, element in enumerate(text):  # range(len(text)):
        rite_char = text[end]

        if rite_char not in char_freq:
            char_freq[rite_char] = 0
        char_freq[rite_char] += 1

        while len(char_freq) > k:
            left_chat = text[start]
            char_freq[left_chat] -= 1
            if char_freq[left_chat] == 0:
                del char_freq[left_chat]
            start += 1
        max_len = max(max_len, end-start+1)

    return max_len


'''
print('test case 1')
text = "araaci"
k = 2
actual = longest_substring_with_k_distinct(text, k)
print(f'actual = {actual}, expected = {4}, then {actual == 4}')

print('')

print('test case 2')
text = "araaci"
k = 1
actual = longest_substring_with_k_distinct(text, k)
print(f'actual = {actual}, expected = {2}, then {actual == 2}')

print('')

print('test case 3')
text = "cbbebi"
k = 3
actual = longest_substring_with_k_distinct(text, k)
print(f'actual = {actual}, expected = {5}, then {actual == 5}')
# '''
