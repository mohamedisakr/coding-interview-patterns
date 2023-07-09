def reverseVowels(s: str) -> str:
    # create a set of vowels for easy lookup
    vowels = set("aeiouAEIOU")
    # convert the string to a list of characters
    chars = list(s)

    # initialize two pointers, one from the left and one from the right
    left = 0
    right = len(chars) - 1

    # loop until the pointers meet
    while left < right:
        # if the left character is not a vowel, move the left pointer to the right
        if chars[left] not in vowels:
            left += 1
        # if the right character is not a vowel, move the right pointer to the left
        elif chars[right] not in vowels:
            right -= 1
        # otherwise, swap the left and right characters and move both pointers
        else:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    # return the modified list as a string
    return "".join(chars)


print(reverseVowels("hello"))  # output: holle
print(reverseVowels("Egypt"))  # output: Egytp
print(reverseVowels("AEIOU"))  # output: UOIEA


'''
def reverseVowels(s: str) -> str:
    txt = list(s.replace(" ", "").lower())
    vowels = "aeiou"
    start = 0
    end = len(txt)-1

    while start < end:
        while start < end and vowels.find(txt[start]) == -1:
            start += 1

        while start < end and vowels.find(txt[end]) == -1:
            end -= 1

        txt[start], txt[end] = txt[end], txt[start]

        start += 1
        end -= 1

    return ''.join(txt)
'''
